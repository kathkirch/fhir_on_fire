from decimal import Decimal
from collections import OrderedDict
from datetime import date
from fhir_integration.services.fhir_client import FHIRClient

class ValidationService: 

    def __init__(self, base_url):
        self.client = FHIRClient(base_url)

    def validate_organization(self, organization):
        return self.client.validate_resource('Organization', organization.dict())

    def validate_mpd(self, mpd):
        data = convert_to_serializable(mpd.dict())
        return self.client.validate_resource('MedicinalProductDefinition', data)
    
    def validate_medicationKnowledge(self, medicationKnowledge):
        data = convert_to_serializable(medicationKnowledge.dict())
        return self.client.validate_resource('MedicationKnowledge', data)

    def validate_clinicalUseDefinition(self, clinicalUseDefinition):
        return self.client.validate_resource('ClinicalUseDefinition', clinicalUseDefinition.dict())


def convert_to_serializable(data):
    if isinstance(data, OrderedDict):
        # Convert OrderedDict to a regular dict recursively
        return {key: convert_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        # Apply the conversion to each item in the list
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, Decimal):
        # Convert Decimal to float
        return float(data)
    elif isinstance(data, date):
        # Convert date to string in ISO format
        return data.isoformat()
    return data