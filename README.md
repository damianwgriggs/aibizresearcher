AI Research Assistant
This is an advanced, multi-agent AI application that takes a user's complex research question, analyzes information from a curated internal knowledge base, and synthesizes the findings into a comprehensive, final report.

This project serves as a portfolio piece demonstrating a sophisticated, agent-based architecture and the ability to make critical design pivots to ensure application stability and reliability.

Project Architecture: A Multi-Agent System
This application functions as an AI Agent Orchestrator. It manages a team of specialized AI agents where the output of one agent becomes the input for the next, creating an automated research pipeline.

The workflow is as follows:

The "Manager" (Main App): The Streamlit script receives the user's research question.

Data Loading: Instead of performing live, unreliable web searches, the application loads pre-vetted articles from a local, static knowledge base (articles_db.py).

The "Analysis" Agent: This agent reads the combined text from the knowledge base and uses a powerful, context-aware prompt to extract the specific information needed to answer the user's question.

The "Writer" Agent: This agent takes the structured findings from the Analysis Agent and synthesizes them into a final, coherent, and well-written report for the user.

The Architectural Pivot: From Web Scraper to Static Database
An initial version of this project used a live web scraping module. During development, it was determined that this created an unreliable external dependency, as websites frequently block scraping attempts. The architectural decision was made to pivot to an internal, static database (articles_db.py). This guarantees the application is always functional and robust, showcasing the ability to make sound design decisions to solve real-world engineering challenges.

Key Technologies
Python: The core programming language.

Streamlit: For building the interactive web interface.

Google Gemini API: For all natural language processing tasks (analysis and synthesis).

Setup and Configuration
To run this project, you will need a secret API key from Google.

1. Clone and Install
First, clone the repository from GitHub and install the necessary libraries from the requirements.txt file.

# Clone the repository
git clone [URL_OF_YOUR_GITHUB_REPO]

# Navigate into the project directory
cd AI-Research-Assistant

# Install all required libraries
pip install -r requirements.txt

2. API Key Configuration
This project is configured to use a secure method for handling API keys on a deployment server.

For Local Testing:
To run the app on your own computer, you must temporarily add your API key to the code.

Get your free API key from Google AI Studio.

Open the research_assistant_app.py file in a code editor.

Find the configuration line (around line 8):

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

Replace that entire line with the following, pasting your key inside the quotation marks:

genai.configure(api_key="YOUR_API_KEY_GOES_HERE")

For Deployment:
IMPORTANT: Before uploading your code to a public repository like GitHub or Hugging Face, you MUST revert the API key line back to the secure version:

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

You will then need to add your key to the Repository secrets in your Hugging Face Space's Settings, using GOOGLE_API_KEY as the name.

How to Run the App
To Run Locally: After adding your API key to the research_assistant_app.py file, run this command in your terminal:

streamlit run research_assistant_app.py

To Deploy: Upload the secure version of the code, the articles_db.py file, and the requirements.txt to a Hugging Face Space. The application will build and run automatically.
