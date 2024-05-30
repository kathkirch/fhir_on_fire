from fhir.resources.medicinalproductdefinition import MedicinalProductDefinition
from fhir.resources.ingredient import Ingredient
from fhir_integration.models.activeIngredient import create_ingredients_from_string
from fhir_integration.models.adjuvantIngredient import create_adjuvant_ingredients_from_string


def map_to_mpd(extracted_mpd_info, org_manufacturer_id):

    active_ingredients = extracted_mpd_info.get("name_strength_active")
    active_ingredients_dict = create_ingredients_from_string(active_ingredients)

    adjuvant_ingredients = extracted_mpd_info.get("name_strength_adjuvant")
    adjuvant_ingredients_dict = create_adjuvant_ingredients_from_string(adjuvant_ingredients)

    data_in = {
        "resourceType": "MedicinalProductDefinition",
        "meta": {"profile": ["http://localhost.org/StructureDefinition/mpdProfile"]}, #not mapped but fix value
        "text": {
            "status": "generated",
            "div": f"<div xmlns=\"http://www.w3.org/1999/xhtml\">MedicianelProductDefinition resource, for {extracted_mpd_info.get('fullName')} .</div>" 
        },
        "identifier": [{"value": extracted_mpd_info.get("admission_nr")}],
        "name": [{
            "productName": extracted_mpd_info.get("fullName"),
            "part": [
            {
                "part": extracted_mpd_info.get("nameDoseFormPart") ,
                "type": { #also fix value
                    "coding" : [{
                        "system" : "http://hl7.org/fhir/medicinal-product-name-part-type",
                        "code" : "DoseFormPart",
                        "display" : "Pharmaceutical dose form part"
                    }],
                    "text": extracted_mpd_info.get("nameDoseFormPart")  #ev ändern zu "Dosierform? wenn dann auch im IG usw."
                }
            },
            {
                "part": extracted_mpd_info.get("nameStrengthPart"), 
                "type": { #also fix value
                    "coding" : [{
                        "system" : "http://hl7.org/fhir/medicinal-product-name-part-type",
                        "code" : "StrengthPart",
                        "display" : "Strength Part"
                    }],
                    "text": extracted_mpd_info.get("nameStrengthPart")  #ev ändern zu "Stärke"? wenn dann auch im IG usw."
                }
            }],
            ## if other names for other languages this strucutre needs to be changed.. 
            "usage" : [{
                "country" : {
                    "coding" : [{
                        "system" : "urn:iso:std:iso:3166",
                        "code" : "AT",
                        "display" : "Austria"
                    }]
                },
                "jurisdiction" : {
                    "coding" : [{
                        "system" : "urn:iso:std:iso:3166",
                        "code" : "AT"
                    }]
                },
                "language" : {
                    "coding" : [{
                        "system" : "urn:ietf:bcp:47",
                        "code" : "de"
                    }]
                }   
            }]
        }],

        # hier noch sowas wie if ensureBasg == true, 
        "contact": [{
            "type": {
                "text": "Zulasser"
            },
            "contact": {
                "reference": "Organization/102" #102 = id basg in db
            } 
        },
        {
            "type": {
                    "text": "Hersteller"
            },
            "contact": {
                "reference": f"Organization/{org_manufacturer_id}"
            }
        }],
        "description": extracted_mpd_info.get("modeOfAction"),
        "indication": extracted_mpd_info.get("indication"),
        "statusDate": extracted_mpd_info.get("creationDate"), 
    }
    
    mpd = MedicinalProductDefinition(**data_in)     
    
    blackTriangle = extracted_mpd_info.get("blackTriangle")
    namePopulationPart = extracted_mpd_info.get("namePopulationPart")

    if blackTriangle:
        mpd.additionalMonitoringIndicator = {
            "text": extracted_mpd_info.get("blackTriangle"),
            "coding": [{
                "system": "http://hl7.org/fhir/medicinal-product-additional-monitoring",
                "code": "BlackTriangleMonitoring",
                "display": "Requirement for Black Triangle Monitoring"
            }], 
        }

    if namePopulationPart: 
        mpd.name[0].part.append(
            {
                "part" : extracted_mpd_info.get("namePopulationPart"),
                "type" : { #also fix value
                    "coding" : [{ 
                        "system" : "http://hl7.org/fhir/medicinal-product-name-part-type",
                        "code" : "PopulationPart",
                        "display" : "Target population part"
                    }],
                    "text": extracted_mpd_info.get("namePopulationPart")  #ev ändern zu "Population"? wenn dann auch im IG usw."
                    }
            }
        )

    mpd.contained = active_ingredients_dict + adjuvant_ingredients_dict
  
    return mpd

