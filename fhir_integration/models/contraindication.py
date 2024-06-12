import re
from fhir.resources.clinicalusedefinition import ClinicalUseDefinition


def map_to_contraindication(extracted_contraindication_info): 
    data_in = {
        "resourceType" : "ClinicalUseDefinition",
        "identifier": [{
            "value": "NameContraindication"
        }],
        "meta" : {
        "profile": ["http://localhost:8080/fhir/StructureDefinition/contraindication"]
        },
        "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      \n      <p>Contraindication</p>\n    \n    </div>"
        },
        "type" : "contraindication",
        "contraindication" : {
            "diseaseSymptomProcedure" : {
                "concept" : {
                "text" : extracted_contraindication_info.get("contraindication")
                }
            }
        }
    }

    contraindication = ClinicalUseDefinition(**data_in)
    return contraindication

