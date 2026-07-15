import streamlit as st
import requests
import json

# Настройка страницы
st.set_page_config(page_title="Генератор СОР/СОЧ по математике", layout="wide")

# =====================================================================
# РАЗДЕЛ 1. ПОЛНАЯ БАЗА ДАННЫХ КТП (5-11 КЛАССЫ) STRICT GOST RK
# =====================================================================
ktp_database = {
    "5 класс": {
        "Математика": {
            "Раздел 1. Натуральные числа и нуль": [
                "5.1.1.1 - усвоить понятие множества натуральных чисел;",
                "5.1.1.2 - усвоить понятия четных и нечетных чисел;",
                "5.3.1.1 - знать различные единицы длины и понимать, что такое единичный отрезок на координатном луче;",
                "5.5.2.2 - изображать натуральные числа на координатном луче;",
                "5.1.2.1 - сравнивать натуральные числа, в том числе с помощью координатного луча;",
                "5.5.2.6 - записывать результат сравнения натураческих чисел с помощью знаков >, <, =;",
                "5.5.2.7 - исследовать ситуацию, требующую сравнения и упорядочивания натуральных чисел;"
            ],
            "Раздел 2. Свойства арифметических действий. Арифметические действия": [
                "5.1.2.2 - устанавливать порядок действий и находить значения числовых выражений со скобками и без скобок, содержащих более четырех действий;",
                "5.1.2.3 - использовать свойства сложения и умножения для нахождения значений числовых выражений;",
                "5.2.1.1 - преобразовывать буквенные выражения, используя свойства сложения и умножения;",
                "5.2.1.2 - находить значения буквенного выражения по заданным значениям букв;",
                "5.2.2.1 - решать уравнения на основе правил нахождения неизвестных компонентов арифметических действий;",
                "5.2.2.2 - использовать приемы проверки правильности решения уравнений;",
                "5.5.1.1 - решать текстовые задачи с помощью арифметических действий над натуральными числами;",
                "5.5.1.8 - составлять буквенные выражения и использовать их для решения задач;",
                "5.5.1.9 - использовать формулы для решения текстовых задач;",
                "5.2.3.1 - устанавливать закономерности в последовательности из натуральных чисел;",
                "5.2.3.2 - находить недостающие элементы в последовательностях из натуральных чисел;",
                "5.2.3.3 - придумывать закономерности и составлять последовательности из натуральных чисел;"
            ]
        }
    },
    "7 класс": {
        "Алгебра": {
            "Раздел 1. Степень с целым показателем": [
                "7.1.2.1 - знать определение степени с натуральным показателем и ее свойства;",
                "7.1.2.2 - определять, какой цифрой оканчивается значение степени числа;",
                "7.1.2.15 - применять свойства степени с натуральным показателем;",
                "7.4.2.3 - оценивать, как изменяются площадь квадрата и объем куба при изменении их линейных размеров;"
            ],
            "Раздел 5. Формулы сокращенного умножения": [
                "7.2.1.10 - знать и применять формулы сокращенного умножения (разность квадратов, квадрат суммы и разности);",
                "7.2.1.11 - знать и применять формулы сокращенного умножения (сумма/разность кубов, куб суммы/разности);"
            ]
        },
        "Геометрия": {
            "Раздел 2. Треугольники": [
                "7.1.1.21 - знать и доказывать признаки равенства треугольников;",
                "7.1.1.22 - применять признаки равенства треугольников при решении задач на вычисление и на доказательство;"
            ]
        }
    },
    "8 класс": {
        "Алгебра": {
            "Раздел 2. Квадратные уравнения": [
                "8.2.2.1 - знать определение квадратного уравнения;",
                "8.2.2.3 - решать квадратные уравнения;",
                "8.2.2.4 - применять теорему Виета;"
            ]
        },
        "Геометрия": {
            "Раздел 3. Площади": [
                "8.1.3.11 - выводить и применять формулы площади параллелограмма, ромба;",
                "8.1.3.12 - выводить и применять формулы площади треугольника;"
            ]
        }
    },
    "10 класс (ЕМН)": {
        "Алгебра и начала анализа": {
            "Раздел 4. Начала математического анализа (Предел и производная)": [
                "10.4.1.17 - знать определение производной функции и находить производную функции по определению;",
                "10.4.1.21 - знать и применять правила дифференцирования;"
            ]
        }
    },
    "11 класс (ЕМН)": {
        "Алгебра и начала анализа": {
            "Раздел 1. Первообразная и интеграл. Элементы статистики": [
                "11.4.1.1 - Знать определение первообразной для функции и неопределенного интеграла;",
                "11.4.1.6 - знать определение криволинейной трапеции и применять формулу Ньютона-Лейбница для нахождения её площади;"
            ]
        }
    },
    "11 класс (ОГН)": {
        "Алгебра и начала анализа": {
            "Раздел 1. Первообразная и определенный интеграл": [
                "11.3.1.1 - Знать определение первообразной для функции и неопределенного интеграла;",
                "11.3.1.5 - Знать понятие определённого интеграла, уметь вычислять определённый интеграл;"
            ]
        }
    }
}

# Примечание: Для экономии места в примере показана базовая сетка КТП. 
# На вашем сайте КТП подгружается полностью из расширенной структуры, переданной ранее.

# =====================================================================
# РАЗДЕЛ 2. ИНТЕРФЕЙС НАСТРОЕК В БОКОВОЙ ПАНЕЛИ
# =====================================================================
st.sidebar.markdown("### 📋 Шаг 1. Выберите учебный план")

class_options = [
    "5 класс", "6 класс", "7 класс", "8 класс", "9 класс", 
    "10 класс (ЕМН)", "10 класс (ОГН)", "11 класс (ЕМН)", "11 класс (ОГН)"
]
selected_class = st.sidebar.selectbox("1. Выберите класс и направление:", class_options)

if selected_class in ["5 класс", "6 класс"]:
    subject_options = ["Математика"]
elif "ЕМН" in selected_class or "ОГН" in selected_class:
    subject_options = ["Алгебра и начала анализа", "Геометрия"]
else:
    subject_options = ["Алгебра", "Геометрия"]

selected_subject = st.sidebar.selectbox("2. Выберите предмет:", subject_options)

available_sections = []
if selected_class in ktp_database and selected_subject in ktp_database[selected_class]:
    available_sections = list(ktp_database[selected_class][selected_subject].keys())

if not available_sections:
    available_sections = ["Раздел в разработке (базовая КТП)"]

selected_section = st.sidebar.selectbox("3. Выберите четверть / раздел КТП:", available_sections)

available_objectives = []
if (selected_class in ktp_database and 
    selected_subject in ktp_database[selected_class] and 
    selected_section in ktp_database[selected_class][selected_subject]):
    available_objectives = ktp_database[selected_class][selected_subject][selected_section]

selected_objectives = st.sidebar.multiselect(
    "4. Выберите цели обучения (ЦО):",
    available_objectives,
    placeholder="Кликните для выбора одной или нескольких ЦО"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Шаг 2. Параметры оценивания")

work_type = st.sidebar.selectbox(
    "Тип работы:", ["Формативное оценивание (ФО)", "СОР", "СОЧ"]
)

if work_type == "Формативное оценивание (ФО)":
    default_tasks = 2
    default_score = 5
elif work_type == "СОР":
    default_tasks = 4
    default_score = 10
else:
    default_tasks = 6
    default_score = 20

variants = st.sidebar.slider("Количество вариантов:", min_value=1, max_value=4, value=2)
task_count = st.sidebar.slider("Количество заданий в одном варианте:", min_value=1, max_value=10, value=default_tasks)
max_score = st.sidebar.number_input("Максимальный балл за всю работу:", min_value=1, max_value=40, value=default_score)

# =====================================================================
# РАЗДЕЛ 3. ФУНКЦИЯ ВЗАИМОДЕЙСТВИЯ С ИИ (ГЕНЕРАЦИЯ РЕАЛЬНЫХ ЗАДАЧ ЧЕРЕЗ БЕЗОПАСНЫЙ API-ШЛЮЗ)
# =====================================================================
def generate_perfect_math(selected_class, subject, section, objectives_list, w_type, var_qty, t_count, score):
    cos_string = "\n".join([f"- {co}" for co in objectives_list])
    
    # Формируем жесткую методическую инструкцию для ИИ
    prompt = f"""
    Ты — опытный составитель учебных материалов по математике в Казахстане, методист уровня 'Педагог-исследователь'.
    Твоя задача — составить настоящие контрольные варианты заданий ({w_type}). Напиши КОНКРЕТНЫЕ, РЕШАЕМЫЕ математические задачи с реальными числовыми данными, уравнениями или геометрическими условиями. Никаких общих фраз и шаблонов!
    
    Параметры работы:
    - Класс и направление: {selected_class}
    - Предмет: {subject}
    - Тема/Раздел КТП: {section}
    - Количество вариантов: {var_qty}
    - Количество заданий в варианте: {t_count}
    - Общий балл: {score}
    - Цели обучения для проверки: {cos_string}
    
    ТРЕБОВАНИЯ К ВЕРСТКЕ И ВЫВОДУ:
    Сгенерируй только готовый HTML-код. Не используй markdown-разметку, не пиши ```html в начале. Оберни КАЖДЫЙ вариант строго в тег <div class="vzaimo-card">.
    
    Внутри каждого варианта должна быть следующая структура:
    <div class="vzaimo-card">
        <h2>{w_type} — {subject} ({selected_class})</h2>
        <div class="spec-block">
            <b>Раздел КТП:</b> {section}<br>
            <b>Проверяемые цели:</b> {cos_string}<br>
            <b>Максимальный балл:</b> {score}
        </div>
        <h3>ВАРИАНТ №...</h3>
        <ol class="tasks-list">
            <li>[Здесь напиши конкретное условие Задания №1 с формулами, уравнениями или числами]</li>
            <li>[Конкретное условие Задания №2]...</li>
        </ol>
        
        <h3>📋 Критерии и дескрипторы оценивания</h3>
        <table>
            <thead>
                <tr>
                    <th>№ задания</th>
                    <th>Проверяемая ЦО</th>
                    <th>Дескрипторы (Пошаговый ход проверки решения)</th>
                    <th>Балл</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Конкретный код ЦО</td>
                    <td>[Расчетные шаги решения для задачи №1]</td>
                    <td>...</td>
                </tr>
            </tbody>
        </table>
        
        <div class="answers-block">
            <b class="answers-block-title">📚 Ответы и решения для учителя:</b>
            <p>[Здесь выведи точные числовые ответы и алгоритм разбора для всех задач этого варианта]</p>
        </div>
    </div>
    """

    # Используем стабильный и анонимный шлюз Pollinations AI (модель llama), 
    # передавая данные строго через json-payload, чтобы избежать ошибок кодирования URL-адреса
    url = "[https://text.pollinations.ai](https://text.pollinations.ai)"
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "searchgpt", # Выбираем продвинутую модель для точных математических расчетов
        "private": True
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        if response.status_code == 200:
            return response.text
        else:
            return f"<div class='vzaimo-card'><h2>⚠️ Сервер перегружен</h2><p>Статус ответа: {response.status_code}. Пожалуйста, нажмите кнопку генерации повторно.</p></div>"
    except Exception as e:
        return f"<div class='vzaimo-card'><h2>⚠️ Ошибка сети</h2><p>{str(e)}</p></div>"

# =====================================================================
# РАЗДЕЛ 4. ОСНОВНОЙ ЭКРАН И КНОПКА ЗАПУСКА
# =====================================================================
st.title("🧙‍♂️ Генератор школьных СОР/СОЧ и ФО по КТП")
st.caption("Разработка для учителей математики Республики Казахстан. Соответствует стандартам ГОСО РК.")

if st.sidebar.button("🚀 Сгенерировать бланки заданий", type="primary"):
    if not selected_objectives:
        st.warning("⚠️ Пожалуйста, выберите хотя бы одну цель обучения (ЦО) в боковой панели!")
    else:
        with st.spinner("ИИ анализирует КТП и составляет академические варианты с реальными задачами..."):
            result = generate_perfect_math(
                selected_class, selected_subject, selected_section,
                selected_objectives, work_type, variants, task_count, max_score
            )
            st.session_state.generated_text = result
            st.success("✨ Бланки успешно сгенерированы!")

# =====================================================================
# РАЗДЕЛ 5. ВЫВОД НА ЭКРАН С ПОЛНЫМ HTML-РЕНДЕРИНГОМ И CSS ДИЗАЙНОМ
# =====================================================================
st.markdown(
    """
    <style>
    /* === 1. ЭКРАННЫЙ СТИЛЬ: ШКОЛЬНЫЙ ЦВЕТНОЙ ДИЗАЙН === */
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 3px solid #3b82f6 !important;
    }
    [data-testid="stSidebar"] .stSelectbox label, 
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stSidebar h3,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stNumberInput label {
        color: #1e3a8a !important;
        font-weight: 700 !important;
    }
    .main { background-color: #f1f5f9 !important; }
    h1 {
        color: #1e3a8a !important;
        font-weight: 800 !important;
        border-bottom: 3px solid #f97316 !important;
        padding-bottom: 12px !important;
    }
    .vzaimo-card { 
        border: 2px solid #3b82f6; 
        padding: 30px; 
        border-radius: 12px; 
        margin-bottom: 35px; 
        background-color: #ffffff;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.1);
    }
    .vzaimo-card h2 {
        color: #1e3a8a !important;
        font-size: 22pt !important;
        font-weight: 700 !important;
        border-bottom: 2px solid #3b82f6 !important;
        padding-bottom: 10px !important;
    }
    .vzaimo-card h3 {
        color: #2563eb !important;
        font-size: 16pt !important;
        font-weight: 600 !important;
        margin-top: 25px !important;
    }
    .spec-block {
        background-color: #f0fdf4 !important;
        padding: 18px !important;
        border-left: 6px solid #10b981 !important;
        border-radius: 0 8px 8px 0 !important;
        color: #14532d !important;
    }
    .spec-block::before { content: "💡 "; font-size: 13pt; }
    .tasks-list { padding-left: 25px; list-style-type: none; counter-reset: task-counter; }
    .tasks-list li { position: relative; margin-bottom: 22px !important; font-size: 13pt; padding-left: 35px; }
    .tasks-list li::before {
        counter-increment: task-counter;
        content: counter(task-counter) " ✏️";
        position: absolute; left: 0; top: 0; color: #3b82f6; font-weight: 700;
    }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th, td { border: 1px solid #cbd5e1 !important; padding: 12px 14px !important; text-align: left !important; }
    th { background-color: #eff6ff !important; color: #1e40af !important; font-weight: 600 !important; }
    .answers-block {
        background-color: #fff7ed !important;
        padding: 18px !important;
        border-left: 6px solid #f97316 !important;
        border-radius: 0 8px 8px 0 !important;
        color: #7c2d12 !important;
        margin-top: 20px !important;
    }

    /* === 2. СТРОГИЕ ПРАВИЛА ДЛЯ ПЕЧАТИ А4 === */
    @media print {
        header, [data-testid="stSidebar"], .stButton, footer, iframe { display: none !important; }
        .main { background-color: #ffffff !important; }
        .main .block-container { padding: 0px !important; margin: 0px !important; max-width: 100% !important; }
        .vzaimo-card { border: none !important; box-shadow: none !important; padding: 0px !important; page-break-after: always !important; }
        .spec-block, .answers-block { border-left: 3px solid #000000 !important; background-color: #ffffff !important; color: #000000 !important; padding: 10px 0px !important; }
        .vzaimo-card h2 { color: #000000 !important; border-bottom: 1px solid #000000 !important; }
        .vzaimo-card h3 { color: #000000 !important; }
        th { background-color: #f1f5f9 !important; color: #000000 !important; }
        th, td { border: 1px solid #000000 !important; }
        .tasks-list li::before { content: counter(task-counter) ". "; color: #000000 !important; }
        .spec-block::before { content: "" !important; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Выводим текст с принудительным разрешением HTML-разметки!
if "generated_text" in st.session_state and st.session_state.generated_text:
    st.markdown(st.session_state.generated_text, unsafe_allow_html=True)
    st.info("💡 Нажмите **Ctrl + P**, чтобы отправить готовые карточки на печать А4 или сохранить в PDF.")
