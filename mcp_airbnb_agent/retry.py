# airbnb_agent/retry.py
from google.genai import types

# Simple retry configuration without RetryOptions
retry_config = types.GenerateContentConfig(
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    max_output_tokens=2048,
)
