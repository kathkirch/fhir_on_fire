Profile: Warning
Parent: ClinicalUseDefinition
Id: warning
Title: "Warning"
Description: "A custom profile for the ClinicalUseDefinition-Resource that is used to display a warning regarding a medication contained in the medication leaflet"

* identifier 1..1 
* identifier.value ^short = "warning as buzzword"
* identifier.value 1..1 MS


* type = #warning

* warning 1..1 MS
* warning.description ^short = "The long description, the long text of the warning"
* warning.description 1..1 MS
