import os
from google import genai


def get_car_ai_bio(model, brand, year):
    contents = ''' Faça uma descrição de venda para o caro {} {} {}. Em apenas 200 caracteres, site as vantagens do modelo
'''

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    contents=contents.format(model, brand, year)
    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=contents
    )
    return(response.text)