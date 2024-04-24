Profile: Warning
Parent: ClinicalUseDefinition
Id: warning
Title: "Clinical Use Definition for Warnings"
Description: "A custom profile for Clinical Use Definition resources that describe warnings."

* identifier 1..1
* identifier.value ^short = "Short name for the interaction to use as warning"

* type = #warning

* warning.description ^short = "Description for the interaction"
* warning.description 1..1
