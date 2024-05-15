ValueSet: ActiveSubstanceValueSet
Id: active-substance-value-set
Title: "Active Substance ValueSet"
Description: "A value set for active substances in medicinal products."
* include codes from system http://snomed.info/sct where concept is-a #105590001 // Use the actual SNOMED CT hierarchy appropriate for active substances


ValueSet: AdditionalInstruction
Id: addition-instructions-value-set
Title: "Additional Instruction Value Set"
Description: "A value set for additional instructions how to take the medication"
* include codes from system http://hl7.org/fhir/ValueSet/additional-instruction-codes 

ValueSet: OrderableDrugForm
Id: orderableDrugForm
Title: "Orderable drugform ValueSet"
Description: "A value set for orderable drugfrom of medicinal products"
* include codes from system http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm


ValueSet: UnitsOfMeasure
Id: units-of-measure
Title: "Units of measure ValueSet"
Description: "A value set for units of measure to describe dosing and units"
* include codes from system http://unitsofmeasure.org

ValueSet: DoseForm
Id: dose-form
Title: "Doseform ValueSet"
Description: "A value set for dose forms"
* include codes from system http://snomed.info/sct where concept is-a #736542009

ValueSet: DrugCharacteristic
Id: drug-characteristic
Title: "Drug characteristic ValueSet"
Description: "A value set to define drug characteristic"
* include codes from system http://terminology.hl7.org/CodeSystem/medicationknowledge-characteristic