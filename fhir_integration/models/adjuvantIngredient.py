import re
import uuid
from fhir.resources.ingredient import Ingredient

def map_to_adjuvant_ingredient(name):
    unique_id = str(uuid.uuid4())
    data_in = {
        "resourceType" : "Ingredient",
		"id": unique_id,
        "text": {
            "status": "generated",
            "div": f"<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Adjuvant Ingredient</b></p><p><b>Name:</b> {name}</p></div>"
        },
        "meta": {
            "profile": ["http://localhost.org/StructureDefinition/adjuvant-ingredient"]
        },
        "status" : "active",
        "for" : [{
        "reference" : "#"
        }],
        "role" : {
        "coding" : [{
            "system" : "http://hl7.org/fhir/ingredient-role",
            "code" : "100000072073",
            "display": "adjuvant"
        }]
        },
        "substance" : {
            "code" : {
                "concept" : {
                "text": name	
                }
            }
        }
    }
    adjucvant_ing = Ingredient(**data_in)
    return adjucvant_ing

def create_adjuvant_ingredients_from_string(adjuvant_ingredients_string): 
    split_list = adjuvant_ingredients_string.split(';') 
    adj_ingredients = []
    for name in split_list:
        name = name.strip()  # Remove leading and trailing whitespace
        adj_ingredients.append(map_to_adjuvant_ingredient(name))
    return adj_ingredients
        

    
   
