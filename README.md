# Google Search Agent (ADK + Gemini)

An AI agent built using Google Agent Development Kit (ADK) and Gemini that answers general questions and automatically uses Google Search to fetch up-to-date information when needed.

## Overview

This project demonstrates:
- Building an AI agent with ADK
- Using Gemini models for reasoning
- Tool usage via Google Search
- Secure authentication (AI Studio or Vertex AI)
- Production-style structure with retries and safe secret handling

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
google_search_agent/
├── google_search_agent/
│   ├── __init__.py
│   ├── agent.py          # Main agent definition
│   ├── retry.py          # Retry configuration
│
├── .env.example          # Example environment variables
├── .gitignore
├── README.md
```

### ADK Web Features

- **Sessions**: Each conversation creates a session with full history
- **Events**: Step-by-step agent actions (tool calls, responses)
- **Trace**: Visual execution flow showing agent relationships and data flow
