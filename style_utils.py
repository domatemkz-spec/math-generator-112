# style_utils.py
import streamlit as st

def apply_custom_styles():
    """Применение пользовательских CSS стилей"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Comfortaa', sans-serif !important;
    }
    
    .main {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    }
    
    .main-title {
        font-size: 2.8rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px !important;
    }
    
    .main-subtitle {
        font-size: 1.2rem !important;
        color: #475569 !important;
        font-weight: 400 !important;
        border-bottom: 3px solid #f59e0b;
        padding-bottom: 12px !important;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
        border-right: 4px solid #3b82f6 !important;
        padding-top: 20px !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stNumberInput label {
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    .vzaimo-card {
        background: #ffffff !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin-bottom: 30px !important;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.12) !important;
        border: none !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .vzaimo-card::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 6px !important;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #f59e0b) !important;
    }
    
    .vzaimo-card h2 {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #1e293b !important;
        margin-bottom: 15px !important;
    }
    
    .vzaimo-card h3 {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: #3b82f6 !important;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
        border-bottom: 2px solid #e2e8f0 !important;
        padding-bottom: 8px !important;
    }
    
    .spec-block {
        background: linear-gradient(135deg, #eff6ff, #dbeafe) !important;
        padding: 20px !important;
        border-radius: 16px !important;
        border-left: 6px solid #3b82f6 !important;
        margin-bottom: 25px !important;
    }
    
    .spec-block ul {
        margin: 10px 0 0 20px !important;
        padding: 0 !important;
    }
    
    .spec-block ul li {
        color: #1e293b !important;
        margin-bottom: 6px !important;
        font-size: 0.95rem !important;
    }
    
    .tasks-list {
        padding: 0 !important;
        list-style-type: none !important;
        counter-reset: task-counter !important;
    }
    
    .tasks-list li {
        position: relative !important;
        padding: 18px 20px 18px 55px !important;
        margin-bottom: 15px !important;
        background: #f8fafc !important;
        border-radius: 14px !important;
        border-left: 4px solid #8b5cf6 !important;
        transition: all 0.2s ease !important;
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }
    
    .tasks-list li::before {
        counter-increment: task-counter !important;
        content: counter(task-counter) !important;
        position: absolute !important;
        left: 12px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        background: linear-gradient(135deg, #8b5cf6, #7c3aed) !important;
        color: #ffffff !important;
        width: 32px !important;
        height: 32px !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
    }
    
    .tasks-list li small {
        color: #64748b !important;
        font-size: 0.85rem !important;
        display: block !important;
        margin-top: 5px !important;
    }
    
    table {
        width: 100% !important;
        border-collapse: separate !important;
        border-spacing: 0 !important;
        margin-top: 20px !important;
        margin-bottom: 25px !important;
        background: #ffffff !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }
    
    th {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        padding: 14px 16px !important;
        text-transform: uppercase !important;
        font-size: 0.9rem !important;
        text-align: left !important;
    }
    
    td {
        border-bottom: 1px solid #e2e8f0 !important;
        padding: 14px 16px !important;
        color: #1e293b !important;
        text-align: left !important;
    }
    
    tr:last-child td {
        border-bottom: none !important;
    }
    
    tr:hover td {
        background: #f8fafc !important;
    }
    
    .answers-block {
        background: linear-gradient(135deg, #fef3c7, #fde68a) !important;
        padding: 20px !important;
        border-radius: 16px !important;
        border-left: 6px solid #f59e0b !important;
        margin-top: 25px !important;
    }
    
    .answers-block b {
        color: #92400e !important;
    }
    
    .answers-block p {
        color: #78350f !important;
        margin: 8px 0 0 0 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 12px 28px !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.45) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    @media print {
        header, [data-testid="stSidebar"], .stButton, footer, iframe, .stAlert, .stSpinner {
            display: none !important;
        }
        
        .main {
            background: #ffffff !important;
        }
        
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
        }
        
        .vzaimo-card {
            box-shadow: none !important;
            border-radius: 0px !important;
            background: #ffffff !important;
            padding: 20px !important;
            margin-bottom: 0px !important;
            page-break-after: always !important;
            border: 1px solid #e2e8f0 !important;
        }
        
        .vzaimo-card::before {
            display: none !important;
        }
        
        .spec-block {
            background: #f8fafc !important;
            border-left: 4px solid #1e293b !important;
        }
        
        .answers-block {
            background: #fef3c7 !important;
            border-left: 4px solid #92400e !important;
        }
        
        .tasks-list li {
            background: #f8fafc !important;
            border-left: 4px solid #8b5cf6 !important;
        }
        
        .tasks-list li::before {
            background: #8b5cf6 !important;
        }
        
        th {
            background: #1e293b !important;
            color: #ffffff !important;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
    }
    
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem !important;
        }
        
        .vzaimo-card {
            padding: 20px !important;
        }
        
        .vzaimo-card h2 {
            font-size: 1.4rem !important;
        }
        
        .tasks-list li {
            padding: 15px 15px 15px 50px !important;
            font-size: 0.95rem !important;
        }
        
        .tasks-list li::before {
            width: 28px !important;
            height: 28px !important;
            left: 10px !important;
            font-size: 0.8rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_sidebar_logo():
    """Отрисовка логотипа в сайдбаре"""
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 15px 0; background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 16px; margin-bottom: 20px;">
        <span style="font-size: 2.5rem;">📚</span>
        <h3 style="color: white; margin: 0;">Генератор</h3>
        <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.85rem;">СОР / СОЧ / ФО</p>
    </div>
    """, unsafe_allow_html=True)

def render_info_cards():
    """Отрисовка информационных карточек"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3b82f6, #2563eb); padding: 20px; border-radius: 16px; color: white; text-align: center;">
            <span style="font-size: 2.5rem;">📖</span>
            <h5 style="color: white; margin: 10px 0 5px 0;">Полная база КТП</h5>
            <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.85rem;">5-11 классы</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); padding: 20px; border-radius: 16px; color: white; text-align: center;">
            <span style="font-size: 2.5rem;">🤖</span>
            <h5 style="color: white; margin: 10px 0 5px 0;">ИИ-генерация</h5>
            <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.85rem;">Уникальные задания</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f59e0b, #d97706); padding: 20px; border-radius: 16px; color: white; text-align: center;">
            <span style="font-size: 2.5rem;">📊</span>
            <h5 style="color: white; margin: 10px 0 5px 0;">Авто-оценивание</h5>
            <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.85rem;">Рубрики + баллы</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981, #059669); padding: 20px; border-radius: 16px; color: white; text-align: center;">
            <span style="font-size: 2.5rem;">🖨️</span>
            <h5 style="color: white; margin: 10px 0 5px 0;">Готово к печати</h5>
            <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.85rem;">Формат A4</p>
        </div>
        """, unsafe_allow_html=True)

def render_footer():
    """Отрисовка футера"""
    st.markdown("""
    <br>
    <div style="text-align: center; padding: 20px; color: #94a3b8; font-size: 0.85rem;">
        <span>📚 ИИ-Генератор СОР/СОЧ по математике</span>
        <span style="margin: 0 10px;">•</span>
        <span>🇰🇿 Соответствует ГОСО РК</span>
        <span style="margin: 0 10px;">•</span>
        <span>🤖 Работает на ИИ</span>
        <span style="margin: 0 10px;">•</span>
        <span>💡 Для учителей математики</span>
    </div>
    """, unsafe_allow_html=True)
