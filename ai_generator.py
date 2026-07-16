import streamlit as st
import json

# =====================================================================
# ИМПОРТ GEMINI SDK (устанавливается через requirements.txt)
# =====================================================================
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    st.warning("⚠️ Библиотека google-generativeai не установлена. Добавьте ее в requirements.txt")

# =====================================================================
# НАСТРОЙКА API
# =====================================================================

def get_gemini_client():
    """Получение клиента Gemini из Streamlit Secrets"""
    api_key = st.secrets.get("GEMINI_API_KEY", None)
    
    if not api_key:
        return None
    
    try:
        genai.configure(api_key=api_key)
        return genai
    except Exception:
        return None

def has_api_key():
    """Проверка наличия API ключа"""
    return get_gemini_client() is not None

def generate_math_task_gemini(
    grade: int,
    subject: str,
    topic: str,
    learning_objectives: list,
    task_type: str,
    difficulty: str = "medium",
    model_name: str = "gemini-2.0-flash"
) -> dict:
    """Генерация математического задания с помощью Gemini"""
    client = get_gemini_client()
    
    if not client:
        return {
            "task": "❌ API ключ не настроен. Добавьте GEMINI_API_KEY в Secrets.",
            "answer": "Настройте ключ в Streamlit Cloud → Settings → Secrets",
            "error": True
        }
    
    objectives_text = "\n".join([f"- {obj}" for obj in learning_objectives])
    
    prompt = f"""
Ты — опытный учитель математики в Казахстане, работающий по программе ГОСО РК.
Сгенерируй математическое задание для {grade} класса по предмету "{subject}".

Тема раздела: {topic}
Цели обучения (ГОСО РК):
{objectives_text}

Тип работы: {task_type}
Сложность: {difficulty}

Требования:
1. Задание должно точно соответствовать указанным целям обучения
2. Условие должно быть четким, понятным, с реальными числами
3. Используй LaTeX для формул (внутри $...$)
4. Предоставь подробное пошаговое решение и ответ

Формат ответа (строго JSON, без лишнего текста):
{{
    "task": "Условие задачи с формулами в LaTeX",
    "answer": "Подробное пошаговое решение и ответ с формулами в LaTeX",
    "learning_objective": "Код ЦО, которому соответствует задание",
    "points": "Рекомендуемое количество баллов (1-5)"
}}
"""
    
    try:
        model = client.GenerativeModel(
            model_name,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 1000,
            }
        )
        
        response = model.generate_content(prompt)
        response_text = response.text
        
        # Ищем JSON в ответе
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        if start != -1 and end != -1:
            json_str = response_text[start:end]
            result = json.loads(json_str)
        else:
            result = json.loads(response_text)
        
        result["error"] = False
        return result
        
    except json.JSONDecodeError as e:
        return {
            "task": "Ошибка парсинга JSON. Попробуйте еще раз.",
            "answer": str(e),
            "error": True
        }
    except Exception as e:
        return {
            "task": f"Ошибка API: {str(e)}",
            "answer": "Проверьте подключение и попробуйте снова",
            "error": True
        }

def generate_multiple_tasks(
    grade: int,
    subject: str,
    topic: str,
    learning_objectives: list,
    task_type: str,
    variants_count: int,
    tasks_per_variant: int,
    difficulty: str = "medium",
    progress_callback=None,
    model_name: str = "gemini-2.0-flash"
) -> list:
    """Генерация нескольких вариантов заданий через Gemini"""
    all_tasks = []
    total_tasks = variants_count * tasks_per_variant
    completed = 0
    
    for v in range(1, variants_count + 1):
        variant_tasks = []
        
        for t in range(tasks_per_variant):
            objective = learning_objectives[t % len(learning_objectives)]
            
            task = generate_math_task_gemini(
                grade=grade,
                subject=subject,
                topic=topic,
                learning_objectives=[objective],
                task_type=task_type,
                difficulty=difficulty,
                model_name=model_name
            )
            variant_tasks.append(task)
            
            completed += 1
            if progress_callback:
                progress_callback(completed, total_tasks)
        
        all_tasks.append({
            "variant": v,
            "tasks": variant_tasks
        })
    
    return all_tasks

def build_variants_html(all_tasks, work_type, max_score):
    """Построение HTML-кода из сгенерированных заданий"""
    final_html = ""
    
    for variant_data in all_tasks:
        variant_num = variant_data["variant"]
        tasks = variant_data["tasks"]
        
        tasks_list_html = ""
        table_rows_html = ""
        answers_list_html = ""
        
        score_per_task = max(1, max_score // len(tasks))
        
        for idx, task in enumerate(tasks, start=1):
            task_text = task.get("task", "Задание не сгенерировано")
            ans_text = task.get("answer", "Ответ не предоставлен")
            objective = task.get("learning_objective", "ЦО не указан")
            
            tasks_list_html += f"<li>{task_text} <b>({score_per_task} б.)</b></li>"
            
            table_rows_html += f"""
            <tr>
                <td>{idx}</td>
                <td><b>{objective}</b></td>
                <td>- Правильно интерпретирует условие задачи;<br>- Демонстрирует корректный алгоритм решения;<br>- Записывает точный математический ответ.</td>
                <td>{score_per_task}</td>
            </tr>
            """
            answers_list_html += f"<li><b>Задание №{idx} ({objective}):</b> {ans_text}</li>"

        if work_type == "Формативное оценивание (ФО)":
            title = "🎯 ФО"
        elif work_type == "СОР":
            title = "📊 СОР"
        else:
            title = "🏛️ СОЧ"
        
        final_html += f"""
        <div class="vzaimo-card">
            <h2>{title} — Вариант №{variant_num}</h2>
            <div class="spec-block">
                <b>Тип работы:</b> {work_type}<br>
                <b>Максимальный балл:</b> {max_score}
            </div>
            <h3>ЗАДАНИЯ:</h3>
            <ol class="tasks-list">
                {tasks_list_html}
            </ol>
            
            <h3>📋 Спецификация</h3>
            <table>
                <thead>
                    <tr>
                        <th>№</th>
                        <th>ЦО</th>
                        <th>Критерии оценивания</th>
                        <th>Балл</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows_html}
                </tbody>
            </table>
            
            <div class="answers-block">
                <b>📚 Ответы и решения:</b>
                <ul>{answers_list_html}</ul>
            </div>
        </div>
        """
    
    return final_html

def render_ai_settings():
    """Рендеринг настроек API в боковой панели"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🤖 Настройки ИИ")
    
    has_key = has_api_key()
    
    if has_key:
        st.sidebar.success("✅ Gemini API ключ активен")
    else:
        st.sidebar.warning("⚠️ Добавьте GEMINI_API_KEY в Secrets")
        st.sidebar.info("""
        В Streamlit Cloud:
        1. Settings → Secrets
        2. Добавьте: GEMINI_API_KEY = "ваш_ключ"
        """)
    
    # Настройки генерации
    st.sidebar.markdown("#### 🎯 Параметры")
    
    use_ai = st.sidebar.checkbox("🤖 Генерировать ИИ", value=has_key)
    
    difficulty = st.sidebar.selectbox(
        "Сложность:",
        ["easy", "medium", "hard"],
        format_func=lambda x: {
            "easy": "🟢 Легкий",
            "medium": "🟡 Средний",
            "hard": "🔴 Сложный"
        }.get(x, x)
    )
    
    model_name = st.sidebar.selectbox(
        "Модель Gemini:",
        ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-2.5-pro"],
        index=0,
        help="gemini-2.5-pro — для Pro подписки"
    )
    
    return {
        "use_ai": use_ai and has_key,
        "difficulty": difficulty,
        "has_key": has_key,
        "model_name": model_name
    }
