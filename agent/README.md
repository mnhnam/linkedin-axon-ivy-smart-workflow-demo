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

## Project Structure

```plain
agent/
├── src/
│   └── agent.py        # Core web crawler agent logic
├── .env                # Environment variables configuration
├── main.py             # Main entry point to run the application
├── requirements.txt    # Python dependencies
├── setup.bat          # Project initialization script
└── README.md          # This file
```

## Usage

After completing the setup steps above, your web crawler agent is ready to use.

### Running the Application

**2. Command Line Arguments:**

```powershell
python main.py "https://www.vietnamworks.com" 3
```

This will extract 10 Python jobs from LinkedIn.

### Features

The project uses:

- **Playwright** for browser automation and web scraping
- **browser-use** for enhanced browser interaction capabilities
- **OpenAI GPT-4** for intelligent job extraction and parsing
- **Headless browsing** for better server compatibility

### Output Options

- View results in the terminal
- Optionally save results to a text file
- Results include job titles, descriptions, and other relevant information

## Environment Configuration

The project includes a `.env` file for environment-specific configuration. **Important:** You need to configure your OpenAI API key before running the crawler.

### Required Configuration

The `.env` file in the project root contains configurations for the project:

```env
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_MODEL=gpt-4.1-mini
```

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

## Common Issues

### File Saving Error
If you encounter "write() argument must be str, not AgentHistoryList" error when saving results:
- This has been fixed in the latest version
- The agent now properly converts history data to string format before saving

### General Troubleshooting
- Ensure your OpenAI API key is correctly set in `.env`
- Make sure you're running from the project root directory
- Check that all dependencies are installed with `pip install -r requirements.txt`

**Note**

Press `Ctrl + C` to force stop the agent

## Deactivating the Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```powershell
deactivate
```

---

**Note:** This project requires browser automation capabilities. The setup script will install Chromium browser automatically for consistent cross-platform behavior.
