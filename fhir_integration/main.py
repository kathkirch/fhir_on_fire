import json
import os
from fhir_integration.llm_services.llm_multiple import LLMMultiple
from fhir_integration.services.validation_service import ValidationService
from fhir_integration.services.store_service import StorageService
from fhir_integration.models.organization import map_to_organization
from fhir_integration.llm_services.questions import questions_mpd
from fhir_integration.models.medicinalProductDefinition import map_to_mpd

generated_path = 'fhir_integration/generated/'


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

    validation_service = ValidationService(base_url)


    # Lesen des Beipackzettel-Textes aus einer Datei
    leaflet_file_path = 'leaflet_as_txt/1-19251.txt'
    with open(leaflet_file_path, 'r') as file:
        leaflet_text = file.read()

    # # Extrahieren der Organization Informationen mit LLM
    # llm_service = LLMServiceOrganization() --> old
    # llm_service = LLMSingle() --> new 
    # if check_if_json_exists(generated_path, '1-19251.json'):
    #     with open(f'{generated_path}1-19251.json', 'r') as json_file:
    #         extracted_info = json.load(json_file)
    # else:
    #     extracted_info = llm_service.extract_organization_info(leaflet_text)
    #     with open(f'{generated_path}1-19251.json', 'w') as json_file:
    #         json.dump(extracted_info, json_file, indent=4)
    
   

    # # Zuordnen zur Organization-Ressource
    # organization = map_to_organization(extracted_info)


    # # Validieren und Speichern der Organization-Ressource
    # validation_response = validation_service.validate_organization(organization)

    # if validation_response:
    #     stored_organization = storage_service.store_organization(organization)
    #     print("Organization resource created:", stored_organization)
    #     organization_id = stored_organization['id']
    #     print(organization_id)
    # else:
    #     print("Organization validation failed:", validation_response)
    
    # Extrahieren der MedicinalProductDefinition Informationen mit LLM
    llm_mpd = LLMMultiple(questions = questions_mpd)
    if check_if_json_exists(generated_path, '1-19251_mpd.json'):
        with open(f'{generated_path}1-19251_mpd.json', 'r', encoding='utf-8') as json_file:
            extracted_info = json.load(json_file)
    else:
        extracted_info = llm_mpd.extract_info(leaflet_text)
        with open(f'{generated_path}1-19251_mpd.json', 'w') as json_file:
            json.dump(extracted_info, json_file, ensure_ascii=False, indent=4)
    
    
    organization_id = "56" # derzeit hardcoded sonst dynamisch
    # Step 4: Map to MedicinalProductDefinition resource with the correct code and display name
    mpd = map_to_mpd(extracted_info, organization_id)

    # Validate and store MedicinalProductDefinition resource
    validation_response = validation_service.validate_mpd(mpd)
    print(f"valid response {validation_response}")
    # if validation_response['issue'][0]['severity'] == 'error':
    #     print("MedicinalProductDefinition validation failed:", validation_response)
    # else:
    #     stored_mpd = storage_service.store_mpd(mpd)
    #     print("MedicinalProductDefinition resource created:", stored_mpd)

# if __name__ == '__main__':
main()