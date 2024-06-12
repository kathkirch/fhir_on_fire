import re
from fhir.resources.clinicalusedefinition import ClinicalUseDefinition

def map_to_interaction(extracted_interaction_info):
    data_in = {  
        "resourceType" : "ClinicalUseDefinition",
        "meta" : {
            "profile": ["http://localhost:8080/fhir/StructureDefinition/interaction"]
        },
        "text" : {
            "status" : "generated",
            "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n\n<p>Interaction</p>\n\n</div>"
        },
        "type" : "interaction",
        "interaction" : {
            "type": {
            "text": "Placeholder for type of interaction drug to drug, acohol etc."},
            "effect": {
                "concept": {
                    "text": "the interaction"
                }
            }
        }
    }
    interaction = ClinicalUseDefinition(**data_in)
    return interaction


##TODO regex alcohol medication
