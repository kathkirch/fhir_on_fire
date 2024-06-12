import re
from fhir.resources.clinicalusedefinition import ClinicalUseDefinition


def map_to_warning():
    data_in = {
        "resourceType" : "ClinicalUseDefinition",
        "meta" : {
            "profile": ["http://localhost:8080/fhir/StructureDefinition//warning"]
        },
        "text" : {
            "status" : "generated",
            "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      \n      <p>Warning</p>\n    \n    </div>"
        },
        "type" : "warning",
        "warning" : {
            "description" : "Placeholder Description of Warning"
        }
    }
    warning = ClinicalUseDefinition(**data_in)
    return warning


##TODO 
# warning als resource schreiben und schon fix in die DB speichern weil das bei jeder quasi dabei sein muss.