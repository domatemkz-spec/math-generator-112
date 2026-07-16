import streamlit as st
import importlib
import sys

# --- 1. НАСТРОЙКА СТРАНИЦЫ ---
st.set_page_config(
    page_title="Панель конструирования КИМ по КТП", 
    page_icon="🏛️",
    layout="wide"
)

# --- 2. ФУНКЦИЯ ДЛЯ БЕЗОПАСНОГО ИМПОРТА СТРАНИЦ ---
def safe_import(page_name):
    """
    Пытается импортировать страницу. Если файл не найден или есть ошибка,
    возвращает заглушку с сообщением об ошибке.
    """
    try:
        # Пытаемся импортировать модуль
        module = importlib.import_module(page_name)
        return module
    except ModuleNotFoundError:
        st.error(f"❌ Файл `{page_name}.py` не найден. Проверьте, что он находится в одной папке с app.py.")
        return None
    except SyntaxError as e:
        st.error(f"❌ Синтаксическая ошибка в файле `{page_name}.py`: {e}")
        return None
    except Exception as e:
        st.error(f"❌ Неизвестная ошибка при загрузке `{page_name}.py`: {e}")
        return None

# --- 3. ОПРЕДЕЛЕНИЕ СТРУКТУРЫ НАВИГАЦИИ С ПРОВЕРКАМИ ---
# Список всех страниц для проверки
pages_to_check = [
    "main_hub", 
    "class_5", "class_6", "class_7", "class_8", "class_9",
    "class_10_emn", "class_10_ogn", "class_11_emn", "class_11_ogn"
]

# Проверяем все страницы при старте (выводим предупреждения, но не останавливаем приложение)
all_pages_exist = True
for page in pages_to_check:
    if safe_import(page) is None:
        all_pages_exist = False
        # st.warning(f"⚠️ Страница `{page}` не загружена. Проверьте файл.")

# --- 4. ПОСТРОЕНИЕ НАВИГАЦИИ ---
# Примечание: st.Page требует, чтобы импортируемый модуль существовал.
# Мы используем конструкцию, которая попытается импортировать страницу,
# но если она не загружена, покажем заглушку.

def create_page_entry(module_name, title, icon):
    """Создает запись страницы для st.Page с обработкой ошибок"""
    try:
        # Пытаемся импортировать модуль
        module = importlib.import_module(module_name)
        # Если модуль загружен, возвращаем st.Page
        return st.Page(module, title=title, icon=icon)
    except Exception as e:
        # Если ошибка, создаем заглушку прямо здесь (но st.Page требует модуль)
        # Поэтому мы создаем временный модуль с функцией-заглушкой
        import types
        stub_module = types.ModuleType(module_name)
        
        def stub_func():
            st.error(f"❌ Страница `{module_name}` не может быть загружена.")
            st.info("Проверьте файл на наличие ошибок.")
            if st.button("🔄 Попробовать перезагрузить"):
                st.rerun()
        
        stub_module.main = stub_func  # Streamlit ищет функцию main() в модуле страницы
        return st.Page(stub_module, title=f"⚠️ {title}", icon="🚫")

# Строим навигацию с проверками
try:
    pg = st.navigation({
        "Информационная панель": [
            create_page_entry("main_hub", "Главная панель наставника", "🏠"),
        ],
        "Среднее звено (5-9 классы)": [
            create_page_entry("class_5", "Математика — 5 класс", "✏️"),
            create_page_entry("class_6", "Математика — 6 класс", "✏️"),
            create_page_entry("class_7", "Алгебра / Геометрия — 7 класс", "📐"),
            create_page_entry("class_8", "Алгебра / Геометрия — 8 класс", "📐"),
            create_page_entry("class_9", "Алгебра / Геометрия — 9 класс", "📐"),
        ],
        "Старшая школа (ЕМН / ОГН)": [
            create_page_entry("class_10_emn", "10 класс (ЕМН)", "🏛️"),
            create_page_entry("class_10_ogn", "10 класс (ОГН)", "📜"),
            create_page_entry("class_11_emn", "11 класс (ЕМН)", "🏛️"),
            create_page_entry("class_11_ogn", "11 класс (ОГН)", "📜"),
        ]
    })
    
    pg.run()
    
except Exception as e:
    st.error(f"🚨 Критическая ошибка при построении навигации: {e}")
    st.stop()
