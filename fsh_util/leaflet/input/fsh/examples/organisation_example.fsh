Instance: MedicinalOrganization
InstanceOf: Organization
Description: "Example for an organization resource used to describe the marketing authorization holder of a medication. Uses the minimum of required information reffered in the paragraph 16 AMG."
Usage: #example
* identifier.value = "basg"
* meta.profile = "http://localhost.org/StructureDefinition/medicinal-organization"
* name = "Bundesamt für Sicherheit im Gesundheitswesen"
* contact.telecom[0].system = #fax
* contact.telecom[=].value = "+ 43 (0) 50 555 36207"
* contact.telecom[+].system = #url
* contact.telecom[=].value = "https://www.basg.gv.at/"
* contact.address.text = "Traisengasse 5, 1200 WIEN, ÖSTERREICH"
* contact.address.line = "Traisengasse 5"
* contact.address.city = "Wien"
* contact.address.postalCode = "1200"
* contact.address.country = "Austria"