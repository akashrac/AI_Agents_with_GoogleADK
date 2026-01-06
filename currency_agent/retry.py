from google.genai import types
# Retry configuration for Gemini API calls.
# Automatically retries transient failures (rate limits or temporary server errors)
# using exponential backoff to improve reliability.
#
# - attempts=5: Maximum retry attempts before failing
# - initial_delay=1: Wait 1 second before the first retry
# - exp_base=7: Exponentially increase wait time between retries
# - http_status_codes: Retry only on retryable server / rate-limit errors

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)
