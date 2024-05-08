Profile: Warning
Parent: ClinicalUseDefinition
Id: warning
Title: "Warning"
Description: "A custom profile for Clinical Use Definition resources that describe a warning."

* identifier 1..1
* identifier.value ^short = "Short name for the interaction to use as warning"

* type = #warning

* warning 1..1
* warning.description ^short = "Description for the interaction"
* warning.description 1..1
