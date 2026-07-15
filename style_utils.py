import streamlit as st

def apply_school_style():
    st.markdown(
        """
        <style>
        /* === 1. ГЛОБАЛЬНЫЙ ШКОЛЬНЫЙ ИНТЕРФЕЙС (ЭКРАН) === */
        
        /* Боковая панель управления (Сайдбар) */
        [data-testid="stSidebar"] {
            background-color: #f8fafc !important;
            border-right: 3px solid #3b82f6 !important;
        }
        
        /* Текст и метки в сайдбаре */
        [data-testid="stSidebar"] .stSelectbox label, 
        [data-testid="stSidebar"] .stMultiSelect label,
        [data-testid="stSidebar"] .stSlider label,
        [data-testid="stSidebar"] .stNumberInput label {
            color: #1e3a8a !important;
            font-weight: 700 !important;
            font-size: 11pt !important;
        }
        
        /* Главный фон сайта */
        .main {
            background-color: #f1f5f9 !important;
        }
        
        /* Главные заголовки страниц */
        h1 {
            color: #1e3a8a !important;
            font-weight: 800 !important;
            border-bottom: 3px solid #f97316 !important;
            padding-bottom: 12px !important;
            margin-bottom: 25px !important;
        }

        /* === 2. СТИЛИЗАЦИЯ КАРТОЧЕК ОЦЕНИВАНИЯ === */

        /* Главный синий контейнер карточки варианта */
        .vzaimo-card { 
            border: 2px solid #3b82f6; 
            padding: 30px; 
            border-radius: 12px; 
            margin-bottom: 35px; 
            background-color: #ffffff;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.1);
        }
        
        /* Крупные структурированные заголовки внутри бланка */
        .vzaimo-card h2 {
            color: #1e3a8a !important;
            font-size: 20pt !important;
            font-weight: 700 !important;
            border-bottom: 2px solid #3b82f6 !important;
            padding-bottom: 10px !important;
            margin-top: 0px !important;
        }
        
        .vzaimo-card h3 {
            color: #2563eb !important;
            font-size: 15pt !important;
            font-weight: 600 !important;
            margin-top: 25px !important;
            margin-bottom: 15px !important;
            border: none !important;
        }

        /* Зеленый блок спецификации и ЦО (Лампочка) */
        .spec-block {
            background-color: #f0fdf4 !important;
            padding: 18px !important;
            border-left: 6px solid #10b981 !important;
            font-size: 11pt !important;
            margin-bottom: 25px !important;
            border-radius: 0 8px 8px 0 !important;
            color: #14532d !important;
        }
        .spec-block::before {
            content: "💡 ";
            font-size: 13pt;
        }
        
        /* Список задач с иконкой карандаша */
        .tasks-list {
            padding-left: 0px;
            list-style-type: none; 
            counter-reset: task-counter;
        }
        .tasks-list li {
            position: relative;
            margin-bottom: 20px !important;
            font-size: 12pt;
            line-height: 1.6;
            color: #1f2937;
            padding-left: 35px;
        }
        .tasks-list li::before {
            counter-increment: task-counter;
            content: counter(task-counter) " ✏️";
            position: absolute;
            left: 0;
            top: 2px;
            color: #3b82f6;
            font-weight: 700;
            font-size: 11pt;
        }
        
        /* Таблица критериев (Галочки и четкие рамки) */
        table { 
            width: 100%; 
            border-collapse: collapse; 
            margin-top: 15px; 
            margin-bottom: 25px; 
            background-color: #ffffff;
        }
        table th, table td { 
            border: 1px solid #cbd5e1 !important; 
            padding: 10px 12px !important; 
            text-align: left !important; 
            font-size: 10.5pt !important; 
            color: #1f2937 !important;
        }
        table th { 
            background-color: #eff6ff !important; 
            color: #1e40af !important;
            font-weight: 600 !important; 
        }
        
        /* Оранжевый блок ответов и ключей (Книга) */
        .answers-block {
            background-color: #fff7ed !important;
            padding: 18px !important;
            border-left: 6px solid #f97316 !important;
            border-radius: 0 8px 8px 0 !important;
            color: #7c2d12 !important;
            margin-top: 25px !important;
            font-size: 11pt !important;
        }
        .answers-block-title::before {
            content: "📚 ";
        }

        /* === 3. СТРОГИЕ ПРАВИЛА ДЛЯ ПЕЧАТИ (А4, Ctrl + P) === */
        @media print {
            header, [data-testid="stSidebar"], .stButton, footer, iframe, .stAlert {
                display: none !important;
            }
            .main {
                background-color: #ffffff !important;
            }
            .main .block-container {
                padding: 0px !important;
                margin: 0px !important;
                max-width: 100% !important;
            }
            .vzaimo-card { 
                border: none !important; 
                box-shadow: none !important; 
                background: #ffffff !important;
                padding: 0px !important;
                margin-bottom: 0px !important; 
                page-break-after: always !important; 
            }
            .spec-block {
                border-left: 3px solid #000000 !important;
                background-color: #ffffff !important;
                color: #000000 !important;
                padding: 10px 0px !important;
            }
            .answers-block {
                border-left: 3px solid #000000 !important;
                background-color: #ffffff !important;
                color: #000000 !important;
                padding: 10px 0px !important;
                page-break-inside: avoid !important; 
            }
            .vzaimo-card h2 {
                color: #000000 !important;
                border-bottom: 1px solid #000000 !important;
                font-size: 18pt !important;
            }
            .vzaimo-card h3 {
                color: #000000 !important;
                font-size: 14pt !important;
            }
            table th {
                background-color: #f1f5f9 !important;
                color: #000000 !important;
            }
            table th, table td {
                border: 1px solid #000000 !important;
                color: #000000 !important;
            }
            .tasks-list li::before {
                content: counter(task-counter) ". ";
                color: #000000 !important;
            }
            .spec-block::before, .answers-block-title::before {
                content: "" !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
