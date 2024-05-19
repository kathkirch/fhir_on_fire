Profile: MedicinalOrganization
Parent: Organization
Id: medicinal-organization
Title: "Medicinal Organization"
Description: "A custom profile for Organization-Resources that is used to display information in the package insert for either the drug manufacturer or the marketing authorization holder"

* identifier 1..1 MS
* identifier.value ^short = "Identifier for the organisation, based on short name of organisation"
* identifier.value 1..1 MS 

* name ^short = "Name of organisation, the whole name of organization is required"
* name 1..1 MS

* contact ^slicing.discriminator.type = #pattern
* contact ^slicing.discriminator.path = "telecom.system"
* contact ^slicing.rules = #open

* contact contains Fax 0..1 
* contact[Fax].telecom 0..1
* contact[Fax].telecom.system = #fax

* contact contains Website 0..1
* contact[Website].telecom 0..1
* contact[Website].telecom.system = #url

* contact ^short = "The whole address must be present"
* contact contains Address 1..1 MS
* contact[Address].address.text 1..1
* contact[Address].address.line 1..1 
* contact[Address].address.city 1..1 
* contact[Address].address.postalCode 1..1 
* contact[Address].address.country 1..1 

