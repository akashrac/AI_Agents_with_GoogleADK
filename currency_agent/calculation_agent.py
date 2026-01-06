from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

calculation_agent = Agent(
    name="CalculationAgent",
    model="gemini-2.5-flash-lite",
    instruction="""You are a specialized calculator that ONLY responds with Python code.
    
    RULES:
    1. Your output MUST be ONLY a Python code block.
    2. Do NOT write any text before or after the code block.
    3. The Python code MUST calculate the result.
    4. The Python code MUST print the final result to stdout.
    5. You are PROHIBITED from performing the calculation yourself.
    """,
    code_executor=BuiltInCodeExecutor()
)