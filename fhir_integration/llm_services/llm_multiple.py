from fhir_integration.llm_services.llm_base import LLMServiceBase

class LLMMultiple(LLMServiceBase): 

    def __init__(self, questions: dict, ):
        self.questions = questions
        self.role = (
            'Du bist ein e-Health Experte der sich Informationen aus einem '
            'Medikamenten-Beipackzettel holt damit diese in einem späteren '
            'Schritt als FHIR-Ressource abgelegt werden können. '
            'Extrahiere nur die nötige Information und antworte direkt auf die Frage'
        )

    def extract_info(self, leaflet_text):
        extracted_info = {}
        for key, question in self.questions.items():
            question_with_txt = (
                f"{question['question']} {leaflet_text}"
            )
            result = self.ask_llm(
                role=self.role,
                prompt=question_with_txt
            )
            if "following" in list(question.keys()):
                following_questions = question["following"]
                for following_key, following_question in following_questions.items():
                    following_question_with_txt = (
                        f"{following_question['question']} {result}"
                    )
                    following_result = self.ask_llm(
                        role=self.role,
                        prompt=following_question_with_txt
                    )
                    extracted_info[following_key] = following_result

            extracted_info[key] = result
        return extracted_info 
    
   
