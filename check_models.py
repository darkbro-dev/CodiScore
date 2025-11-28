import google.generativeai as genai
import streamlit as st

# Load API Key
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# List all available models
print("=== 사용 가능한 모델 목록 ===")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")
        print(f"  지원 메서드: {model.supported_generation_methods}")
        print()
