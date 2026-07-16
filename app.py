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
# СОЗДАЕМ ФУНКЦИИ-ОБЕРТКИ С УНИКАЛЬНЫМИ ИМЕНАМИ
# =====================================================================
def page_main():
    main_hub.render()

def page_class_5():
    class_5.render()

def page_class_6():
    class_6.render()

def page_class_7():
    class_7.render()

def page_class_8():
    class_8.render()

def page_class_9():
    class_9.render()

def page_class_10_emn():
    class_10_emn.render()

def page_class_10_ogn():
    class_10_ogn.render()

def page_class_11_emn():
    class_11_emn.render()

def page_class_11_ogn():
    class_11_ogn.render()

# =====================================================================
# ПОСТРОЕНИЕ НАВИГАЦИИ
# =====================================================================
try:
    pg = st.navigation({
        "Информационная панель": [
            st.Page(page_main, title="Главная панель наставника", icon="🏠"),
        ],
        "Среднее звено (5-9 классы)": [
            st.Page(page_class_5, title="Математика — 5 класс", icon="✏️"),
            st.Page(page_class_6, title="Математика — 6 класс", icon="✏️"),
            st.Page(page_class_7, title="Алгебра / Геометрия — 7 класс", icon="📐"),
            st.Page(page_class_8, title="Алгебра / Геометрия — 8 класс", icon="📐"),
            st.Page(page_class_9, title="Алгебра / Геометрия — 9 класс", icon="📐"),
        ],
        "Старшая школа (ЕМН / ОГН)": [
            st.Page(page_class_10_emn, title="10 класс (ЕМН)", icon="🏛️"),
            st.Page(page_class_10_ogn, title="10 класс (ОГН)", icon="📜"),
            st.Page(page_class_11_emn, title="11 класс (ЕМН)", icon="🏛️"),
            st.Page(page_class_11_ogn, title="11 класс (ОГН)", icon="📜"),
        ]
    })
    
    pg.run()
    
except Exception as e:
    st.error(f"🚨 Критическая ошибка при построении навигации: {e}")
    st.stop()
