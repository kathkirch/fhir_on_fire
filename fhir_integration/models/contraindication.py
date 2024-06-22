from fhir.resources.clinicalusedefinition import ClinicalUseDefinition

def map_to_contraindication(contraindication): 
    data_in = {
        "resourceType" : "ClinicalUseDefinition",
        "meta" : {
            "profile": ["http://localhost:8080/fhir/StructureDefinition/contraindication"]
        },
        "text" : {
            "status" : "generated",
            "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n \n <p>Contraindications</p>\n    \n    </div>"
        },
        "type" : "contraindication",
        "contraindication" : {
            "diseaseSymptomProcedure" : {
                "concept" : {
                "text" : contraindication
                }
            }
        }
    }

    contraindication = ClinicalUseDefinition(**data_in)
    return contraindication


def split_contraindications(contrindications_string): 
    entries = contrindications_string.split('|')
    contraindication_list = []
    for entry in entries:
        entry = entry.strip()
        contraindication_list.append(entry)
    return contraindication_list

    


