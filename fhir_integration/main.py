import json
import os
import sys
from fhir_integration.llm_services.llm_multiple import LLMMultiple
from fhir_integration.llm_services.llm_single import LLMSingle
from fhir_integration.models.contraindication import map_to_contraindication, split_contraindications
from fhir_integration.models.interaction import map_to_interaction, split_interactions
from fhir_integration.models.medicationKnowledge import add_cud_references, map_to_medKnow
from fhir_integration.models.sideEffect import map_to_sideEffect, spilt_side_effects_by_frequency
from fhir_integration.models.warning import map_to_warning, split_warnings
from fhir_integration.services.validation_service import ValidationService
from fhir_integration.services.store_service import StorageService
from fhir_integration.models.organization import map_to_organization
from fhir_integration.llm_services.questions import questions_mpd
from fhir_integration.llm_services.questions import questions_medical_knowledge
from fhir_integration.llm_services.questions import questions_undesirable_effects
from fhir_integration.llm_services.questions import questions_organization
from fhir_integration.llm_services.questions import questions_icw
from fhir_integration.models.medicinalProductDefinition import map_to_mpd

generated_path = 'fhir_integration/generated/'
list_cuds = []

valid_org = False
valid_cud = False
valid_mpd = False
valid_mk = False

org_id = 0
mpd_id = 0

def check_if_json_exists(folder_path, file_name):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)
    
    # Check if the JSON file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False
    

def main():
    base_url = 'http://localhost:8080/fhir'

    ## Service initialization
    validation_service = ValidationService(base_url)
    storage_service = StorageService(base_url)

    ## read leaflet text
    leaflet_file_path = 'leaflet_as_txt/1-19251.txt'
    with open(leaflet_file_path, 'r') as file:
        leaflet_text = file.read()

    # Extract information for Organization-Resource from llm 
    if check_if_json_exists(generated_path, '1-19251_org.json'):
        with open(f'{generated_path}1-19251_org.json', 'r') as json_file:
            extracted_org_info = json.load(json_file)
    else:
        llm_org = LLMMultiple(questions=questions_organization) 
        extracted_org_info = llm_org.extract_info(leaflet_text)
        with open(f'{generated_path}1-19251_org.json', 'w') as json_file:
            json.dump(extracted_org_info, json_file, indent=4)
    
    ## Create organization Resource & validate & send to server if valid
    organization_resource = map_to_organization(extracted_org_info)
    validation_response = validation_service.validate_organization(organization_resource)
    if validation_response:
        stored_organization = storage_service.store_organization(organization_resource)
        org_id = stored_organization['id']
        print("Organization resource added")
    else:
        #TODO error handling if not valid
        print("Organization validation failed:", validation_response)
    
    ## Extract information for MedicinalProductDefinition-Resource from llm 
    if check_if_json_exists(generated_path, '1-19251_mpd.json'):
        with open(f'{generated_path}1-19251_mpd.json', 'r', encoding='utf-8') as json_file:
            extracted_mpd_info = json.load(json_file)
    else:
        llm_mpd = LLMMultiple(questions = questions_mpd)
        extracted_mpd_info = llm_mpd.extract_info(leaflet_text)
        with open(f'{generated_path}1-19251_mpd.json', 'w') as json_file:
            json.dump(extracted_mpd_info, json_file, ensure_ascii=False, indent=4)

    ## Create MedicinalProductDefinition-Resource, validate and send to server if valid
    mpd = map_to_mpd(extracted_mpd_info, org_id)
    validation_response = validation_service.validate_mpd(mpd)
    if validation_response:
        stored_mpd = storage_service.store_mpd(mpd)
        mpd_id = stored_mpd['id']
        print("MedicinalProductDefinition added")
    else:
        #TODO error handling
        print("MedicinalProductDefinition validation failed:", validation_response)
       
    ## Extract undesirable effect information from llm 
    if check_if_json_exists(generated_path, '1-19251_undes.json'):
        with open(f'{generated_path}1-19251_undes.json', 'r', encoding='utf-8') as json_file:
            extracted_undes_effect_info = json.load(json_file)
    else:
        llm_undes = LLMSingle(questions = questions_undesirable_effects)
        extracted_undes_effect_info = llm_undes.extract_info(leaflet_text)
        with open(f'{generated_path}1-19251_undes.json', 'w') as json_file:
            json.dump(extracted_undes_effect_info, json_file, ensure_ascii=False, indent=4)

    ## Create ClinicalUseDefinition-Resources (type = undesireable effect) & validate them and send to server:
    undesireable_effect_pairs = spilt_side_effects_by_frequency(extracted_undes_effect_info.get("undesirable_effects"))
    for pair in undesireable_effect_pairs: 
        undes_resource =  map_to_sideEffect(pair.get("side_effect"), pair.get("frequency"))
        validation_response = validation_service.validate_clinicalUseDefinition(undes_resource)
        if validation_response:
            stored_undes = storage_service.store_cud(undes_resource)
            cud_to_add = add_cud_references(id=stored_undes['id'], definition='undesirable-effect')
            list_cuds.append(cud_to_add)
        else: 
            #TODO error handling
            print("ClinicalUseDefinition (type=undesirable effect) validation failed:", validation_response)
            sys.exit()

    # ## Extract ClinicalUseDefinition information from llm 
    if check_if_json_exists(generated_path, '1-19251_icw.json'):
        with open(f'{generated_path}1-19251_icw.json', 'r', encoding='utf-8') as json_file:
            extracted_icw_info = json.load(json_file)
    else:
        llm_cud = LLMMultiple(questions = questions_icw)
        extracted_icw_info = llm_cud.extract_info(leaflet_text)
        with open(f'{generated_path}1-19251_icw.json', 'w') as json_file:
            json.dump(extracted_icw_info, json_file, ensure_ascii=False, indent=4)
       

    ## Create contraindication Resources & validate them 
    contraindication_string = extracted_icw_info.get("contraindications")
    contraindications = split_contraindications(contraindication_string)
    for contraindication in contraindications:
        contraindication_resource = map_to_contraindication(contraindication)
        validation_response = validation_service.validate_clinicalUseDefinition(contraindication_resource)
    if validation_response:
        stored_undes = storage_service.store_cud(undes_resource)
        cud_to_add = add_cud_references(id=stored_undes['id'], definition='contraindication')
        list_cuds.append(cud_to_add)
    else: 
        #TODO error handling
        print("ClinicalUseDefinition (type=contraindication) validation failed:", validation_response)  

    ## Create interaction Resources & validate them
    interaction_string = extracted_icw_info.get("interaction_medications")
    interactions = split_interactions(interaction_string)
    for interaction in interactions:
        interaction_resource = map_to_interaction(interaction)
        validation_response = validation_service.validate_clinicalUseDefinition(interaction_resource)
    if validation_response:
        stored_undes = storage_service.store_cud(undes_resource)
        cud_to_add = add_cud_references(id=stored_undes['id'], definition='interaction')
        list_cuds.append(cud_to_add)
    else: 
        #TODO error handling
        print("ClinicalUseDefinition (type=interaction) validation failed:", validation_response)

    ## Create warning Resource & validate them 
    hint_string = extracted_icw_info.get('hints')
    hints = split_warnings(hint_string)
    for hint in hints:
        warning_hint_resource = map_to_warning(hint)
        validation_response = validation_service.validate_clinicalUseDefinition(warning_hint_resource)
    if validation_response:
        stored_undes = storage_service.store_cud(undes_resource)
        cud_to_add = add_cud_references(id=stored_undes['id'], definition='warning')
        list_cuds.append(cud_to_add)
    else: 
        #TODO error handling
        print("ClinicalUseDefinition (type=warning) validation failed:", validation_response)

    warning_string = extracted_icw_info.get('warning_other')
    warnings = split_warnings(warning_string)
    for warning in warnings:
        warning_resource = map_to_warning(warning)
        validation_response = validation_service.validate_clinicalUseDefinition(warning_resource)
        print(validation_response)
    if validation_response:
        stored_undes = storage_service.store_cud(undes_resource)
        cud_to_add = add_cud_references(id=stored_undes['id'], definition='warning')
        list_cuds.append(cud_to_add)
    else: 
        #TODO error handling
        print("ClinicalUseDefinition (type=undesirable effect) validation failed:", validation_response)

    ## Extract MedicalKnowledge information from llm 
    if check_if_json_exists(generated_path, '1-19251_mk.json'):
        with open(f'{generated_path}1-19251_mk.json', 'r', encoding='utf-8') as json_file:
            extracted_mk_info = json.load(json_file)
    else:
        llm_mk = LLMMultiple(questions = questions_medical_knowledge)
        extracted_mk_info = llm_mk.extract_info(leaflet_text)
        with open(f'{generated_path}1-19251_mk.json', 'w') as json_file:
            json.dump(extracted_mk_info, json_file, ensure_ascii=False, indent=4)

    ## Create MedicalKnowledge-Resource validate append ClinicalUseDefinition Resources and send to server
    mk_resource = map_to_medKnow(extracted_mk_info, mpd_id, list_cuds, extracted_mpd_info.get('admission_nr'))
    validation_response = validation_service.validate_medicationKnowledge(mk_resource)
    if validation_response:
        storage_service.store_mk(mk_resource)
        print('MedicationKnowledge added')
    else:
        #TODO error handling
        print("MedicationKnowledge validation failed:", validation_response)

main()