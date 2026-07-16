import streamlit as st
import importlib
import sys
import os

# Импортируем утилиты стилей
from style_utils import apply_school_style, render_sidebar_logo, render_info_cards, render_footer

# =====================================================================
# НАСТРОЙКА СТРАНИЦЫ (set_page_config уже в app.py)
# =====================================================================

# Инициализация session_state
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""

# Применяем единый школьный дизайн (ВСЕ СТИЛИ ЗДЕСЬ!)
apply_school_style()

# =====================================================================
# ПОДКЛЮЧЕНИЕ MATHJAX (ТОЛЬКО ОДИН РАЗ!)
# =====================================================================
if "mathjax_loaded" not in st.session_state:
    st.markdown("""
    <script>
    window.MathJax = {
        tex: { 
            inlineMath: [['$', '$']], 
            displayMath: [['$$', '$$']],
            processEscapes: true 
        },
        svg: {
            fontCache: 'global'
        }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
    </script>
    """, unsafe_allow_html=True)
    st.session_state.mathjax_loaded = True

# =====================================================================
# БОКОВАЯ ПАНЕЛЬ (используем утилиту)
# =====================================================================
render_sidebar_logo()

# =====================================================================
# КЛАССЫ - СЛОВАРЬ ДЛЯ НАВИГАЦИИ
# =====================================================================
CLASSES = {
    "5 класс": "class_5",
    "6 класс": "class_6",
    "7 класс": "class_7",
    "8 класс": "class_8",
    "9 класс": "class_9",
    "10 класс (ЕМН)": "class_10_emn",
    "10 класс (ОГН)": "class_10_ogn",
    "11 класс (ЕМН)": "class_11_emn",
    "11 класс (ОГН)": "class_11_ogn"
}

st.sidebar.markdown("### 📖 Выберите класс")
selected_class = st.sidebar.selectbox("Класс:", list(CLASSES.keys()), index=0)

st.sidebar.markdown("---")
st.sidebar.info(f"💡 Выбран класс: **{selected_class}**")

# =====================================================================
# ОСНОВНАЯ ОБЛАСТЬ
# =====================================================================

# Заголовок
st.markdown("""
<div style="text-align: center; padding: 20px 0 10px 0;">
    <h1 class="main-title">📚 Генератор учебных материалов</h1>
    <p class="main-subtitle">✨ 5-11 классы • ГОСО РК • С Искусственным Интеллектом</p>
</div>
""", unsafe_allow_html=True)

# Информационные карточки (используем утилиту)
render_info_cards()

st.markdown("---")

# =====================================================================
# ЗАГРУЗКА МОДУЛЯ ДЛЯ ВЫБРАННОГО КЛАССА
# =====================================================================
module_name = CLASSES[selected_class]

try:
    # Используем importlib для динамической загрузки
    module = importlib.import_module(module_name)
    
    # Проверяем наличие функции render
    if hasattr(module, 'render'):
        try:
            # Вызываем рендер модуля с обработкой ошибок
            module.render()
        except Exception as render_error:
            st.error(f"❌ Ошибка в модуле {module_name}: {str(render_error)}")
            st.info("Пожалуйста, проверьте код модуля.")
    else:
        st.warning(f"⚠️ Модуль {module_name} не содержит функцию render()")
        
        # Показываем заглушку
        st.markdown(f"""
        <div style="text-align: center; padding: 40px 20px; background: white; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <span style="font-size: 3rem;">🚧</span>
            <h3 style="color: #475569; margin-top: 20px;">Модуль в разработке</h3>
            <p style="color: #94a3b8; font-size: 1.1rem;">
                Для класса <b>{selected_class}</b> модуль будет доступен в ближайшее время
            </p>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Файл: <code>{module_name}.py</code>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
except ImportError as e:
    st.error(f"❌ Ошибка загрузки модуля: {e}")
    st.info(f"💡 Создайте файл `{module_name}.py` с функцией `render()`")
    
    # Показываем пример кода
    with st.expander("📖 Как создать модуль для класса"):
        st.code(f"""
# {module_name}.py
import streamlit as st

def render():
    st.markdown("## 📚 {selected_class}")
    st.info("🚧 Модуль для {selected_class} в разработке")
    
    # Добавьте здесь логику генерации заданий
""", language="python")
except Exception as e:
    st.error(f"❌ Непредвиденная ошибка при загрузке модуля: {e}")

# =====================================================================
# ФУТЕР (используем утилиту)
# =====================================================================
render_footer()
