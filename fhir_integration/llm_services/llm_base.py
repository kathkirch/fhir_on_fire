from openai import OpenAI
from fhir_integration.services.secrets import access_secret_version

openai_api_key = access_secret_version('openai_key')
openai_organization_id = access_secret_version('openai_id')

client = OpenAI(
    api_key=openai_api_key,
    organization=openai_organization_id,
)


class LLMServiceBase:
    def __init__(self):
        pass

    def ask_llm(self, role, prompt):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ],
        )
        result = response.choices[0].message.content.strip()
        if result == 'None':
            result = None
        return result


