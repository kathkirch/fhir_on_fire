Profile: UndesirableEffect
Parent: ClinicalUseDefinition
Id: undesirable-effect
Title: "Undesirable Effect"
Description: "A custom profile for ClinicalUseDefinition-Resources tailored to describe an undesirable effect"

* identifier 1..1
* identifier.value ^short = "Buzzword of the side effect"

* type = #undesirable-effect

* undesirableEffect.symptomConditionEffect only CodeableReference
* undesirableEffect.symptomConditionEffect.concept.text 1..1
* undesirableEffect.symptomConditionEffect.concept.text ^short = "The side effect as plain text"


* undesirableEffect.frequencyOfOccurrence 1..1 
* undesirableEffect.frequencyOfOccurrence only CodeableConcept
* undesirableEffect.frequencyOfOccurrence.coding from http://hl7.org/fhir/ValueSet/undesirable-effect-frequency (required)
* undesirableEffect.frequencyOfOccurrence.coding.system 1..1
* undesirableEffect.frequencyOfOccurrence.coding.code 1..1
* undesirableEffect.frequencyOfOccurrence.coding.display 1..1
