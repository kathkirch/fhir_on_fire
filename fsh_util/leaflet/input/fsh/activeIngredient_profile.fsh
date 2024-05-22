Profile: ActiveIngredient
Parent: Ingredient
Id: active-ingredient
Title: "Active Ingredient"
Description: "Custom profile for an active Ingredient focusing on specific use to describe medication leaflet of medicinal product"

* identifier 1..1 MS
* identifier.value ^short = "Name of the active ingredient"
* identifier.value 1..1 MS

* for 1..1 MS
* for only Reference(MedicinalProductDefinition)

* role 1..1
* role only CodeableConcept

* role.coding.system = "http://hl7.org/fhir/ingredient-role"
* role.coding.system 1..1
* role.coding.code = #100000072072
* role.coding.code 1..1
* role.coding.display = "active"
* role.coding.display 1..1

* substance 1..1

* substance.code only CodeableReference 
* substance.code from ActiveSubstanceValueSet
* substance.code.concept.text 1..1
* substance.code.concept.text ^short = "Ingredient name"
* substance.code.concept.coding.system = "http://snomed.info/sct"

* substance.strength 1..*
* substance.strength.presentationRatio only Ratio
* substance.strength.presentationRatio.numerator 1..1
* substance.strength.presentationRatio.numerator only Quantity
* substance.strength.presentationRatio.numerator.system = "http://unitsofmeasure.org"
// * substance.strength.presentationRatio.numerator.system 0..1
// * substance.strength.presentationRatio.numerator.code 0..1
* substance.strength.presentationRatio.numerator.unit 1..1
* substance.strength.presentationRatio.numerator.value 1..1

* substance.strength.presentationRatio.denominator 1..1
* substance.strength.presentationRatio.denominator only SimpleQuantity
* substance.strength.presentationRatio.denominator.system = "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
* substance.strength.presentationRatio.denominator.value 1..1
* substance.strength.presentationRatio.denominator.unit 1..1
// * substance.strength.presentationRatio.denominator.code 1..1

