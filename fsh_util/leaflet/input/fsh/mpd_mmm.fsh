Alias: ingredient-role = "http://example.org/fhir/ValueSet/ingredient-role"

Profile: MPD_Profile
Parent: MedicinalProductDefinition
Id: mpdProfile
Title: "Profile Leaflet Information"
Description: "Profile used to create IG to display leaflet information"

* identifier 1..1
* identifier.value = "placeholder admission number"

* name.productName 1..1
* name.productName = "placeholder long name"

// * name.part ^slicing.discriminator.type = #pattern
// * name.part ^slicing.discriminator.path = "type"
// * name.part ^slicing.rules = #open

//* name.part[type = 'dosageForm'] 1..1 // Each name must have exactly one dosageForm
//* name.part only CodeableConcept
* name.part.type from Medicinal-Product-Name-Part-Type (required)

//* name.part[type = 'strength'] 1..1 // Each name must have exactly one strength
// * name.part[type = 'strength'].value[x] only CodeableConcept
// * name.part[type = 'strength'].valueCodeableConcept from Medicinal-Product-Name-Part-Type (required)

// //* name.part[type = 'Population'] 0..1 // Population part is optional
// * name.part[type = 'Population'].value[x] only CodeableConcept
// * name.part[type = 'Population'].valueCodeableConcept from PMedicinal-Product-Name-Part-Typet (required)

* name.usage.country = urn:iso:std:iso:3166#AT "Austria"
* name.usage.jurisdiction = urn:iso:std:iso:3166#AT
* name.usage.language = urn:ietf:bcp:47#de

* operation.organization ^slicing.discriminator.type = #pattern
* operation.organization ^slicing.discriminator.path = "type"
* operation.organization ^slicing.rules = #open

* operation.organization contains manufacturer 1..* and marketingAuthorizationHolder 1..*
* operation.organization[manufacturer].reference only Organization
* operation.organization[manufacturer].reference ^short = "Reference to the manufacturer's Organization."
* operation.organization[marketingAuthorizationHolder].reference only Organization
* operation.organization[marketingAuthorizationHolder].reference ^short = "Reference to the marketing authorization holder's Organization."

* description 1..1
* indication 1..1

* ingredient ^slicing.discriminator.type = #pattern
* ingredient ^slicing.discriminator.path = "role"
* ingredient ^slicing.rules = #open
* ingredient contains ActiveIngredient 1..1 and AdjuvantIngredient 0..* // At least one active ingredient, adjuvants are optional

* ingredient[ActiveIngredient].role = $ingredient-role#100000072072 // Code for "active" role
* ingredient[ActiveIngredient].substance 1..1 // Must contain exactly one substance reference
* ingredient[ActiveIngredient].substance.code from ActiveSubstanceValueSet (required)

* ingredient[AdjuvantIngredient].role = $ingredient-role#100000072073 // Code for "adjuvant" role
* ingredient[AdjuvantIngredient].substance 0..* // Adjuvant substances are optional

* statusDate ^short = "date leaflet created"
* additionalMonitoringIndicator ^short =  "Info for black triangle if existing"

