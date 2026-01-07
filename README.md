# AI Agents with Google ADK

A collection of AI agents built using Google Agent Development Kit (ADK) and Gemini, demonstrating custom tools, nested agent patterns, and automated reasoning capabilities.

## Table of Contents

- [Overview](#overview)
- [Agents](#agents)
  - [Google Search Agent](#-google-search-agent)
  - [Currency Conversion Agent](#-currency-conversion-agent)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Clone Repository](#clone-repository)
  - [Windows (PowerShell)](#windows-powershell)
  - [Mac/Linux](#maclinux)
  - [Access ADK Web Interface](#access-adk-web-interface)
- [Project Structure](#project-structure)
- [ADK Web Features](#adk-web-features)

## Overview

This repository showcases:
- Building AI agents with Google ADK
- Custom function tools with business logic
- Nested agent patterns using AgentTool
- Built-in code execution for reliable calculations
- Google Search integration for real-time information
- Secure authentication (AI Studio or Vertex AI)
- Production-ready structure with retry handling

## Agents

### 🔍 Google Search Agent
An AI agent that answers general questions and automatically uses Google Search to fetch up-to-date information when needed.

**Features:**
- 🤖 Gemini-powered reasoning (gemini-2.0-flash-exp)
- 🔍 Automatic Google Search tool usage
- 🔁 Retry handling with exponential backoff
- 🔐 Secure authentication

### 💱 Currency Conversion Agent
An intelligent currency converter that calculates conversion costs including transaction fees using custom tools and nested agent architecture.

**Features:**
- 🛠️ Custom function tools (fee lookup, exchange rates)
- 🧮 Nested calculation agent with BuiltInCodeExecutor
- 📊 Detailed breakdown of conversions with fees
- ✅ Structured error handling with status responses
- 🎯 AgentTool pattern for reliable math calculations

**Workflow:**
1. Looks up transaction fees for payment method
2. Retrieves currency exchange rates
3. Delegates calculation to specialist agent
4. Generates Python code for precise math
5. Returns detailed breakdown with final amount

### 🏠 Airbnb Travel Planning Agent
An intelligent travel planning assistant that searches real-time Airbnb listings across multiple cities using Model Context Protocol (MCP) integration with Google ADK.

**Features:**
- 🤖 Gemini-powered reasoning (gemini-2.0-flash-exp)
- 🔌 MCP server integration via @openbnb/mcp-server-airbnb
- 🌎 Multi-city search with parallel comparison capabilities
- 💰 Real-time pricing and availability checking
- 🏷️ Advanced filtering (dates, guests, price range, amenities)
- 📊 Automatic trip budget calculations and cost breakdowns
- 🔗 Direct booking links to available properties
- ⚡ Rate limiting and error handling for reliable searches
- 🎯 Pet-friendly, work-friendly, and custom amenity filtering

**MCP Integration:**
This agent demonstrates Google ADK's Model Context Protocol (MCP) capabilities by connecting to an external Node.js-based Airbnb search server. The `McpToolset` enables seamless integration with npm packages, allowing the agent to:
- Execute external tools without Python dependencies
- Communicate with Node.js MCP servers via stdio transport
- Access live web data through standardized protocol
- Filter and expose specific MCP tools to the agent

**Workflow:**
1. Accepts travel dates, destinations, and guest requirements
2. Connects to MCP server via stdio transport
3. Searches Airbnb using `airbnb_search` tool for each city
4. Filters properties by budget, amenities, and preferences
5. Retrieves detailed info using `airbnb_listing_details` tool
6. Calculates per-night and total costs for each location
7. Compares options across cities with analysis
8. Returns comprehensive results with direct booking links


## Features

🤖 **Gemini-powered reasoning** (gemini-2.5-flash-lite)  
🔍 **Automatic Google Search tool usage**  
🔁 **Retry handling** with exponential backoff  
🔐 **Secure authentication**
🧱 **Clean, maintainable project structure**


## Prerequisites

- Python 3.10+
- Google Cloud SDK (`gcloud`) installed and authenticated
- Access to Google Cloud project with active Vertex AI environment
- Git installed


### Clone Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd AI_Agents_with_GoogleADK
```

Replace `<repository-url>` with the actual repository URL provided by organizers.

### Setup Instructions

**Important**: Use the commands for your operating system. Windows uses PowerShell commands, while Mac/Linux use bash commands.

#### Windows (PowerShell)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.bat

# Install dependencies
pip install google-adk

# Authenticate with Google Cloud
# This will open a browser window - use your Google email to sign in
gcloud auth application-default login

# (Optional) Set Google Cloud project for gcloud commands
# Note: This is optional - your .env file will set the project for the agents
# If you get a password prompt, you can skip this step
# gcloud config set project project_id

# Launch ADK Web Server
adk web

```

#### Mac/Linux

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install google-adk

# Authenticate with Google Cloud
# This will open a browser window - use your Google email to sign in
gcloud auth application-default login

# (Optional) Set Google Cloud project for gcloud commands
# Note: This is optional - your .env file will set the project for the agents
# If you get a password prompt, you can skip this step
# gcloud config set project project_id

# Launch ADK Web Server
adk web

# In a second terminal, start the Streamlit testing console
streamlit run ui/hackathon_agents_ui.py
```

### Access ADK Web Interface

1. Open browser to `http://localhost:8000`
2. In ADK Web, select an agent (e.g., `google_search_agent`) from the dropdown menu
3. Enter your query in the chat interface


## Project Structure
```
AI_Agents_with_google/
├── google_search_agent/
│ ├── init.py
│ ├── agent.py # Main agent definition
│ ├── retry.py # Retry configuration
│ └── .env # Environment variables
│
├── currency_agent/
│ ├── init.py
│ ├── agent.py # Root agent definition
│ ├── tools.py # Custom function tools (fee lookup, exchange rates)
│ ├── calculation_agent.py # Nested calculation agent with BuiltInCodeExecutor
│ ├── retry.py # Retry configuration
│ └── .env # Environment variables
│
├── mcp_airbnb_agent/
│ ├── init.py
│ ├── agent.py # Root agent with MCP integration
│ ├── tools.py # Custom function tools
│ ├── retry.py # Retry configuration
│ └── .env # Environment variables
│
├── .env.example # Example environment variables template
├── .gitignore
└── README.md
```

### ADK Web Features

- **Sessions**: Each conversation creates a session with full history
- **Events**: Step-by-step agent actions (tool calls, responses)
- **Trace**: Visual execution flow showing agent relationships and data flow
