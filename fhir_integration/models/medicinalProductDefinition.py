

def map_to_mpd(extracted_mpd_info):
    mpd = MedicinalProductDefinition(
        resourceType = "MedicinalProductDefintion",
            meta = {"profile": "http://localhost.org/StructureDefinition/mpdProfile"}, #not mapped but fix value
            identifier = [{"value": info_mpd.get("admission_nr")}],
            name = [{
                "productName": info_mpd.get("fullName"),
                "part": [{
                    "part": info_mpd.get("nameDoseFormPart") ,
                    "type": { #also fix value
                        "coding" : [{
                            "system" : "http://hl7.org/fhir/medicinal-product-name-part-type",
                            "code" : "DoseFormPart",
                            "display" : "Pharmaceutical dose form part"
                        }],
                        "text": info_mpd.get("nameDoseFormPart")  #ev ändern zu "Dosierform? wenn dann auch im IG usw."
                    }
                },
                {
                    "part": info_mpd.get("nameStrengthPart"), 
                    "type": { #also fix value
                        "coding" : [{
                            "system" : "http://hl7.org/fhir/medicinal-product-name-part-type",
                            "code" : "FormulationPart",
                            "display" : "Formulation part"
                        }],
                        "text": info_mpd.get("nameStrengthPart")  #ev ändern zu "Stärke"? wenn dann auch im IG usw."
                    }
                },
                {
                    "part" : info_mpd.get("namePopulationPart"),
                    "type" : { #also fix value
                        "coding" : [{ 
                            "system" : "http://hl7.org/fhir/medicinal-product-name-part-type",
                            "code" : "PopulationPart",
                            "display" : "Target population part"
                        }],
                        "text": info_mpd.get("namePopulationPart")  #ev ändern zu "Population"? wenn dann auch im IG usw."
                        }
                }],
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
                    "reference": "Organization/idBasg"
                }
            }],
            description = info_mpd.get("modeOfAction"),
            indication = info_mpd.get("indication"),
            statusDate = info_mpd.get("creationDate"),
            
            if "blackTriangle" in info_mpd:
                additionalMonitoringIndicator = {
                    "text": info_mpd.get("blackTriangle")
                }   
    )
    return mpd