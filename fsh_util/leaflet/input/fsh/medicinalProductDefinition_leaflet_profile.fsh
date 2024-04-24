Alias: ingredient-role = http://hl7.org/fhir/ingredient-role

Profile: MPD_Profile
Parent: MedicinalProductDefinition
Id: mpdProfile
Title: "Profile Leaflet Information"
Description: "Profile used to create IG to display leaflet information"

* identifier 1..1
* identifier.value ^short = "Use of the admission number of the medication is required for the identifier"

* name.productName 1..1
* name.productName ^short = "the complete product name, which is also presented on the package."
* name.part ^slicing.discriminator.type = #pattern
* name.part ^slicing.discriminator.path = "type"
* name.part ^slicing.rules = #open
* name.part.type from http://hl7.org/fhir/ValueSet/medicinal-product-name-part-type (required)
* name.part contains doseFormPart 1..1
* name.part contains strengthPart 1..1
* name.part contains populationPart 0..1
* name.part[doseFormPart].type.coding.code = #DoseFormPart
* name.part[strengthPart].type.coding.code = #StrengthPart
* name.part[populationPart].type.coding.code = #PopulationPart

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

* ingredient ^slicing.discriminator.type = #pattern
* ingredient ^slicing.discriminator.path = "role"
* ingredient ^slicing.rules = #open
* ingredient contains ActiveIngredient 1..* and AdjuvantIngredient 0..*

* statusDate ^short = "Date when leaflet was created"
* additionalMonitoringIndicator ^short =  "Info for black triangle warning if existing"

