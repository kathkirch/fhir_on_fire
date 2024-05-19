class LLMService:
    
    def __init__(self):
        self.extractor = pipeline('question-answering')

    def extract_organization_info(self, leaflet_txt):
        questions_organization = {
            "shortNameAsID" : "Mit welchem Namen lässt sich der Hersteller kurz identifizieren?"
            "orgName": "Wie lautet der vollständige Name des Hersteller oder der Herstellerfirma"
            "address_street_number": "Wie lautet die Strasse und Türnummer des Herstellers"
            "address_city": "Welche Stadt ist in der Adresse des Herstellers angegeben?"
            "address_zip": "Welche Postleitzahl ist in der Adresse des Herstellers angegeben"
            "address_country": "Welches Land ist in der Adresse des Herstellers angegeben"
            "webAdress": "Wenn der Hersteller eine Webadresse angibt, wie lautet sie?"
            "fax":  "Wenn der Hersteller eine Faxnummer angibt, wie lautet sie?"
        }

        extracted_org_info = {}
        for key, question in questions_organization.items():
            result = self.extractor(question=question, context=leaflet_text)
            extracted_info[key] = result['answer']
        
        return extracted_org_info
