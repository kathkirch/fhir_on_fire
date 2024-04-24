Profile: ActiveIngredient
Parent: Ingredient
Id: active-ingredient
Title: "Active Ingredient"
Description: "Custom profile for an active Ingredient focusing on specific use to describe medication leaflet of medicinal product"

* identifier 1..1
* identifier.value = "Name of the ingredient"

* for 1..1
* for only Reference(MedicinalProductDefinition)

* role 1..1
* role.coding ^slicing.discriminator.type = #pattern
* role.coding ^slicing.discriminator.path = "code"
* role.coding ^slicing.rules = #open

* role.coding contains activeRole 1..1
* role.coding[activeRole].system = "http://hl7.org/fhir/ingredient-role"
* role.coding[activeRole].code = #100000072072
* role.coding[activeRole].display = "active"

* substance.code from ActiveSubstanceValueSet (required)

* substance.strength 1..*
* substance.strength.presentationRatio.numerator 1..1
* substance.strength.presentationRatio.numerator.system = "http://unitsofmeasure.org"

* substance.strength.presentationRatio.denominator 1..1
* substance.strength.presentationRatio.denominator.system = "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
