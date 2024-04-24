Profile: UndesirableEffect
Parent: ClinicalUseDefinition
Id: undesirable-effect
Title: "Custom Clinical Use Definition for Undesirable Effects"
Description: "A custom profile for Clinical Use Definition resources tailored to describe undesirable effects."

* identifier 1..1
* identifier.value ^short = "Short name to for the effect to use as identifier"

* type = #undesirable-effect

* undesirableEffect.symptomConditionEffect.concept.text 1..1
* undesirableEffect.symptomConditionEffect.concept.text ^short = "Description of Side Effect"

* undesirableEffect.frequencyOfOccurrence.coding from http://hl7.org/fhir/ValueSet/undesirable-effect-frequency (required)

