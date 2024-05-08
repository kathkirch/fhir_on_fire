Profile: Contraindication
Parent: ClinicalUseDefinition
Id: Contraindication
Title: "Contraindication"
Description: "Custom Profile used in IG to display leaflet information in fhir"


* identifier 1..1
* identifier.value ^short = "a short name to describe contraindication"

* type = #contraindication

* contraindication 1..1
* contraindication.diseaseSymptomProcedure 1..1
* contraindication.diseaseSymptomProcedure only CodeableReference
* contraindication.diseaseSymptomProcedure.concept.text ^short = "Description of Contraindication"
* contraindication.diseaseSymptomProcedure.concept.text 1..1