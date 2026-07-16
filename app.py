import streamlit as st

# Глобальная настройка платформы
st.set_page_config(
    page_title="Панель конструирования КИМ по КТП", 
    page_icon="🏛️",
    layout="wide"
)

# =====================================================================
# ИМПОРТ ВСЕХ МОДУЛЕЙ СТРАНИЦ
# =====================================================================
import main_hub
import class_5
import class_6
import class_7
import class_8
import class_9
import class_10_emn
import class_10_ogn
import class_11_emn
import class_11_ogn

# =====================================================================
# СОЗДАЕМ АЛИАСЫ ДЛЯ ФУНКЦИЙ С УНИКАЛЬНЫМИ ИМЕНАМИ
# =====================================================================
page_main = main_hub.render
page_5 = class_5.render
page_6 = class_6.render
page_7 = class_7.render
page_8 = class_8.render
page_9 = class_9.render
page_10_emn = class_10_emn.render
page_10_ogn = class_10_ogn.render
page_11_emn = class_11_emn.render
page_11_ogn = class_11_ogn.render

# =====================================================================
# ПОСТРОЕНИЕ НАВИГАЦИИ (исправленная версия)
# =====================================================================
try:
    pg = st.navigation({
        "Информационная панель": [
            st.Page(page_main, title="Главная панель наставника", icon="🏠", url_pathname="main"),
        ],
        "Среднее звено (5-9 классы)": [
            st.Page(page_5, title="Математика — 5 класс", icon="✏️", url_pathname="class_5"),
            st.Page(page_6, title="Математика — 6 класс", icon="✏️", url_pathname="class_6"),
            st.Page(page_7, title="Алгебра / Геометрия — 7 класс", icon="📐", url_pathname="class_7"),
            st.Page(page_8, title="Алгебра / Геометрия — 8 класс", icon="📐", url_pathname="class_8"),
            st.Page(page_9, title="Алгебра / Геометрия — 9 класс", icon="📐", url_pathname="class_9"),
        ],
        "Старшая школа (ЕМН / ОГН)": [
            st.Page(page_10_emn, title="10 класс (ЕМН)", icon="🏛️", url_pathname="class_10_emn"),
            st.Page(page_10_ogn, title="10 класс (ОГН)", icon="📜", url_pathname="class_10_ogn"),
            st.Page(page_11_emn, title="11 класс (ЕМН)", icon="🏛️", url_pathname="class_11_emn"),
            st.Page(page_11_ogn, title="11 класс (ОГН)", icon="📜", url_pathname="class_11_ogn"),
        ]
    })
    
    pg.run()
    
except Exception as e:
    st.error(f"🚨 Критическая ошибка при построении навигации: {e}")
    st.stop()
