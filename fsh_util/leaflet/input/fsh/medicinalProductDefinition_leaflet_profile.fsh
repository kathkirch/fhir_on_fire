Alias: ingredient-role = http://hl7.org/fhir/ingredient-role

Profile: MPDProfile
Parent: MedicinalProductDefinition
Id: mpdProfile
Title: "Leaflet MedicinalProductDefinition"
Description: "Custom MedicinalProductDefinition profile for displaying information in the medication package leaflet, including name, name parts country and language, references to manufacturer and marketing authorization holder, ingredients and other required informations."

* identifier 1..1
* identifier.value ^short = "Use of the admission number of the medication is required for the identifier"
* identifier.value 1..1 MS

* name.productName 1..1 MS
* name.productName ^short = "the full product name, which is also presented on the package."

* name.part ^slicing.discriminator.type = #value
* name.part ^slicing.discriminator.path = "type.coding.code"
* name.part ^slicing.rules = #closed
* name.part ^slicing.description = "The different name parts are differentiated by code, content is captured by name.part.part element"

* name.part contains doseFormPart 1..1 MS
* name.part contains strengthPart 1..1 MS 
* name.part contains populationPart 0..1 MS

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

* contact ^slicing.discriminator.type = #value
* contact ^slicing.discriminator.path = "type.text"
* contact ^slicing.rules = #open
* contact ^slicing.description = "There must be a reference to organization resouce which holds contact information for maufacturer and one to marketing authorization holder"
* contact contains manufacturer 1..1 MS
* contact contains authorizationHolder 1..1 MS
* contact[manufacturer].type.text = "Hersteller"
* contact[authorizationHolder].type.text = "Zulasser"
* contact[manufacturer].contact only Reference(Organization)
* contact[authorizationHolder].contact only Reference(Organization)

* description 1..1 MS
* description ^short = "The mode of action described in leaflet" 

* indication 1..1 MS
* indication ^short = "The indication described in leaflet" 

* contained ^short = "Contained resources to ingredients"
* contained only Ingredient

* contained ^slicing.discriminator.type = #value
* contained ^slicing.discriminator.path = "meta.profile"
* contained ^slicing.rules = #open
* contained ^slicing.description = "In the contained there must be at least one ActiveIngredient-Resource Profile and 0..* AdjuvantIngredient"

* contained contains ActiveIngredient 1..* MS and AdjuvantIngredient 0..* 

* contained[ActiveIngredient] only ActiveIngredient
* contained[AdjuvantIngredient] only AdjuvantIngredient

* contained[ActiveIngredient].meta.profile = "http://localhost:8080/fhir/StructureDefinition/active-ingredient"
* contained[AdjuvantIngredient].meta.profile = "http://localhost:8080/fhir/StructureDefinition/adjuvant-ingredient"

* statusDate 1..1 MS
* statusDate ^short = "Date when leaflet was created"

* additionalMonitoringIndicator 0..1
* additionalMonitoringIndicator ^short = "Info for black triangle monitoring if existing in leaflet"
* additionalMonitoringIndicator only CodeableConcept 
* additionalMonitoringIndicator.coding 1..1 
* additionalMonitoringIndicator.coding.system = "http://hl7.org/fhir/medicinal-product-additional-monitoring" 
* additionalMonitoringIndicator.coding.code = #BlackTriangleMonitoring
* additionalMonitoringIndicator.text 1..1
* additionalMonitoringIndicator.text ^short =  "Info for black triangle warning if existing"

