import streamlit as st
import google.generativeai as genai
import os
# --- NEW: Import the articles from our local database file ---
from articles_db import ARTICLES

# --- Configuration ---
# For local testing, replace with: genai.configure(api_key="YOUR_KEY")
genai.configure(api_key=""YOUR_API_KEY")

# --- AI Model Setup ---
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Failed to initialize the AI model. Please check your API key. Error: {e}")
    st.stop()


# --- Agent Classes (SearchAgent and ScrapingAgent are now removed) ---

class AnalysisAgent:
    def __init__(self, model):
        self.model = model

    def analyze(self, text, original_question):
        prompt = f"""Act as a research analyst. Your task is to analyze the following text from multiple articles and extract the key facts, figures, and arguments that are directly relevant to the user's research question.

        User's Research Question: "{original_question}"

        Please return your findings as a clean, well-organized bulleted list.
        ---
        Scraped Text:
        {text}
        """
        response = self.model.generate_content(prompt)
        return response.text

class WriterAgent:
    def __init__(self, model):
        self.model = model

    def write_report(self, findings, original_question):
        prompt = f"""Act as an expert research analyst and writer. Your task is to synthesize the following bulleted list of findings into a coherent, well-written, and professional final report. The report must directly address the user's original research question.

        The report should begin with a concise executive summary.

        User's Original Research Question: "{original_question}"
        ---
        Key Findings to Synthesize:
        {findings}
        """
        response = self.model.generate_content(prompt)
        return response.text


# --- Streamlit App (The "Manager Agent") ---
st.title("🤖 AI Research Assistant")

user_question = st.text_area("Enter your complex research question:", "", height=100)

if st.button("Begin Research"):
    if not user_question.strip():
        st.warning("Please enter a research question first.")
    else:
        try:
            with st.status("Initializing agents and starting research...", expanded=True) as status:
                
                status.write("Instantiating agent team...")
                analysis_agent = AnalysisAgent(model)
                writer_agent = WriterAgent(model)

                # --- NEW: Load articles directly from the database file ---
                status.update(label="Loading articles from local database...")
                
                # Combine the content of all articles into a single text block
                combined_text = ""
                sources_used = []
                for article in ARTICLES:
                    combined_text += article['content'] + "\n\n--- End of Article ---\n\n"
                    sources_used.append(article['source'])
                
                st.write("Using the following internal sources for analysis:")
                for source in sources_used:
                    st.write(f"- {source}")
                
                status.update(label="Analyzing findings from articles...")
                analysis_results = analysis_agent.analyze(combined_text, user_question)

                status.update(label="Writing final comprehensive report...")
                final_report = writer_agent.write_report(analysis_results, user_question)
                
                status.update(label="Research complete!", state="complete", expanded=False)

            st.success("Research complete!")
            st.markdown("---")
            st.subheader("Final Report")
            st.markdown(final_report)

        except Exception as e:
            st.error(f"The research process failed. Error: {e}")


