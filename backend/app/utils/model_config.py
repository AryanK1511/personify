from typing import Dict

import google.generativeai as genai

# Define the models and system instruction
GEMINI_MODEL = 'gemini-1.5-flash'

SYSTEM_INSTRUCTION = """
You are analyzing web content to identify potential visitor profiles.
Your task is to suggest visitor profiles that would be most interested in the content,
based on the topics, themes, and structure of the scraped content.
"""


def generate_prompt(scraped_content: Dict[str, str]) -> str:
    return f"""
    Analyze the following website content to identify visitor profiles 
    that would likely access and engage with it:

        {scraped_content}

    Based on the topics, themes, and general tone of the content,
    suggest different types of visitor profiles.
    For example, a tech blog might attract profiles like "AI Enthusiast",
    "Web Developer", or "Product Manager".

    The scraped content that I gave you can be from any type of website though.

    Format your response as a JSON object with a single key `"profiles"`, which is an array of objects.
    Each profile object should contain:
    - `"profile_name"`: A brief title for the profile (e.g., "AI Enthusiast")
    - `"description"`: A brief description of why this profile would be interested in the content.

    Structure the output as follows:

    ```json
    {{
      "profiles": [
        {{
          "profile_name": "string",
          "description": "string"
        }}
      ]
    }}
    ```

    Ensure each profile is distinct and describes a clear reason for engagement with the content.
    """


def get_gemini_generation_config(
    candidate_count=1,
    temperature=0.5,
    stop_sequences=None,
    max_output_tokens=None,
):
    if stop_sequences is not None and (
        not isinstance(stop_sequences, list)
        or len(stop_sequences) > 5
        or not all(isinstance(seq, str) for seq in stop_sequences)
    ):
        raise ValueError('stop_sequences must be a list of up to 5 strings.')

    if max_output_tokens is not None and (
        not isinstance(max_output_tokens, int) or max_output_tokens < 1
    ):
        raise ValueError('max_output_tokens must be an integer ≥ 1.')

    return genai.types.GenerationConfig(
        candidate_count=candidate_count,
        temperature=temperature,
        stop_sequences=stop_sequences or [],
        max_output_tokens=max_output_tokens,
        response_mime_type='application/json',
    )
