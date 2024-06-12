import re
from fhir.resources.clinicalusedefinition import ClinicalUseDefinition

def map_to_sideEffect(effect, frequency):
    data_in = {
        "resourceType" : "ClinicalUseDefinition",
        "text" : {
            "status" : "generated",
            "div" : f"<div xmlns=\"http://www.w3.org/1999/xhtml\">\n\n<p>SideEffect: {effect}</p>\n\n</div>"
        },
        "meta" : {
            "profile": ["http://localhost:8080/fhir/StructureDefinition/undesirable-effect"]
        },
        "type" : "undesirable-effect",
        "undesirableEffect" : {
            "symptomConditionEffect": {
                "concept": {
                    "text": effect
                }
            },
            "frequencyOfOccurrence": {  
                "text": frequency
            }
        }
    }
    side_effect = ClinicalUseDefinition(**data_in)
    return side_effect


def spilt_side_effects_by_frequency(input_string):
    # Trennen des Strings an Semikolons, gefolgt von einem Großbuchstaben und einem Leerzeichen
    categories = input_string.split(';')
    
    result_cud = []
    for i, category in enumerate(categories):
        categories[i] = category.strip() # remove leading whitespace
        
        pair = parse_side_effects(category)
        if isinstance(pair, str):
            continue
        # print(i)
        # print(pair)
        result_cud = result_cud + pair

    return result_cud

def parse_side_effects(input_string):
    # Trennen der Eingabe am ersten Doppelpunkt
    parts = input_string.split(':', 1)
    # print(f"parts = {parts}")
    if len(parts) < 2:
        return "Fehler: Der Input-String ist nicht korrekt formatiert."

    # Teil vor dem Doppelpunkt als Häufigkeit
    frequency = parts[0].strip()
    
    # Teil nach dem Doppelpunkt als Liste von Nebenwirkungen, getrennt durch Kommas
    side_effects = parts[1].split('|')
    for i, effect in enumerate(side_effects):
        side_effects[i] = effect.strip()

    # Erstellen einer Liste von Dictionaries
    results = []
    for effect in side_effects:
        effect_dict = {'frequency': frequency, 'side_effect': effect}
        results.append(effect_dict)
    return results


