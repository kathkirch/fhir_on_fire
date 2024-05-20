# fhir_integration/services/lookup_service.py
from fhir_integration.services.fhir_client import FHIRClient

class LookupService:
    
    def __init__(self, base_url):
        self.client = FHIRClient(base_url)

    def find_matching_code(self, value_set_url, search_text):
        expanded_value_set = self.client.expand_value_set(value_set_url)
        for concept in expanded_value_set['expansion']['contains']:
            if search_text.lower() in concept['display'].lower():
                return concept
        return None