from fhir_integration.llm_services.llm_multiple import LLMMultiple
from fhir_integration.llm_services.llm_single import LLMSingle
from fhir_integration.llm_services.questions import questions_mpd
from fhir_integration.llm_services.questions import questions_medical_knowledge
from fhir_integration.llm_services.questions import questions_undesirable_effects
from fhir_integration.llm_services.questions import questions_organization
from fhir_integration.llm_services.questions import questions_icw
from fhir_integration.utils import LeafletHandling, ValidateAndSaveContraindication, ValidateAndSaveInteraction, ValidateAndSaveMK, ValidateAndSaveMPD, ValidateAndSaveOrganization, ValidateAndSaveUndesirableEffect

generated_path = 'fhir_integration/generated/'
list_cuds = []

def main():
 
    admission_number = '1-19251'
    leaflet_file_path = 'leaflet_as_txt'
    
    ## read leaflet text
    leaflet_file_path = f'{leaflet_file_path}/{admission_number}.txt'
    with open(leaflet_file_path, 'r') as file:
        leaflet_text = file.read()

    ## Instantiate the LLM-Model 
    llm_org = LLMMultiple(questions=questions_organization)
    ## Extract information for Organization-Resource from llm 
    extracted_org_info = LeafletHandling(leaflet_text, generated_path).extract_info_leaflet(
        admission_number = admission_number,
        info_type = "org",
        llm_model = llm_org
    )

    ## Instantiate the LLM-Model 
    llm_mpd = LLMMultiple(questions = questions_mpd)
    ## Extract information for MedicinalProductDefinition-Resource from llm 
    extracted_mpd_info = LeafletHandling(leaflet_text, generated_path).extract_info_leaflet(
        admission_number = admission_number,
        info_type = "mpd",
        llm_model = llm_mpd
    )

    ## Instantiate the LLM-Model
    llm_undes = LLMSingle(questions = questions_undesirable_effects)
    ## Extract undesirable effect information from llm 
    extracted_undes_effect_info = LeafletHandling(leaflet_text, generated_path).extract_info_leaflet(
        admission_number = admission_number,
        info_type = "undes",
        llm_model = llm_undes
    )

    ## Instantiate the LLM-Model
    llm_cud = LLMMultiple(questions = questions_icw)
    ## Extract ClinicalUseDefinition information from llm 
    extracted_icw_info = LeafletHandling(leaflet_text, generated_path).extract_info_leaflet(
        admission_number = admission_number,
        info_type = "icw",
        llm_model = llm_cud
    )

    ## Instantiate the LLM-Model
    llm_mk = LLMMultiple(questions = questions_medical_knowledge)
    ## Extract MedicalKnowledge information from llm 
    extracted_mk_info = LeafletHandling(leaflet_text, generated_path).extract_info_leaflet(
        admission_number = admission_number,
        info_type = "mk",
        llm_model = llm_mk
    )

    ## Create, Validate, and Store Resources
    org_id = ValidateAndSaveOrganization().handle_resource(extracted_org_info)
    mpd_id = ValidateAndSaveMPD().handle_resource(extracted_mpd_info, org_id)
    sideEffect_id_list = ValidateAndSaveUndesirableEffect().handle_resource(extracted_undes_effect_info)
    contraindication_id_list = ValidateAndSaveContraindication().handle_resource(
        extracted_info = extracted_icw_info.get("contraindications"), 
        definition = 'contraindication'
    )
    interaction_id_list = ValidateAndSaveInteraction().handle_resource(
        extracted_info = extracted_icw_info.get("interaction_medications"),
        definition = 'interaction'
    )
    hints_id_list = ValidateAndSaveInteraction().handle_resource(
        extracted_info = extracted_icw_info.get("hints"),
        definition = 'warning'
    )
    warning_id_list = ValidateAndSaveInteraction().handle_resource(
        extracted_info = extracted_icw_info.get("warning_other"),
        definition = 'warning'
    )
    
    ## append all the stored resources id to a dict to add references in MedicationKnowledge Resource
    list_cuds.append(sideEffect_id_list) 
    list_cuds.append(contraindication_id_list)
    list_cuds.append(interaction_id_list)
    list_cuds.append(hints_id_list)
    list_cuds.append(warning_id_list)
    
    ## Create MedicalKnowledge-Resource validate append ClinicalUseDefinition Resources and send to server
    ValidateAndSaveMK().handle_resource(
        extracted_info = extracted_mk_info,
        mpd_id = mpd_id, 
        list_cuds = list_cuds,
        admission_number = extracted_mpd_info.get("admission_nr")
    )

main()