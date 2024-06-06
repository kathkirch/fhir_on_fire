ValueSet: ActiveSubstanceValueSet
Id: active-substance-value-set
Title: "Active Substance ValueSet"
Description: "A value set for active substances in medicinal products."
* ^experimental = true
* include codes from system http://snomed.info/sct where concept is-a #105590001 // Use the actual SNOMED CT hierarchy appropriate for active substances


ValueSet: AdditionalInstruction
Id: addition-instructions-value-set
Title: "Additional Instruction Value Set"
Description: "A value set for additional instructions how to take the medication"
* ^experimental = true
* include codes from system http://hl7.org/fhir/ValueSet/additional-instruction-codes 

ValueSet: OrderableDrugForm
Id: orderableDrugForm
Title: "Orderable drugform ValueSet"
Description: "A value set for orderable drugfrom of medicinal products"
* ^experimental = true
* include codes from system http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm


ValueSet: UnitsOfMeasure
Id: 156
Title: "Units of measure ValueSet"
Description: "A value set for units of measure to describe dosing and units"
* ^experimental = true
* include codes from system http://unitsofmeasure.org

ValueSet: DoseForm
Id: dose-form
Title: "Doseform ValueSet"
Description: "A value set for dose forms"
* ^experimental = true
* include codes from system http://snomed.info/sct where concept is-a #736542009

// ValueSet: DrugCharacteristic
// Id: drug-characteristic
// Title: "Drug characteristic ValueSet"
// Description: "A value set to define drug characteristic"
// * ^experimental = true
// * include codes from system http://terminology.hl7.org/CodeSystem/medicationknowledge-characteristic

ValueSet: BlackTriangleMonitoring
Id: 157
Title: "Black Triangle ValueSet"
Description: "Code System for black triangle monitoring information"
* ^experimental = true
* include codes from system http://hl7.org/fhir/medicinal-product-additional-monitoring


ValueSet: DosingInstructionCodes
Id: 206
Title: "Instruction Codes for Medication Intake"
Description: "A set of SNOMED CT codes describing various scenarios related to the administration of medication."
* ^experimental = true
* http://snomed.info/sct#223422006 "Recommendation regarding what to do if drug omitted"
* http://snomed.info/sct#260378005 "Excessive"
* http://snomed.info/sct#410546004 "Discontinued"
* http://snomed.info/sct#422096002 "Dosing instruction fragment"
* http://snomed.info/sct#261773006 "Duration of therapy"