import fhirpy

class FHIRClient:

    def __init__(self, base_url):
        self.client = fhirpy.SyncFHIRClient(base_url)

    def validate_resource(self, resource_type, resource_data):
        resource = self.client.resource(resource_type, **resource_data)
        return resource.is_valid(raise_exception=True)

    def save_resource(self, resource_type, resource_data):
        resource = self.client.resource(resource_type, **resource_data)
        resource.save()
        return resource

    def expand_value_set(self, value_set_url):
        value_set = self.client.reference(f"ValueSet?url={value_set_url}").fetch()
        return value_set.perform(operation='$expand')