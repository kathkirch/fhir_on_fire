import json
import os

from fhir_integration.models.contraindication import map_to_contraindication, split_contraindications
from fhir_integration.models.interaction import map_to_interaction
from fhir_integration.models.medicationKnowledge import add_cud_references, map_to_medKnow
from fhir_integration.models.medicinalProductDefinition import map_to_mpd
from fhir_integration.models.organization import map_to_organization
from fhir_integration.models.sideEffect import map_to_sideEffect, spilt_side_effects_by_frequency
from fhir_integration.models.warning import map_to_warning
from fhir_integration.services.store_service import StorageService
from fhir_integration.services.validation_service import ValidationService


def check_if_json_exists(folder_path, file_name):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)
    
    # Check if the JSON file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False

def split_entries_by_line(entry_string):
    entries = entry_string.split('|')
    entry_list = []
    for entry in entries:
        entry = entry.strip()
        entry_list.append(entry)
    return entry_list


class LeafletHandling():
    def __init__(
            self,
            leaflet_text,
            generated_path
    ):
        self._leaflet_text = leaflet_text
        self._generated_path = generated_path

    def extract_info_leaflet(
            self,
            admission_number,
            info_type,
            llm_model
    ):
        extracted_info = self._check_if_extracted(
            admission_number=admission_number,
            info_type=info_type
        )
        if not extracted_info:
            extracted_info = self._extract_info(
                llm_model=llm_model,
                admission_number=admission_number,
                info_type=info_type
            )
        return extracted_info

    def _check_if_extracted(self, admission_number, info_type):
        extracted_info = None
        exists = check_if_json_exists(
            folder_path=self._generated_path,
            file_name=f'{admission_number}_{info_type}.json'
        )
        path_to_check = f'{self._generated_path}{admission_number}_{info_type}.json'
        if exists:
            with open(path_to_check, 'r') as json_file:
                extracted_info = json.load(json_file)
        return extracted_info
    
    def _extract_info(self, llm_model, admission_number, info_type):
        extracted_info = llm_model.extract_info(self._leaflet_text)
        
        path_to_dump = f'{self._generated_path}{admission_number}_{info_type}.json'
        
        with open(path_to_dump, 'w') as json_file:
            json.dump(extracted_info, json_file, indent=4)
        return extracted_info


class ValidateAndSaveResourceStrategy():

    def __init__(self):
        self._validation_service = ValidationService('http://localhost:8080/fhir')
        self._store_service = StorageService('http://localhost:8080/fhir')

    def _map(self):
        pass

    def _validate(self, resource):
        return self._validation_service.validate(resource)

    def _store(self, resource):
        return self._store_service.store(resource)

    def _handle_resource(self): 
        pass


class ValidateAndSaveOrganization(ValidateAndSaveResourceStrategy):
    
    def _map(self, extracted_org_info):
        resource = map_to_organization(extracted_org_info)
        return resource
    
    def handle_resource(self, extracted_org_info):
        resource = self._map(extracted_org_info)
        result = self._validate(resource)
        if result: 
            stored_resource = self._store(resource)
            stored_resource_id = stored_resource['id']
            return stored_resource_id
        else :
            #TODO error handling
            return None
        

class ValidateAndSaveMPD(ValidateAndSaveResourceStrategy):

    def _map(self, extracted_mpd_info, org_id):
        resouce = map_to_mpd(extracted_mpd_info, org_id)
        return resouce
    
    def handle_resource(self, extracted_mpd_info, org_id):
        resource = self._map(extracted_mpd_info, org_id)
        result = self._validate(resource)
        if result: 
            stored_resource = self._store(resource)
            stored_resource_id = stored_resource['id']
            return stored_resource_id
        else :
            #TODO error handling
            return None
        

class ValidateAndSaveUndesirableEffect(ValidateAndSaveResourceStrategy):

    def _map(self, sideEffect, frequency):
            resouce = map_to_sideEffect(sideEffect, frequency)
            return resouce
        
    def handle_resource(self, extracted_undes_effect_info):
        result_ids = []
        effect_pairs = spilt_side_effects_by_frequency(extracted_undes_effect_info.get("undesirable_effects"))
        for pair in effect_pairs:
            sideEffect = pair.get("sideEffect")
            frequency = pair.get("frequency")
            resource = self._map(sideEffect, frequency)
            result = self._validate(resource)
            if result:
                stored_resource = self._store(resource)
                cud_to_add = add_cud_references(id=stored_resource['id'], definition='undesirable-effect')
                result_ids.append(cud_to_add)
            else : 
                #TODO error handling
                print(result)
        return result_ids


class ValidateAndSaveCUD(ValidateAndSaveResourceStrategy):
    
    def _map(self):
        pass
    
    def _handle_resource(self, extractedInfo, definition):
        result_ids = []
        entries = split_entries_by_line(extractedInfo)
        for entry in entries:
            resource = self._map(entry)
            result = self._validate(resource)
            if result:
                stored_resource = self._store(resource)
                cud_to_add = add_cud_references(id=stored_resource['id'], definition=definition)
                result_ids.append(cud_to_add)
            else : 
                #TODO error handling 
                print(result)
        return result_ids


class ValidateAndSaveContraindication(ValidateAndSaveCUD):
    def _map(self, entry):
        resource = map_to_contraindication(entry)
        return resource  

    def handle_resource(self, extracted_info, definition):
        return super()._handle_resource(extracted_info, definition)  


class ValidateAndSaveInteraction(ValidateAndSaveCUD):
    def _map(self, entry):
        resource = map_to_interaction(entry)
        return resource
    
    def handle_resource(self, extracted_info, definition):
        return super()._handle_resource(extracted_info, definition)
    

class ValidateAndSaveWarning(ValidateAndSaveCUD):
    def _map(self, entry):
        resource = map_to_warning(entry)
        return resource
    
    def handle_resource(self, extracted_info, definition):
        return super()._handle_resource(extracted_info, definition)
    

class ValidateAndSaveMK(ValidateAndSaveResourceStrategy):
    def _map(self, extracted_mk_info, mpd_id, list_cud_ids, admission_nr):
        resource = map_to_medKnow(
            extracted_medKnow_info=extracted_mk_info, 
            id_mpd=mpd_id, 
            cud_list=list_cud_ids,
            admission_nr=admission_nr)
        return resource

    def handle_resource(self, extracted_info, mpd_id, list_cud_ids, admission_nr):
        resouce = self._map(extracted_info, mpd_id, list_cud_ids, admission_nr)
        result = self._validate(resouce)
        if result:
            self._store(resouce)
        else: 
            #TODO error handling 
            print(result)