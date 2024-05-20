# from transformers import pipeline
from openai import OpenAI
from fhir_integration.services.secrets import access_secret_version

openai_api_key = access_secret_version('openai_key')
openai_organization_id = access_secret_version('openai_id')

client = OpenAI(
    api_key=openai_api_key,
    organization=openai_organization_id,
)

class LLMService:
    
    def __init__(self):
        # self.extractor = pipeline('question-answering',  model="deepset/roberta-base-squad2")
        pass

    def extract_organization_info(self, leaflet_txt):
        questions_organization = {
            "orgName": (
                "Wie lautet der vollständige Name des Hersteller oder der Herstellerfirma. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. Suche exakt den Hersteller"
                "Die Antwort sollte nur den Herstellernamen enthalten"
            ),
            "shortNameAsID" : (
                "Finde den Herstellernamen und generiere ein Kürzel mit welchen sich der Hersteller identifzieren lässt. "
                "Die Anwort sollte nur das Kürzel enthalten"
            ),
            
            "address_street_number": (
                "Suche die Adresszeile des Herstellers. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                "Aus der Adresszeile des Herstellers extrahiere die Strasse und Türnummer, falls vorhanden. "
                "Ist keine Strasse und Türnummer vorhanden antworte ausschliesslich mit None! "
            ),
            "address_city": (
                "Suche die Adresszeile des Herstellers. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                "Aus der Adresszeile des Herstellers extrahiere die Stadt, falls vorhanden. "
                "Ist keine Stadt angegeben antworte ausschliesslich mit None! "
            ),
            "address_zip": (
                "Suche die Adresszeile des Herstellers. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                "Aus der Adresszeile des Herstellers extrahiere die Postleitzahl. "
                "Die Antwort sollte nur die Postleitzahl enthalten!"
            ),
            "address_country": (
                "Suche die Adresszeile des Herstellers. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                "Extrahiere das Land aus der Adresszeile. "
                "Die Antwort sollte nur das Land enthalten!"
            ),
            "webAdress": (
                "Suche nach der Webadresse des Herstellers. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                "Ist keine Webadresse angegeben so antworte ausschliesslich mit None! "
            ),
            "fax":  (
                "Suche nach der Faxnummer des Herstellers. "
                "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                "Ist keine Faxnummer angegeben so antworte ausschliesslich mit None! "
            )
        }

        extracted_org_info = {}
        for key, question in questions_organization.items():
            # result = self.extractor(question=question, context=leaflet_txt)
            question_with_txt = (
                f"{question} {leaflet_txt}"
            )
            role = (
                'Du bist ein e-Health Experte der sich Informationen aus einem '
                'Medikamenten-Beipackzettel holt damit diese in einem späteren '
                'Schritt als FHIR-Ressource abgelegt werden können. '
                'Extrahiere nur die nötige Information und antworte direkt auf die Frage'
            )
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": role},
                    {"role": "user", "content": question_with_txt}
                ],
            )
            result = response.choices[0].message.content.strip()
            if result == 'None':
                result = None
            # print(f"question: {question}, result: {result}")
            # print("--------------------------------------------------------------------------")
            extracted_org_info[key] = result
        return extracted_org_info
