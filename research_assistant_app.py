import streamlit as st
import google.generativeai as genai
import os
import time
# Import the articles from our local database file
from articles_db import ARTICLES

# --- Configuration ---
# Securely loads the API key from Hugging Face secrets. Your key is NOT in this file.
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# --- AI Model Setup ---
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    # This will show a clear error if the API key is missing in the secrets
    st.error(f"Failed to initialize the AI model. Have you set the GOOGLE_API_KEY secret in your Space settings? Error: {e}")
    st.stop()

# --- Rate Limiter Functions ---
def check_rate_limit(limit=1, period_seconds=3600): # Limit set to 1 per hour
    """Checks the usage limit based on Streamlit's Session State."""
    if 'usage_log' not in st.session_state:
        st.session_state.usage_log = []
    
    current_time = time.time()
    cutoff_time = current_time - period_seconds
    st.session_state.usage_log = [ts for ts in st.session_state.usage_log if ts > cutoff_time]
    
    return len(st.session_state.usage_log) < limit

def add_usage_record():
    """Adds a new usage timestamp to the session state."""
    st.session_state.usage_log.append(time.time())

# --- Agent Classes ---
class AnalysisAgent:
    def __init__(self, model):
        self.model = model

    def analyze(self, text, original_question):
        prompt = f"""Act as a research analyst. Analyze the provided text to extract key facts, figures, and arguments relevant to the question: "{original_question}". Return findings as a clean bulleted list."""
        response = self.model.generate_content(prompt)
        return response.text

class WriterAgent:
    def __init__(self, model):
        self.model = model

    def write_report(self, findings, original_question):
        prompt = f"""Act as an expert research analyst. Synthesize the following findings into a coherent, well-written report with an executive summary, addressing the research question: "{original_question}"."""
        response = self.model.generate_content(prompt)
        return response.text

# --- Streamlit App (The "Manager Agent") ---
st.title("🤖 AI Research Assistant")

# --- Disclaimer about the static database ---
st.info(
    """**Important Note:** This is a portfolio demonstration. The AI's knowledge is limited to a pre-defined, static set of articles about the business and economic impact of Generative AI. It does not perform live web searches.
    """, 
    icon="ℹ️"
)

user_question = st.text_area("Enter your research question about the business impact of Generative AI:", "", height=100)

if st.button("Begin Research"):
    if not user_question.strip():
        st.warning("Please enter a research question first.")
    # --- Check the rate limit before proceeding ---
    elif not check_rate_limit():
        st.error("Rate limit exceeded. Please try again in an hour.")
    else:
        try:
            with st.status("Initializing agents and starting research...", expanded=True) as status:
                status.write("Instantiating agent team...")
                analysis_agent = AnalysisAgent(model)
                writer_agent = WriterAgent(model)

                status.update(label="Loading articles from internal knowledge base...")
                combined_text = ""
                sources_used = [article['source'] for article in ARTICLES]
                for article in ARTICLES:
                    combined_text += article['content'] + "\n\n--- End of Article ---\n\n"
                
                st.write("Using the following internal sources for analysis:")
                for source in sources_used:
                    st.write(f"- {source}")
                
                status.update(label="Analyzing findings from articles...")
                analysis_results = analysis_agent.analyze(combined_text, user_question)

                status.update(label="Writing final comprehensive report...")
                final_report = writer_agent.write_report(analysis_results, user_question)
                
                status.update(label="Research complete!", state="complete", expanded=False)
            
            # Log a successful use for the rate limiter
            add_usage_record()
            
            st.success("Research complete!")
            st.markdown("---")
            st.subheader("Final Report")
            st.markdown(final_report)

        except Exception as e:
            st.error(f"The research process failed. Error: {e}")

