ValueSet: Medicinal-Product-Name-Part-Type
Id: medicinal-product-name-part-type
Title: "Product Name Part Type"
Description: "Value set for product name part types"
* include codes from system http://hl7.org/fhir/medicinal-product-name-part-type

ValueSet: ActiveSubstanceValueSet
Id: active-substance-value-set
Title: "Active Substance Value Set"
Description: "A value set for active substances in medicinal products."
* include codes from system http://snomed.info/sct where concept is-a #105590001 // Use the actual SNOMED CT hierarchy appropriate for active substances
