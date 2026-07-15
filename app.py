import streamlit as st

# Глобальная настройка страницы (запускается один раз здесь)
st.set_page_config(page_title="Платформа FutureSkillsScrum", layout="wide")

# Объявляем многостраничную структуру по классам
pg = st.navigation([
    st.Page("main_hub.py", title="Главная панель наставника", icon="🏠"),
    st.Page("class_5.py", title="Математика — 5 класс", icon="✏️"),
    st.Page("class_7.py", title="Алгебра и Геометрия — 7 класс", icon="📐")
])

# Запуск выбранной страницы
pg.run()
