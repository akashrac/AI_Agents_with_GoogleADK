from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from .tools import calculate_trip_budget, format_search_dates

root_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="airbnb_travel_planner",
    instruction="""You are an expert travel planning assistant with access to real-time Airbnb data.

    **Available Tools:**
    - airbnb_search: Search for Airbnb listings
    - airbnb_listing_details: Get detailed property information
    - calculate_trip_budget: Calculate total costs across multiple properties
    - format_search_dates: Convert start date and nights into checkin/checkout dates

    When calculating multi-city trips:
    1. After searching each city, use calculate_trip_budget to get cost summaries
    2. Use format_search_dates if user provides "nights" instead of checkin/checkout dates
    3. Present comprehensive budget breakdowns
    """,
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
                ),
            ),
            tool_filter=['airbnb_search', 'airbnb_listing_details']
        ),
        calculate_trip_budget,
        format_search_dates,
    ],
)
