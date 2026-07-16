import streamlit as st
import json
import google.generativeai as genai

def get_gemini_client():
    """Получение клиента Gemini с использованием официального SDK."""
    api_key = st.secrets.get("GEMINI_API_KEY", st.session_state.get("gemini_api_key", ""))
    if not api_key:
        return None
    try:
        genai.configure(api_key=api_key)
        # Простая проверка, что ключ работает
        genai.list_models()
        return genai
    except Exception as e:
        st.error(f"Ошибка подключения к Gemini: {e}")
        return None

# ... (остальные функции, но теперь они используют get_gemini_client() и genai)

def generate_math_task_gemini(...):
    client = get_gemini_client()
    if not client:
        return {"task": "Ошибка: API ключ не настроен", ...}

    model = client.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    # ... (обработка ответа)
