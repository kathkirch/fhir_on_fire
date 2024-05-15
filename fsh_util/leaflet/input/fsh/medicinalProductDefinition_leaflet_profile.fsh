Alias: ingredient-role = http://hl7.org/fhir/ingredient-role

Profile: MPD_Profile
Parent: MedicinalProductDefinition
Id: mpdProfile
Title: "Leaflet MedicinalProductDefinition"
Description: "Custom MedicinalProductDefinition profile for displaying information in the medication package leaflet, including name, name parts country and language, references to manufacturer and marketing authorization holder, ingredients and other required informations."

* identifier 1..1
* identifier.value ^short = "Use of the admission number of the medication is required for the identifier"

* name.productName 1..1
* name.productName ^short = "the full product name, which is also presented on the package."

* name.part ^slicing.discriminator.type = #pattern
* name.part ^slicing.discriminator.path = "type"
* name.part ^slicing.rules = #open

* name.part contains doseFormPart 1..1
* name.part contains strengthPart 1..1
* name.part contains populationPart 0..1

* name.part[doseFormPart].part 1..1
* name.part[doseFormPart].part ^short = "doseFormPart of medication name"
* name.part[doseFormPart].type from http://hl7.org/fhir/ValueSet/medicinal-product-name-part-type (required)
* name.part[doseFormPart].type.coding.code  1..1
* name.part[doseFormPart].type.coding.code = #DoseFormPart

* name.part[strengthPart].part 1..1
* name.part[strengthPart].part ^short = "strength part of medication name"
* name.part[strengthPart].type from http://hl7.org/fhir/ValueSet/medicinal-product-name-part-type (required)
* name.part[strengthPart].type.coding.code  1..1
* name.part[strengthPart].type.coding.code = #StrengthPart

* name.part[populationPart].part 1..1
* name.part[populationPart].part ^short = "population part of medication name"
* name.part[populationPart].type from http://hl7.org/fhir/ValueSet/medicinal-product-name-part-type (required)
* name.part[populationPart].type.coding.code 1..1
* name.part[populationPart].type.coding.code = #PopulationPart

* name.usage.country ^short = "The country in which the medicine was marketed under this name"
* name.usage.country = urn:iso:std:iso:3166#AT "Austria"
* name.usage.jurisdiction = urn:iso:std:iso:3166#AT
* name.usage.language = urn:ietf:bcp:47#de

* contact ^slicing.discriminator.type = #pattern
* contact ^slicing.discriminator.path = "type"
* contact ^slicing.rules = #open
* contact contains manufacturer 1..1
* contact contains authorizationHolder 1..1
* contact[manufacturer].contact only Reference(Organization)
* contact[authorizationHolder].contact only Reference(Organization)

* description 1..1 
* description ^short = "The mode of action described in leaflet" 

* indication 1..1
* indication ^short = "The indication described in leaflet" 

* contained ^short = "Contained resources to ingredients"

* contained ^slicing.discriminator.type = #profile
* contained ^slicing.discriminator.path = "ingredient"
* contained ^slicing.rules = #open

* contained contains ActiveIngredient 1..1
* contained contains AdjuvantIngredient 0..*


* contained[ActiveIngredient] only active-ingredient
* contained[AdjuvantIngredient] only adjuvant-ingredient

* statusDate 1..1
* statusDate ^short = "Date when leaflet was created"
* additionalMonitoringIndicator ^short =  "Info for black triangle warning if existing"

