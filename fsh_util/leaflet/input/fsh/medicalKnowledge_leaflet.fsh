Profile: MedicationKnowledge_Leaflet
Parent: MedicationKnowledge
Id: medicationKnowledge-leaflet
Title: "Leaflet MediactionKnowledge"
Description: "Custom MedicationKnowledge Profile used to describe infos from medication leaflet"

* identifier 1..1
* identifier.value ^short = "Admission number on medication package"
* identifier.value 1..1 MS

* indicationGuideline 1..* MS
* indicationGuideline.indication 1..*
* indicationGuideline.indication.concept.text 1..1
* indicationGuideline.indication.concept.text ^short = "The various indications described in the package leaflet for which the dosage applies"

* indicationGuideline.dosingGuideline ^slicing.discriminator.type = #value
* indicationGuideline.dosingGuideline ^slicing.discriminator.path = "dosage.type.coding.code"
* indicationGuideline.dosingGuideline ^slicing.rules = #open

* indicationGuideline.dosingGuideline contains forgottenIntakeDosing 1..1 MS
* indicationGuideline.dosingGuideline contains excessiveIntakeDosing 1..1 MS
* indicationGuideline.dosingGuideline contains ifDiscontinued 0..1 MS
* indicationGuideline.dosingGuideline contains generalDosing 1..1 MS
* indicationGuideline.dosingGuideline contains maxDuration 1..1 MS

* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type only CodeableConcept 
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.coding 1..1 
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.coding from DosingInstructionCodes (required)
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.coding.code = #223422006
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.type.text ^short = "The Header, e.g. 'Measures to be taken if the administration of one or more doses has been omitted'"
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[forgottenIntakeDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet if administration has been omitted"

* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type only CodeableConcept
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.coding 1..1
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.coding from DosingInstructionCodes (required)
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.coding.code = #260378005
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.type.text ^short = "The Header, e.g. 'Instruction in case of an overdose'"
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[excessiveIntakeDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet in case of overdose."

* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type only CodeableConcept
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.coding 1..1
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.coding from DosingInstructionCodes (required)
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.coding.code = #410546004 
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.type.text ^short = "The Header, e.g. 'If you discontinue administration'"
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[ifDiscontinued].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet if medication is discontinued."

* indicationGuideline.dosingGuideline[maxDuration].dosage.type only CodeableConcept
* indicationGuideline.dosingGuideline[maxDuration].dosage.type.coding 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.type.coding from DosingInstructionCodes (required)
* indicationGuideline.dosingGuideline[maxDuration].dosage.type.coding.code = #261773006 
* indicationGuideline.dosingGuideline[maxDuration].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.type.text ^short = "The header, e.g. 'Maximum intake duration if not prescribed other'"
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.patientInstruction ^short = "Instructions for maximum intake duration"
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing ^short = "Timing event used to describe the maximum intake duration in units of time, e.g  days"
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing.repeat 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing.repeat.boundsDuration 1..1
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing.repeat.boundsDuration.unit 1..1 
* indicationGuideline.dosingGuideline[maxDuration].dosage.dosage.timing.repeat.boundsDuration.value 1..1


* indicationGuideline.dosingGuideline[generalDosing].dosage.type only CodeableConcept 
* indicationGuideline.dosingGuideline[generalDosing].dosage.type.coding 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.type.coding from DosingInstructionCodes (required)
* indicationGuideline.dosingGuideline[generalDosing].dosage.type.coding.code = #422096002 
* indicationGuideline.dosingGuideline[generalDosing].dosage.type.text 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.type.text ^short = "The Header e.g. 'Dosing instructions for adults'"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.patientInstruction 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.patientInstruction ^short = "Instructions described in leaflet for administration if not other prescribed"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction 1..* 
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction only CodeableConcept 
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction.coding.system from AdditionalInstruction (required) // Use coding if specific codes are applicable
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction.text ^short = "Instruction as text always required, if no code is available it should contain the whole instruction, if code can be specified, the instruction as text field should only contain buzzwords to describe the code"
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.additionalInstruction.text 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route 1..1 MS
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route only CodeableConcept
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route.text 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.route.text ^short = "Route of administration e.g. To be ingested"

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.doseAndRate.doseQuantity.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration 1..1 MS
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerAdministration.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod 1..1 MS
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.numerator.unit 1..1

* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator 1..1 MS
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.value 1..1
* indicationGuideline.dosingGuideline[generalDosing].dosage.dosage.maxDosePerPeriod.denominator.unit 1..1

* storageGuideline 1..* 
* storageGuideline.note.text 1..1
* storageGuideline.note.text ^short = "Description of storage guideline in text"
* storageGuideline.environmentalSetting 0..1
* storageGuideline.environmentalSetting.type ^short = "Categorization of the setting e.g coding for celsius"
* storageGuideline.environmentalSetting.type 1..1
* storageGuideline.environmentalSetting.valueRange ^short = "Value range of the environmental setting"
* storageGuideline.environmentalSetting.valueRange.high.value 0..1

* definitional.definition 1..1 MS
* definitional.definition only Reference (MedicinalProductDefinition)

* definitional.doseForm.coding from DoseForm (required)
* definitional.doseForm.coding 0..1
* definitional.doseForm.text ^short = "The doseform of the medication as text"
* definitional.doseForm.text 1..1 MS

* definitional.drugCharacteristic 0..* 
* definitional.drugCharacteristic.valueString 1..1
* definitional.drugCharacteristic.valueString ^short = "Description of characteristic found in leaflet, if coding provided suitable to coding. If no coding present whole visual charecteristics described in valueString."

* clinicalUseIssue ^short = "Reference to the ClinicalUseDefinition to describe every side effect, interaction, contraindication, warning"

* clinicalUseIssue ^slicing.discriminator.type = #value
* clinicalUseIssue ^slicing.discriminator.path = "display"
* clinicalUseIssue ^slicing.rules = #open

* clinicalUseIssue contains SideEffect 1..* MS
* clinicalUseIssue contains Interaction 1..* MS
* clinicalUseIssue contains Contraindication 1..* MS
* clinicalUseIssue contains Warning 1..* MS

* clinicalUseIssue[SideEffect] only Reference(UndesirableEffect) 
* clinicalUseIssue[Interaction] only Reference(Interaction) 
* clinicalUseIssue[Contraindication] only Reference(Contraindication) 
* clinicalUseIssue[Warning] only Reference(Warning)

* clinicalUseIssue[SideEffect].display = "http://localhost:8080/fhir/StructureDefinition/undesirable-effect"
* clinicalUseIssue[Interaction].display = "http://localhost:8080/fhir/StructureDefinition/interaction" 
* clinicalUseIssue[Contraindication].display = "http://localhost:8080/fhir/StructureDefinition/contraindication"
* clinicalUseIssue[Warning].display = "http://localhost:8080/fhir/StructureDefinition/warning"


