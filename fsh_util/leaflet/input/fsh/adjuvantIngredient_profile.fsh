Profile: AdjuvantIngredient
Parent: Ingredient
Id: adjuvant-ingredient
Title: "Adjuvant Ingredient"
Description: "Custom profile for an adjuvant Ingredient focusing on specific use to describe medication leaflet of medicinal product"

* identifier 1..1 MS
* identifier.value ^short = "Name of the adjuvant ingredient"
* identifier.value MS

* for 1..1 MS
* for only Reference(MedicinalProductDefinition)

* role 1..1
* role only CodeableConcept

* role.coding.system = "http://hl7.org/fhir/ingredient-role"
* role.coding.system 1..1
* role.coding.code = #100000072073
* role.coding.code 1..1
* role.coding.display = "adjuvant"
* role.coding.display 1..1

* substance 1..1
* substance.code 1..1
* substance.code only CodeableReference
* substance.code.concept.text 1..1 
* substance.code.concept.text ^short = "Name of the substance/ingredient"
