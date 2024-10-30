import json
from typing import Any, Dict

import google.generativeai as genai
from app import app
from app.constants import MODEL_TEMPERATURE
from app.utils.model_config import (
    GEMINI_MODEL,
    SYSTEM_INSTRUCTION,
    generate_prompt,
    get_gemini_generation_config,
)

try:
    genai.configure(api_key=app.config['GOOGLE_GEMINI_API_KEY'])
except Exception as e:
    raise Exception(
        'Failed to configure the Gemini GenAI API. Check whether the API key is valid.'
    ) from e

model = genai.GenerativeModel(
    model_name=GEMINI_MODEL, system_instruction=SYSTEM_INSTRUCTION
)


def get_gemini_response(scraped_insights: Dict[str, Any]) -> Dict[str, Any]:
    try:
        response = model.generate_content(
            f'{generate_prompt(scraped_insights)}',
            generation_config=get_gemini_generation_config(
                temperature=MODEL_TEMPERATURE
            ),
        )

        json_response = json.loads(response.text)

        return {
            'response': json_response,
        }

    except Exception as e:
        raise RuntimeError(
            f'Failed to generate summary using gemini: {str(e)}'
        ) from e
