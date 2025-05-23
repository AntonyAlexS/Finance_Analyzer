# -*- coding: utf-8 -*-
"""Final_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IN5I6Q7-VDs51KH2JDYhYoNdDAGRmdFM
"""

!pip install PyPDF2
!pip install google-generativeai
!pip install streamlit
!pip install pyngrok

# Set up Google Gemini API Key
from google.colab import userdata
import google.generativeai as genai
GEMINI_API_KEY = userdata.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Use the model directly
model = genai.GenerativeModel(model_name="models/learnlm-2.0-flash-experimental")

response = model.generate_content("Explain about Data Science in shortly")
print(response.text)

import os

# Create a folder named .streamlit
os.makedirs(".streamlit", exist_ok=True)

# Save the key in a file called secrets.toml
with open(".streamlit/secrets.toml", "w") as f:
    f.write(f'GEMINI_API_KEY = "{GEMINI_API_KEY}"')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import os
# import streamlit as st
# import PyPDF2
# import google.generativeai as genai
# 
# 
# # Streamlit UI
# st.set_page_config(page_title="Finance Analyzer for UPI Transactions", page_icon="💰", layout="wide")
# 
# 
# # Sidebar with usage info
# st.sidebar.title("ℹ️ How to Use This Tool?")
# st.sidebar.write("- Upload your UPI Transaction statement in PDF format.")
# st.sidebar.write("- The AI Powered finance analyzer will analyze your transactions.")
# st.sidebar.write("- You will receive financial insights including income, expenses, savings, and spending trends.")
# st.sidebar.write("- Use this data to plan your finances effectively.")
# st.sidebar.write("Please note : The document you uploaded will not be stored and will be deleted after the analysis is complete.")
# 
# 
# st.markdown("<h1 style='text-align: center;'>💰 Finance Analyzer for UPI Transactions</h1>",
#     unsafe_allow_html=True)
# st.markdown("<div style='text-align: center;'>Upload your UPI Transaction statement in PDF format for Financial Insights</div>",unsafe_allow_html=True)
# 
# 
# # Upload PDF File
# uploaded_file = st.file_uploader("📂 Upload PDF File", type=["pdf"], help="Only PDF files are supported")
# 
# def extract_text_from_pdf(file_path):
#     """Extracts text from the uploaded PDF file."""
#     text = ""
#     with open(file_path, "rb") as pdf_file:
#         reader = PyPDF2.PdfReader(pdf_file)
#         for page in reader.pages:
#             text += page.extract_text() + "\n"
#     return text.strip()
# 
# def analyze_financial_data(text):
#     """Sends extracted text to Google Gemini AI for financial insights."""
#     model = genai.GenerativeModel("models/learnlm-2.0-flash-experimental")
# 
#     prompt = f"""
#     Analyze the following UPI transaction statement and generate financial insights:
#     You are a financial advisor AI specialized in analyzing UPI transaction statements. A user will provide you with their recent UPI transaction data. Your task is to:
# 
#     1. Summarize total spending by category and monthwise and mention the amount spend (e.g., Food - Rs.1000, Transport - Rs.1500, Shopping - Rs.3000 , Utilities - Rs.8000, etc.)
#     2. Create a suggested monthly budget based on their current spending patterns.
#     3. Identify unnecessary or excessive spending and suggest realistic ways to reduce it.
#     4. Provide personalized financial advice to help them save more and manage their money better.
# 
#     UPI Statement Format (Example):
#     "Paid ₹120 to Swiggy on 5th May"
#     "Received ₹1500 from Rahul on 6th May"
#     "Paid ₹2000 to Amazon on 7th May"
#     ...
# 
#     Now, analyze the following UPI statements:
#     {text}
# 
# 
#     Please give your output in the following format:
# 
#     ---
# 
#     **1. Monthly Spending Summary by Category:**
#     provide month wise expense and inome breakup as much as possible breakup in tabular column
#     - Food: ₹____
#     - Shopping: ₹____
#     - Transport: ₹____
#     - Utilities: ₹____
#     - Others: ₹____
# 
#     **2. Suggested Monthly Budget Plan:**
#     - Total income: ₹____
#     - Total spending: ₹____
#     - Recommended spending limits by category:
#     - Food: ₹____
#     - Shopping: ₹____
#     - Transport: ₹____
#     - Savings Goal: ₹____
# 
#     **3. Suggestions to Reduce Unnecessary Spending:**
#     - [Example: Limit food delivery to 2x a week, consider meal prep to save ₹1000/month]
# 
#     **4. Personalized Financial Advice:**
#     - [I need financial advice to manage my income, savings, and expenses better. Can you help me create a simple monthly budget and suggest ways to save more?"]
# """
#     response = model.generate_content(prompt)
#     return response.text.strip() if response else "⚠️ Error processing financial data."
# 
# 
# if uploaded_file is not None:
#     file_path = f"temp_{uploaded_file.name}"
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.read())
# 
#     st.success("✅ File uploaded successfully!")
# 
#     with st.spinner("📄 Extracting text from document..."):
#         extracted_text = extract_text_from_pdf(file_path)
# 
#     if not extracted_text:
#         st.error("⚠️ Failed to extract text. Ensure the document is not a scanned image PDF.")
#     else:
#         progress_bar = st.progress(0)
#         with st.spinner("🧠 AI is analyzing your financial data..."):
#             insights = analyze_financial_data(extracted_text)
# 
#         progress_bar.progress(100)
# 
#         st.subheader("📊 Financial Insights Report")
#         st.markdown(f'<div class="result-card"><b>📄 Financial Report for {uploaded_file.name}</b></div>', unsafe_allow_html=True)
# 
#         st.write(insights)
# 
#         st.markdown('<div class="success-banner">🎉 Analysis Completed! Plan your finances wisely. 🚀</div>', unsafe_allow_html=True)
#         st.balloons()
# 
#     os.remove(file_path)  # Cleanup

import streamlit as st
from pyngrok import ngrok
from google.colab import userdata
!streamlit cache clear
!pkill ngrok
!pkill streamlit
auth_token=userdata.get('auth_token')

# Terminate any existing ngrok processes
!pkill -f ngrok

ngrok.set_auth_token(auth_token)
port = 8501

# Start Streamlit in the background
!streamlit run app.py &>/dev/null&

# Connect ngrok to the Streamlit port
public_url = ngrok.connect(port)
print("Streamlit App is live at:", public_url)

