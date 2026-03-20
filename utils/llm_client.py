import os
from openai import AzureOpenAI

api_key = os.getenv("AZURE_API_KEY")
endpoint = os.getenv("AZURE_ENDPOINT")
deployment = os.getenv("AZURE_DEPLOYMENT")

if not api_key or not endpoint or not deployment:
    raise ValueError("Missing Azure OpenAI environment variables")

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version="2024-05-01-preview"
)

DEPLOYMENT_NAME = deployment


def call_llm(system_prompt, user_input):
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
