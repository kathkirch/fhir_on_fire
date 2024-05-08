Profile: AdjuvantIngredient
Parent: Ingredient
Id: adjuvant-ingredient
Title: "Adjuvant Ingredient"
Description: "Custom profile for an adjuvant Ingredient focusing on specific use to describe medication leaflet of medicinal product"

* identifier 1..1
* identifier.value ^short = "Name of the adjuvant ingredient"

* for 1..1
* for only Reference(MedicinalProductDefinition)

* role 1..1
* role only CodeableConcept
* role.coding ^slicing.discriminator.type = #pattern
* role.coding ^slicing.discriminator.path = "code"
* role.coding ^slicing.rules = #open

* role.coding contains activeRole 1..1
* role.coding[activeRole].system = "http://hl7.org/fhir/ingredient-role"
* role.coding[activeRole].system 1..1
* role.coding[activeRole].code = #100000072073
* role.coding[activeRole].code 1..1
* role.coding[activeRole].display = "adjuvant"
* role.coding[activeRole].display 1..1

* substance.code 1..1
* substance.code only CodeableReference
* substance.code.concept.text 1..1 
* substance.code.concept.text ^short = "Name of the substance/ingredient"
