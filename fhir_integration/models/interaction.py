import re
from fhir.resources.clinicalusedefinition import ClinicalUseDefinition

def map_to_interaction(interaction):
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
            "text": "Wechselwirkung mit anderen Medikamenten"},
            "effect": {
                "concept": {
                    "text": interaction
                }
            }
        }
    }
    interaction = ClinicalUseDefinition(**data_in)
    return interaction

def split_interactions(interaction_string): 
    entries = interaction_string.split('|')
    interaction_list = []
    for entry in entries:
        entry = entry.strip()
        interaction_list.append(entry)
    return interaction_list
