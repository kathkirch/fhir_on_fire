from fhir.resources.medicinalproductdefinition import MedicinalProductDefinition

def map_to_mpd(extracted_mpd_info, org_manufacturer_id):
    mpd = MedicinalProductDefinition(
        resourceType = "MedicinalProductDefintion",
        meta = {"profile": ["http://localhost.org/StructureDefinition/mpdProfile"]}, #not mapped but fix value
        identifier = [{"value": extracted_mpd_info.get("admission_nr")}],
        name = [{
            "productName": extracted_mpd_info.get("fullName"),
            "part": [{
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
                        "code" : "FormulationPart",
                        "display" : "Formulation part"
                    }],
                    "text": extracted_mpd_info.get("nameStrengthPart")  #ev ändern zu "Stärke"? wenn dann auch im IG usw."
                }
            },
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
        contact = [{
            "contact": {
                "type": {
                    "text": "Zulasser"
                },
                "reference": "Organization/102" #102 = id basg in db
            }
        },
        {
            "contact": {
                "type": {
                    "text": "Marketing Authorization Holder"
                },
            "reference": f"Organization/{org_manufacturer_id}"
            }
        }],
        description = extracted_mpd_info.get("modeOfAction"),
        indication = extracted_mpd_info.get("indication"),
        statusDate = extracted_mpd_info.get("creationDate"),
         
    )        
    if "blackTriangle" in extracted_mpd_info:
        additionalMonitoringIndicator = {
            "text": extracted_mpd_info.get("blackTriangle")
        }
    


    return mpd