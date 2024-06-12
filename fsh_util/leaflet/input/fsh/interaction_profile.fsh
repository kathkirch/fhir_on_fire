Profile: Interaction
Parent: ClinicalUseDefinition
Id: interaction
Title: "Interaction"
Description: "A custom profile for Clinical Use Definition resources that describe interactions."

// * identifier 1..1 MS
// * identifier.value ^short = "Short name for the interaction to use as identifier"
// * identifier.value 1..1 MS

* type = #interaction

* interaction 1..1 MS
* interaction.type 1..1
* interaction.type.text ^short = "Description for the type of interaction, e.g. drug to drug, alcohol, etc."
* interaction.type.text 1..1

* interaction.effect 1..1
* interaction.effect.concept only CodeableConcept
* interaction.effect.concept.text 1..1
* interaction.effect.concept.text ^short = "Description of the interaction inclusive instructions when to talk to physician"



