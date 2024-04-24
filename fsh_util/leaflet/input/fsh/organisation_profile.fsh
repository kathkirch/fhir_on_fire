Profile: MedicinalOrganization
Parent: Organization
Id: medicinal-organization
Title: "Medicianl Organization"
Description: "A custom profile for Organization resources tailored to describe leaflet information."

* identifier 1..1 // Assuming there can be multiple identifiers but at least one is required
* identifier.value ^short = "Identifier for the organisation, based on short name of organisation"
* name ^short = "Name of organisation "
* name 1..1 

* contact ^slicing.discriminator.type = #pattern
* contact ^slicing.discriminator.path = "telecom.system"
* contact ^slicing.rules = #open

* contact contains Fax 0..1 
* contact[Fax].telecom 0..1
* contact[Fax].telecom.system = #fax

* contact contains Website 0..1
* contact[Website].telecom 0..1
* contact[Website].telecom.system = #url

* contact contains Address 1..1
* contact[Address].address.text 1..1
* contact[Address].address.line 1..1 
* contact[Address].address.city 1..1 
* contact[Address].address.postalCode 1..1 
* contact[Address].address.country 1..1 

