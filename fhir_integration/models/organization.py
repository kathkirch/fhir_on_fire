from fhir.resources.organization import Organization
from fhir.resources.contactpoint import ContactPoint

def map_to_organization(extracted_organization_info):
    organization = Organization(
        resourceType = "Organization",
        meta = {"profile": "http://localhost.org/StructureDefinition/medicinal-organization"}
            identifier = [{
                "value": extracted_organization_info.get("shortnameAsID")
            }],
            name = extracted_organization_info.get("orgName"),
            contact = [{
                "address": {
                    "text": extracted_organization_info.get("address_street_number"),
                    "line": [extracted_organization_info.get("address_street_number")],
                    "city": extracted_organization_info.get("address_city"),
                    "postalCode": extracted_organization_info.get("address_zip"),
                    "country": extracted_organization_info.get("address_country")
                }
            }]
    )

    if "fax" in extracted_organization_info: 
        if not organization.contact.telecom:
            organization.contact.telecom = []
        organization.contact.telecom.append(ContactPoint(system="fax", value=extracted_organization_info.get("fax")))
    if "webAdress" in extracted_organization_info: 
        if not organization.contact.telecom :
            organization.contact.telecom = []
        organization.contact.telecom.append(ContactPoint(system="url", value=extracted_organization_info.get("webAddress")))

    return organization