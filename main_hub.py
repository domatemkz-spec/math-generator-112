# main_hub.py
import streamlit as st
from style_utils import apply_custom_styles, render_sidebar_logo, render_info_cards, render_footer

# Настройка страницы
st.set_page_config(
    page_title="📚 ИИ-Генератор СОР/СОЧ по математике",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Инициализация session_state
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""

# Применение стилей
apply_custom_styles()

# Подключение MathJax
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

# Боковая панель
render_sidebar_logo()

# Список классов
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

# Основная область
# Заголовок
st.markdown("""
<div style="text-align: center; padding: 20px 0 10px 0;">
    <h1 class="main-title">📚 Генератор учебных материалов</h1>
    <p class="main-subtitle">✨ 5-11 классы • ГОСО РК • С Искусственным Интеллектом</p>
</div>
""", unsafe_allow_html=True)

# Информационные карточки
render_info_cards()

st.markdown("---")

# Загрузка модуля для выбранного класса
module_name = CLASSES[selected_class]

try:
    # Импортируем модуль
    module = __import__(module_name)
    
    # Проверяем наличие функции render
    if hasattr(module, 'render'):
        # Вызываем рендер модуля
        module.render()
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
        </div>
        """, unsafe_allow_html=True)
        
except ImportError as e:
    st.error(f"❌ Ошибка загрузки модуля: {e}")
    st.info(f"💡 Создайте файл {module_name}.py с функцией render()")

# Футер
render_footer()
