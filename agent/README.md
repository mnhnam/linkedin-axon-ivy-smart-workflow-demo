# Web Crawler Agent

A Python-based web crawler agent using browser automation for web scraping and data collection.

## Prerequisites

- Python 3.12.7 or higher
- Windows PowerShell (for Windows users)

## Setup Instructions

### 1. Install Dependencies

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

This will install:

- `browser-use` - Browser automation library
- `playwright` - Web browser automation framework
- `python-dotenv` - Environment variable management

### 1. Create a Virtual Environment

First, create a virtual environment to isolate project dependencies:

```powershell
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment using the following command:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### 4. Initialize the Project

Run the setup script to complete the project initialization:

```powershell
.\setup.bat
```

This script will:

- Install Python dependencies (if not already installed)
- Install Playwright's Chromium browser with system dependencies
- Set up the necessary browser automation environment

## Environment Configuration

### Setting up your .env file

1. Copy the example environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

2. Edit the `.env` file and replace `your_openai_api_key_here` with your actual OpenAI API key:

   ```env
   OPEN_AI_API_KEY=sk-your-actual-api-key-here
   DEFAULT_MODEL=gpt-4.1-mini
   ```

**Important:** You must configure your OpenAI API key before running the crawler.

### Configuration Options

- **OPENAI_API_KEY**: Your OpenAI API key (required)
- **DEFAULT_MODEL**: The OpenAI model to use for job extraction (optional, defaults to `gpt-4.1-mini`)

Available models you can use:

- `gpt-4.1-mini` (recommended - cost-effective)
- `gpt-4.1` (more capable but more expensive)

## Development

When working on this project:

1. Always activate the virtual environment first
2. Install new dependencies using `pip install <package>`
3. Update `requirements.txt` with new dependencies:

   ```powershell
   pip freeze > requirements.txt
   ```

4. Test changes in the isolated virtual environment

## Project Structure

```plain
agent/
├── src/
│   ├── abstract_agent.py      # Abstract base class for all agents
│   ├── agent_factory.py       # Factory to create appropriate agents
│   ├── itviec_agent.py        # ITViec-specific job crawler
│   └── vietnamworks_agent.py  # VietnamWorks-specific job crawler
├── .env                       # Environment variables configuration
├── .env.example              # Environment variables template
├── main.py                   # Main entry point to run the application
├── requirements.txt          # Python dependencies
├── setup.bat                # Project initialization script
└── README.md                # This file
```

## Agent Architecture

The project uses an abstract agent pattern for extensibility and maintainability:

```
AbstractAgent (abstract_agent.py)
├── Provides common functionality:
│   ├── Browser initialization
│   ├── Environment configuration
│   └── Job posting extraction flow
│
├── ITViecAgent (itviec_agent.py)
│   ├── Supports: https://itviec.com/
│   └── Custom task template for ITViec website structure
│
└── VietnamWorksAgent (vietnamworks_agent.py)
    ├── Supports: https://www.vietnamworks.com/
    └── Custom task template for VietnamWorks website structure

AgentFactory (agent_factory.py)
└── URL-based agent selection:
    ├── "itviec.com" → ITViecAgent
    └── "vietnamworks.com" → VietnamWorksAgent
```

**How it works:**
1. Main application calls `create_agent(url)` 
2. Factory analyzes URL and returns appropriate agent
3. Agent uses its custom task template for the specific website
4. Results are automatically saved to `result.txt`

## Usage

After completing the setup steps above, your web crawler agent is ready to use.

### Running the Application

**Command Line Usage:**

```powershell
python main.py "https://www.vietnamworks.com" 3 "data science"
```

This will extract 3 "data science" jobs from vietnamworks.

**All parameters are required:**

- First parameter: Website URL (required)
- Second parameter: Number of jobs to extract (required)
- Third parameter: Search term (required)

### Output Options

- View results in the terminal
- Results automatically saved to `result.txt`
- Results include job titles, descriptions, and other relevant information

## Common Issues

### Stop agent

Press `Ctrl + C` to force stop the agent

### Deactivating the Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```powershell
deactivate
```

---

**Note:** This project requires browser automation capabilities. The setup script will install Chromium browser automatically for consistent cross-platform behavior.
