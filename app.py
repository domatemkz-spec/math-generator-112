import streamlit as st

# Глобальная настройка платформы (запускается один раз для всего сайта)
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
# ПОСТРОЕНИЕ НАВИГАЦИИ (исправленная версия)
# =====================================================================
try:
    pg = st.navigation({
        "Информационная панель": [
            st.Page(main_hub.render, title="Главная панель наставника", icon="🏠"),
        ],
        "Среднее звено (5-9 классы)": [
            st.Page(class_5.render, title="Математика — 5 класс", icon="✏️"),
            st.Page(class_6.render, title="Математика — 6 класс", icon="✏️"),
            st.Page(class_7.render, title="Алгебра / Геометрия — 7 класс", icon="📐"),
            st.Page(class_8.render, title="Алгебра / Геометрия — 8 класс", icon="📐"),
            st.Page(class_9.render, title="Алгебра / Геометрия — 9 класс", icon="📐"),
        ],
        "Старшая школа (ЕМН / ОГН)": [
            st.Page(class_10_emn.render, title="10 класс (ЕМН)", icon="🏛️"),
            st.Page(class_10_ogn.render, title="10 класс (ОГН)", icon="📜"),
            st.Page(class_11_emn.render, title="11 класс (ЕМН)", icon="🏛️"),
            st.Page(class_11_ogn.render, title="11 класс (ОГН)", icon="📜"),
        ]
    })
    
    pg.run()
    
except Exception as e:
    st.error(f"🚨 Критическая ошибка при построении навигации: {e}")
    st.stop()
