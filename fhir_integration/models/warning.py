import re
from fhir.resources.clinicalusedefinition import ClinicalUseDefinition


def map_to_warning(warning):
    data_in = {
        "resourceType" : "ClinicalUseDefinition",
        "meta" : {
            "profile": ["http://localhost:8080/fhir/StructureDefinition/warning"]
        },
        "text" : {
            "status" : "generated",
            "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n\n<p>Warning</p>\n\n</div>"
        },
        "type" : "warning",
            "warning" : {
                "description" : warning
            }
    }
    warning = ClinicalUseDefinition(**data_in)
    return warning


# def split_warnings(warning_string):
#     entries = warning_string.split('|')
#     warning_list = []
#     for entry in entries:
#         entry = entry.strip()
#         warning_list.append(entry)
#     return warning_list



##TODO 
# warning als resource schreiben und schon fix in die DB speichern weil das bei jeder quasi dabei sein muss.