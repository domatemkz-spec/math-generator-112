import streamlit as st

# Глобальная настройка платформы (запускается один раз для всего сайта)
st.set_page_config(
    page_title="Панель конструирования КИМ по КТП", 
    page_icon="🏛️",
    layout="wide"
)

# Строим полную структуру академической платформы
pg = st.navigation({
    "Информационная панель": [
        st.Page("main_hub.py", title="Главная панель наставника", icon="🏠"),
    ],
    "Среднее звено (5-9 классы)": [
        st.Page("class_5.py", title="Математика — 5 класс", icon="✏️"),
        st.Page("class_6.py", title="Математика — 6 класс", icon="✏️"),
        st.Page("class_7.py", title="Алгебра / Геометрия — 7 класс", icon="📐"),
        st.Page("class_8.py", title="Алгебра / Геометрия — 8 класс", icon="📐"),
        st.Page("class_9.py", title="Алгебра / Геометрия — 9 класс", icon="📐"),
    ],
    "Старшая школа (ЕМН / ОГН)": [
        st.Page("class_10_emn.py", title="10 класс (ЕМН)", icon="🏛️"),
        st.Page("class_10_ogn.py", title="10 класс (ОГН)", icon="📜"),
        st.Page("class_11_emn.py", title="11 класс (ЕМН)", icon="🏛️"),
        st.Page("class_11_ogn.py", title="11 класс (ОГН)", icon="📜"),
    ]
})

# Запуск единой экосистемы
pg.run()
