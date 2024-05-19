from fhir_integration.services.fhir_client import fhir_client

class ValidationService: 

    def __init__(self, base_url):
        self.client = FHIRClient(base_url)

    def validate_organization(self, organization)
        return self.client.validate_resource('Organization', organization.dict())

    def validate_mpd(self, medicinalProductDefinition)
        return self.client.validate_resource('MedicinalProductDefinition', medicinalProductDefinition.dict())
    
    def validate_medicationKnowledge(self, medicationKnowledge)
        return self.client.validate_resource('MedicationKnowledge', medicationKnowledge.dict())

    def validate_clinicalUseDefinition(self, validate_clinicalUseDefinition)
        return self.client.validate_resource('ClinicalUseDefinition', clinicalUseDefinition.dict())
