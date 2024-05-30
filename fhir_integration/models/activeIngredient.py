import re
import uuid
from fhir.resources.ingredient import Ingredient


# Create active ingredient resource
def map_to_active_ingredient(name, strength, form):
    unique_id = str(uuid.uuid4())

    # Split the strength into value and unit
    value, unit = re.match(r'(\d+)\s*(\w+)', strength).groups()
    value = value 
    data_in = {
        "resourceType": "Ingredient",
        "id": unique_id,
        "meta" :  {
            "profile": ["http://localhost.org/StructureDefinition/active-ingredient"]
        },
        "identifier" : {"value": name},
        "status" : "active",
        "text" : {
            "status": "generated",
            "div": f"<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Active Ingredient</b></p><p><b>Name:</b> {name}</p></div>"
        },
        "for" : [{
            "reference" : "#"
        }],
        "role" : {
            "coding" : [{
                "system" : "http://hl7.org/fhir/ingredient-role",
                "code" : "100000072072",
                "display": "active"
            }]
        },
        "substance" : {
            "code": {
                "concept": {
                    "text": name,    
                }
            },
            "strength": [{
                "presentationRatio": {
                    "numerator": {
                        "value": value,
                        "unit": unit,
                    },
                    "denominator": {
                        "value": 1,
                        "unit": form

                    }
                }
            }]
        }
    }
    active_ing = Ingredient(**data_in)
   
    return active_ing

def create_ingredients_from_string(active_ingredients_string):
    parsed_entries = split_name_strength_form(active_ingredients_string)
    ingredients = []
    for name, strength, form in parsed_entries:
        ingredients.append(map_to_active_ingredient(name, strength, form))
    return ingredients
        
        
def split_name_strength_form(input_string):
    # Define the regular expression pattern
    pattern = re.compile(r'(?P<name>[^,]+),\s*(?P<strength>\d+\s*\w+),\s*(?P<form>[^;]+)')
    
    # Split the input string by semicolons to handle multiple entries
    entries = input_string.split(';')
    
    results = []
    for entry in entries:
        entry = entry.strip()  # Remove leading and trailing whitespace
        match = pattern.match(entry)
        if match:
            name = match.group('name').strip()
            strength = match.group('strength').strip()
            form = match.group('form').strip()
            results.append((name, strength, form))
        else:
            raise ValueError(f"Entry '{entry}' does not match the expected format")
    
    return results

