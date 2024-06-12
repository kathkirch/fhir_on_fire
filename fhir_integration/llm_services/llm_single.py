from fhir_integration.llm_services.llm_base import LLMServiceBase
from fhir_integration.llm_services.questions import questions_organization

class LLMSingle(LLMServiceBase):
    
    def __init__(self, questions: dict):
        self.questions = questions
        self.role = (
            'Du bist ein e-Health Experte der sich Informationen aus einem '
            'Medikamenten-Beipackzettel holt damit diese in einem späteren '
            'Schritt als FHIR-Ressource abgelegt werden können. '
            'Extrahiere nur die nötige Information und antworte direkt auf die Frage. '
            'Antworten sollten keine Querverweise auf andere Abschnitte oder Aufzählungszeichen enthalten. '
        )

    def extract_info(self, leaflet_text):
        extracted_info = {}
        for key, question in self.questions.items():
            question_with_txt = (
                f"{question} {leaflet_text}"
            )

            result = self.ask_llm(
                role=self.role,
                prompt=question_with_txt
            )
            extracted_info[key] = result
        return extracted_info
    


# Instanzierung der Klasse

# llm_organization = LLMSingle(questions=questions_organization)

# llm_organization.extract_info("text")