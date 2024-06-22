from collections import OrderedDict
from decimal import Decimal
from datetime import date
from fhir_integration.services.fhir_client import FHIRClient


class StorageService:

    def __init__(self, base_url):
        self.client = FHIRClient(base_url)

    def store_organization(self, organization):
        created_resource = self.client.save_resource('Organization', organization.dict())
        return created_resource
    
    def store_mpd(self, mpd):
        data = convert_to_serializable(mpd.dict())
        created_resource = self.client.save_resource('MedicinalProductDefinition', data)
        return created_resource  

    def store_cud(self, cud):
        created_resource = self.client.save_resource('ClinicalUseDefinition', cud.dict())
        return created_resource 

    def store_mk(self, mk):
        data = convert_to_serializable(mk.dict())
        created_resource = self.client.save_resource('MedicationKnowledge', data) 
        return created_resource   
    

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