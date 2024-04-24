Profile: Interaction
Parent: ClinicalUseDefinition
Id: interaction
Title: "Clinical Use Definition for Interactions"
Description: "A custom profile for Clinical Use Definition resources that describe interactions."

* identifier 1..1
* identifier.value ^short = "Short name for the interaction to use as identifier"

* type = #interaction

* interaction.type.text ^short = "Description for the interaction"
* interaction.type.text 1..1
