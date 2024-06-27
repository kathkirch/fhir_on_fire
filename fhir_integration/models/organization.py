from fhir.resources.organization import Organization
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address

def map_to_organization(extracted_organization_info):
    org_name = extracted_organization_info.get("orgName")
    street_number = extracted_organization_info.get("address_street_number")
    fax = extracted_organization_info.get("fax")
    url = extracted_organization_info.get("webAdress")
    
    data_in = {
        "resourceType": "Organization",
        "meta": {
            "profile": ["http://localhost:8080/fhir/StructureDefinition/medicinal-organization"]
        },
        "name": org_name,
        "text": {
            "status": "generated",
            "div": f"<div xmlns=\"http://www.w3.org/1999/xhtml\"><h1>{org_name}</h1></div>"
        }
    }
    organization = Organization(**data_in)
   
    if street_number:
       organization.contact = [{
            "address": {
                "text": 
                    (
                        f'{street_number}, '
                        f'{extracted_organization_info.get("address_zip")} '
                        f'{extracted_organization_info.get("address_city")}, '
                        f'{extracted_organization_info.get("address_country")}'
                    ),
                "line": [street_number],
                "city": extracted_organization_info.get("address_city"),
                "postalCode": extracted_organization_info.get("address_zip"),
                "country": extracted_organization_info.get("address_country")
            }
        }]
    else:
        organization.contact = [{
            "address": {
                "text": 
                    (
                        f'{extracted_organization_info.get("address_zip")} '
                        f'{extracted_organization_info.get("address_city")}, '
                        f'{extracted_organization_info.get("address_country")}'
                    ),
                "city": extracted_organization_info.get("address_city"),
                "postalCode": extracted_organization_info.get("address_zip"),
                "country": extracted_organization_info.get("address_country")
            }
        }] 

    if fax: 
        if not organization.contact[0].telecom:
            organization.contact[0].telecom = []
        organization.contact[0].telecom.append(ContactPoint(system="fax", value=fax))
    if url: 
        if not organization.contact[0].telecom:
            organization.contact[0].telecom = []
        organization.contact[0].telecom.append(ContactPoint(system="url", value=url))

    return organization