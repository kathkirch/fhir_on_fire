import json
from fhir.resources.ingredient import Ingredient


def map_to_activeIngredient():
    activeIngredient = Ingredient(
        meta = {"profile": ["http://localhost.org/StructureDefinition/mpdProfile"]}
    )





# Funktion zum Erstellen der FHIR-JSON-Struktur
def create_substance(name, strength, form):
    return {
        "substance": {
            "code": {
                "concept": {
                    "coding": [{
                        "system": "http://snomed.info/sct",
                        "code": "__",
                        "display": name
                    }]
                }
            },
            "strength": [{
                "presentationRatio": {
                    "numerator": {
                        "value": strength,
                        "unit": "__",
                        "system": "http://unitsofmeasure.org",
                        "code": "__"
                    },
                    "denominator": {
                        "value": 1,
                        "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
                        "code": getCode(form)
                    }
                }
            }]
        }
    }

# Eingabedaten verarbeiten
def split_name_strength_active(name_strength_active: dict):
    output = []
    items = name_strength_active["name_strength_active"].split('; ')
    for item in items:
        parts = item.split(', ')
        name = parts[0]
        strength = int(parts[1].split()[0])
        form = parts[2]
        fhir_structure = create_fhir_structure(name, strength, form)
        output.append(fhir_structure)
    return output

# Ausgabe der FHIR-JSON-Struktur
fhir_output = split_name_strength_active(input_data)
print(json.dumps(fhir_output, indent=4))
