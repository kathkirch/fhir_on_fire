// Alias: $medicinal-product-name-part-type = http://hl7.org/fhir/medicinal-product-name-part-type
// Alias: $medicinal-product-additional-monitoring = http://hl7.org/fhir/medicinal-product-additional-monitoring
// Alias: $ingredient-role = http://hl7.org/fhir/ingredient-role
// Alias: $sct = http://snomed.info/sct

// Instance: MPDProfile
// InstanceOf: MedicinalProductDefinition
// Usage: #example
// * meta.profile = "http://localhost.org/StructureDefinition/mpdProfile"
// * identifier.value = "1-12345"
// * name.productName = "Paracetamol 500 mg Filmtabletten"
// * name.part[0].part = "Filmtabletten"
// * name.part[=].type = $medicinal-product-name-part-type#DoseFormPart "Pharmaceutical dose form part"
// * name.part[=].type.text = "Filmtabletten"
// * name.part[+].part = "500mg"
// * name.part[=].type = $medicinal-product-name-part-type#StrengthPart "Strength part"
// * name.part[=].type.text = "500mg"
// * name.part[+].part = "Population"
// * name.part[=].type = $medicinal-product-name-part-type#PopulationPart "Target population part"
// * name.part[=].type.text = "Population"
// * name.usage.country = urn:iso:std:iso:3166#AT "Austria"
// * name.usage.jurisdiction = urn:iso:std:iso:3166#AT
// * name.usage.language = urn:ietf:bcp:47#de
// * contact[0].type.text = "Hersteller"
// * contact[=].contact = Reference(Organization/56)
// * contact[+].type.text = "Zulasser"
// * contact[=].contact = Reference(Organization/102)
// * description = "Paracetamol (auch Acetaminophen, als Kontraktionen des chemischen Namens para-(Acetylamino)phenol) ist ein schmerzlindernder und fiebersenkender Arzneistoff aus der Gruppe der Nichtopioid-Analgetika"
// * indication = "Paracetamol Filmtabletten werden angewendet Schmerzen, ..."
// * contained[0] = ActiveIngredient
// * contained[+] = AdjuvantIngredient
// * statusDate = "2024-01-24"
// * additionalMonitoringIndicator = $medicinal-product-additional-monitoring#BlackTriangleMonitoring "Requirement for Black Triangle Monitoring"
// * additionalMonitoringIndicator.text = "Info for black triangle if existing"

// Instance: ActiveIngredient
// InstanceOf: Ingredient
// Usage: #inline
// * identifier.value = "Paracetamol"
// * status = #active
// * meta.profile = "http://localhost.org/StructureDefinition/active-ingredient"
// * for = Reference(MedicinalProductDefinition/123)
// * role = $ingredient-role#100000072072 "active"
// * substance.code.concept.text = "Paracetamol"
// * substance.code.concept = $sct#387517004 "Paracetamol"
// * substance.strength.presentationRatio.numerator.value = 500
// * substance.strength.presentationRatio.numerator.unit = "mg"
// * substance.strength.presentationRatio.denominator.value = 1
// * substance.strength.presentationRatio.denominator.unit = "Tablette"

// Instance: AdjuvantIngredient
// InstanceOf: Ingredient
// Usage: #inline
// * identifier.value = "Maisstaerke"
// * meta.profile = "http://localhost.org/StructureDefinition/adjuvant-ingredient"
// * status = #active
// * for = Reference(MedicinalProductDefinition/123)
// * role = $ingredient-role#100000072073 "adjuvant"
// * substance.code.concept.text = "Maisstärke"

