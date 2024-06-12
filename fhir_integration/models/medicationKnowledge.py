from fhir.resources.medicationknowledge import MedicationKnowledge

def map_to_medKnow(extracted_medKnow_info, admission_nr, id_mpd): 

    name = extracted_medKnow_info.get("name_medication")
    doseform = extracted_medKnow_info.get("doseform")

    data_in = {
        "resourceType": "MedicationKnowledge",
        "status": "active",
        "meta" : {
            "profile": ["http://localhost:8080/fhir/StructureDefinition/medicationKnowledge-leaflet"]
        },
        "indicationGuideline": [{
            "dosingGuideline": [
            {
                "dosage": [{
                    "type": {
                        "coding": [{
                            "system" : "http://snomed.info/sct", 
                            "code" : "223422006",
                            "display": "Recommendation regarding what to do if drug omitted"
                        }],
                        "text": f"Wenn Sie die Einnahme von {name} vergessen haben"
                    },
                    "dosage": [{
                        "patientInstruction": extracted_medKnow_info.get("forgotten")
                    }]
                }]
            },
            {
                "dosage": [{
                    "type": {
                        "coding": [{
                            "system" : "http://snomed.info/sct", 
                            "code" : "410546004",
                            "display": "Discontinued"
                        }],
                        "text": f"Wenn Sie die Einnahme von {name} abbrechen"
                    },
                    "dosage": [{
                        "patientInstruction": extracted_medKnow_info.get("quit")
                        
                    }]
                }]
            },
            {
                "dosage": [{
                    "type": {
                        "coding": [{
                            "system" : "http://snomed.info/sct", 
                            "code" : "260378005",
                            "display": "Excessive"
                        }],
                        "text": f"Wenn Sie eine größere Menge von {name} eingenommen haben, als Sie sollten"
                    },
                    "dosage": [{
                        "patientInstruction": extracted_medKnow_info.get("too_much")
                    }]
                }]
            },
            {
                "dosage": [{
                    "type": {
                        "coding": [{
                            "system" : "http://snomed.info/sct", 
                            "code" : "261773006", 
                            "display":  "Duration of therapy"
                        }],
                        "text": "Maximale Einnahmedauer wenn nicht anders ärztlich verordnet"
                    },
                    "dosage": [{
                        "patientInstruction": extracted_medKnow_info.get("hint_intake_duration"),
                        
                    }]
                }]
            },    
            {
                "dosage": [{
                    "type": {
                        "coding": [{
                            "system" : "http://snomed.info/sct", 
                            "code" : "422096002",
                            "display": "Dosing instruction fragment"
                        }],
                        "text": "Empfohlene Einnahme wenn nicht anders ärztlich verordnet"
                    },
                    "dosage": [{
                        "patientInstruction": extracted_medKnow_info.get("patient_instruction") ,
                        "additionalInstruction":[{
                                "text": extracted_medKnow_info.get("additional_instruction")
                        }],
                        "route": {
                            "text": extracted_medKnow_info.get("route")
                        },
                        "doseAndRate": [{
                            "doseQuantity": {
                                    "value": extracted_medKnow_info.get("dose_and_rate"),
                                    "unit": doseform
                            }
                        }],
                        "maxDosePerAdministration": {
                            "value": extracted_medKnow_info.get("max_dose_per_intake"),
                            "unit": doseform
                        },
                        "maxDosePerPeriod": [
                        {
                            "numerator": {
                                "value": extracted_medKnow_info.get("max_dose_per_period"),
                                "unit": doseform
                            },
                            "denominator": {
                                "value": 1,
                                "unit": "Tag"
                            }
                        }]
                    }]
                }]
            }]
        }],
        "storageGuideline": [{
            "note": [{
                "text": extracted_medKnow_info.get("storage_guideline"),
            }],
           
        }],    
        "definitional": {
            "definition": [{
                "reference": f"MedicinalProductDefinition/{id_mpd}"
            }], 
            "doseForm": {
                "text": doseform
            },
            "drugCharacteristic": [{
                "valueString": extracted_medKnow_info.get("storage_guideline")
            }]
        }
    }

    medication_knowledge = MedicationKnowledge(**data_in)

    return medication_knowledge



        
    

    # def add_cud_references(
    #         list_side_effects,
    #         list_warnings,
    #         list_contraindication,
    #         list_interaction
    #     )



def add_cud_references(
    id,
    definition,
    reference: str = "ClinicalUseDefinition/",
    display: str = "http://localhost:8080/fhir/StructureDefinition/",
):

    base_dict = {
        "reference": f"{reference}{id}",
        "display": f"{display}{definition}"
    }
    return base_dict

list_results = []

for validate in to_validate:
    definition = "interaction"
    id = get_id_to_definition()

    clinical_use_issue = add_cud_references(id=id, definition=definition)
    list_results.append(clinical_use_issue)


