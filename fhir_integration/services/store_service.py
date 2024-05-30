from fhir_integration.services.fhir_client import FHIRClient


class StorageService:

    def __init__(self, base_url):
        self.client = FHIRClient(base_url)

    def store_organization(self, organization):
        created_resource = self.client.save_resource('Organization', organization.dict())
        return created_resource
    
    def store_mpd(self, mpd):
        created_resource = self.client.save_resource('MedicinalProductDefinition', mpd.dict())
        return created_resource        