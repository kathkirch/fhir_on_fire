from transformers import pipeline
from fhir.resources.medicinalproductdefinition import MedicinalProductDefinition 
from fhir.resources.organization import Organization

#things needed to create mpd_resource, including organization and ingredient resources

info_organization = {
    "shortNameAsID" : 
    "orgName": 
    "address_street_number":
    "address_city": 
    "address_zip":
    "address_country":
    "webAdress":
    "fax": 
}


## now the manufacturer needs to be validated
## if valid --> send manufacturer to server/db
## get manufacturerID

info_mpd = {
    "admission_nr": 
    "fullName":
    "nameDoseFormPart":
    "nameStrengthPart":
    "namePopulationPart":
    "modeOfAction":
    "indication":
    "creationDate":
    "blackTriangle": 
    # attributes to create proper mpd
    "countActiveIngredients": 
    "countAdjuvantIngredients":
    "ensureBasg":
}

info_active_ingredients = {
    "substance_name_active": 
    "strength": 
    "strength_unit": 
    "strength_value": 
    "strength_denominator": 
}

info_adjucant_ingredients = {
    "substance_name_adjucant":
}




    


