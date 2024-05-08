Profile: MedicationKnowledge_Leaflet
Parent: MedicationKnowledge
Id: medicationKnowledge-leaflet
Title: "Leaflet MediactionKnowledge"
Description: "Custom MedicationKnowledge Profile used to describe infos from medication leaflet"

* identifier 1..1
* identifier.value ^short = "Admission number on medication package"

* indicationGuideline 1..* 
* indicationGuideline.indication 1..*
* indicationGuideline.indication.concept.text ^short = "The different indications described in the leaflet"


* indicationGuideline.dosingGuideline ^slicing.discriminator.type = #pattern
* indicationGuideline.dosingGuideline ^slicing.discriminator.path = "dosage.type.text"
* indicationGuideline.dosingGuideline ^slicing.rules = #open

* indicationGuideline.dosingGuideline contains forgottenIntakeDosing 1..1
* indicationGuideline.dosingGuideline contains excessiveIntakeDosing 1..1
* indicationGuideline.dosingGuideline contains ifDiscontinued 0..1
* indicationGuideline.dosingGuideline contains generalDosing 1..1

* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.text ^short = "The Header, e.g. 'Measures to be taken if the administration of one or more doses has been omitted'"
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet if administration has been omitted"

* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.text ^short = "The Header, e.g. 'Instruction in case of an overdose'"
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet in case of overdose."

* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.text ^short = "The Header, e.g. 'If you discontinue administration'"
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet if medication is discontinued."

* indicationGuideline.dosingGuideline[generalDosing].dosage.type.text ^short = "The Header e.g. 'Dosing instructions for adults'"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.patientInstruction = "Instructions described in leaflet for administration in general"


* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction 0..* // Allowing multiple additional instructions
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction from http://snomed.info/sct (required) // Use coding if specific codes are applicable
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction.text ^short = "instructions described in leaflet and reffered in code system"

// Define timing structure, but allow for flexibility in its content
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing ^short = "To describe the maximum intake duration in days"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing.repeat 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing.repeat.frequency 0..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing.repeat.period 0..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing.repeat.periodUnit = #d
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.timing.repeat.boundsRange 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route from http://hl7.org/fhir/ValueSet/route-codes (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route.text ^short = "Description of route found on leaflet and referred in code"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.type.text 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.type.text ^short = "Header for type of dose e.g. 'Standard dosage'"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.system from http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm (required) 
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.code 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.system from http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.code 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.system from http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.code 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.system from http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.code 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.unit 1..1

* storageGuideline 1..*
* storageGuideline.note.text 1..1
* storageGuideline.environmentalSetting 0..1
* storageGuideline.environmentalSetting.type.coding from http://unitsofmeasure.org (required)
* storageGuideline.environmentalSetting.type 1..1

* storageGuideline.environmentalSetting.valueRange.high.value 0..1

* definitional.definition ^slicing.discriminator.type = #pattern
* definitional.definition ^slicing.discriminator.path = "definition"
* definitional.definition ^slicing.rules = #open

* definitional.definition contains mpd 1..1
* definitional.definition[mpd] only Reference (MedicinalProductDefinition)

* definitional.doseForm.coding from http://snomed.info/sct (required)
* definitional.doseForm.coding 1..1
* definitional.doseForm.text ^short = "Description of doseform found in leaflet and referrenced in coding"

* definitional.drugCharacteristic 0..* 
* definitional.drugCharacteristic.type.coding from http://terminology.hl7.org/CodeSystem/medicationknowledge-characteristic (required) 
* definitional.drugCharacteristic.type.coding 0..1 
* definitional.drugCharacteristic.valueString 1..1
* definitional.drugCharacteristic.valueString ^short = "Description of characteristic found in leaflet and referrenced in coding"


