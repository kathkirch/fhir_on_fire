Profile: MedicationKnowledge_Leaflet
Parent: MedicationKnowledge
Id: medicationKnowledge-leaflet
Title: "Leaflet MediactionKnowledge"
Description: "Custom MedicationKnowledge Profile used to describe infos from medication leaflet"

* identifier 1..1
* identifier.value ^short = "Admission number on medication package"

* indicationGuideline 1..* 
* indicationGuideline.indication 1..*
* indicationGuideline.indication.concept.text 1..1
* indicationGuideline.indication.concept.text ^short = "The different indications described in the leaflet for which the dosing applies"

* indicationGuideline.dosingGuideline ^slicing.discriminator.type = #pattern
* indicationGuideline.dosingGuideline ^slicing.discriminator.path = "dosage.type.text"
* indicationGuideline.dosingGuideline ^slicing.rules = #open

* indicationGuideline.dosingGuideline contains forgottenIntakeDosing 1..1
* indicationGuideline.dosingGuideline contains excessiveIntakeDosing 1..1
* indicationGuideline.dosingGuideline contains ifDiscontinued 0..1
* indicationGuideline.dosingGuideline contains generalDosing 1..1
* indicationGuideline.dosingGuideline contains maxDuration 1..1

* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.text ^short = "The Header, e.g. 'Measures to be taken if the administration of one or more doses has been omitted'"
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet if administration has been omitted"

* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.text ^short = "The Header, e.g. 'Instruction in case of an overdose'"
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet in case of overdose."

* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.text ^short = "The Header, e.g. 'If you discontinue administration'"
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet if medication is discontinued."

* indicationGuideline.dosingGuideline[maxDuration].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.type.text ^short = "The header, e.g. 'max intake duration if not precribed other'"
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.patientInstruction ^short = "Instructions for maximum intake duration"

* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing ^short = "Timing event used to describe the maximum intake duration described in the medication leaflet"
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing.repeat 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing.repeat.boundsDuration 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.type.text ^short = "The Header e.g. 'Dosing instructions for adults'"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet for administration in general"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction 0..* 
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction from AdditionalInstruction (required) // Use coding if specific codes are applicable
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction ^short = "To describe instructions coded if applicable"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction.text ^short = "Buzzword as plain text also described in coded form"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route from http://hl7.org/fhir/ValueSet/route-codes (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route.text ^short = "Description of route found on leaflet and referred in code"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.type.text 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.type.text ^short = "Header for type of dose e.g. 'Standard dosage'"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.system from OrderableDrugForm (required) 
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.code 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.system from OrderableDrugForm (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.code 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.system from OrderableDrugForm (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.code 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.system from OrderableDrugForm (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.system 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.code 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.unit 1..1

* storageGuideline 1..*
* storageGuideline.note.text 1..1
* storageGuideline.note.text ^short = "Description of storage guideline in text"
* storageGuideline.environmentalSetting 0..1
* storageGuideline.environmentalSetting.type ^short = "Categorization of the setting e.g coding for celsius"
* storageGuideline.environmentalSetting.type.coding from UnitsOfMeasure (required)
* storageGuideline.environmentalSetting.type 1..1

* storageGuideline.environmentalSetting.valueRange ^short = "value range of the environmental setting"
* storageGuideline.environmentalSetting.valueRange.high.value 0..1

* definitional.definition ^slicing.discriminator.type = #pattern
* definitional.definition ^slicing.discriminator.path = "definition"
* definitional.definition ^slicing.rules = #open

* definitional.definition contains mpd 1..1
* definitional.definition[mpd] only Reference (MedicinalProductDefinition)

* definitional.doseForm.coding from DoseForm (required)
* definitional.doseForm.coding 1..1
* definitional.doseForm.text ^short = "Description of doseform found in leaflet and referrenced in coding"

* definitional.drugCharacteristic 0..* 
* definitional.drugCharacteristic.type.coding from DrugCharacteristic (required) 
* definitional.drugCharacteristic.type.coding 0..1 
* definitional.drugCharacteristic.valueString 1..1
* definitional.drugCharacteristic.valueString ^short = "Description of characteristic found in leaflet and referrenced in coding"

* clinicalUseIssue ^short = "Reference to the ClinicalUseDefinition to describe every side effect, interaction, contraindication, warning"

* clinicalUseIssue ^slicing.discriminator.type = #profile
* clinicalUseIssue ^slicing.discriminator.path = "reference"
* clinicalUseIssue ^slicing.rules = #open

* clinicalUseIssue contains SideEffect 1..*
* clinicalUseIssue contains Interaction 1..*
* clinicalUseIssue contains Contraindication 1..*
* clinicalUseIssue contains Warning 1..*

* clinicalUseIssue[SideEffect] only Reference(undesirable-effect)
* clinicalUseIssue[Interaction] only Reference(interaction)
* clinicalUseIssue[Contraindication] only Reference(contraindication)
* clinicalUseIssue[Warning] only Reference(warning)


