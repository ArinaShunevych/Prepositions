import gradio as gr
from language.preposition import extract_prepositions

def process_prepositions(text):
    # Перевірка на пустий або некоректний ввід
    if not text.strip():
        return "Текст введено некоректно. Поле не може бути порожнім."
    
    if not all(char.isalpha() or char.isspace() or char in '.,-’\'‘"' for char in text):
        return "Текст введено некоректно. Використовуйте лише кириличні символи, пробіли та пунктуацію."
    
    # Перевірка на кирилицю
    if not any("а" <= char.lower() <= "я" or char == "є" or char == "ї" for char in text):
        return "Текст введено некоректно. Використовуйте лише кириличні символи."

    # Обробка тексту
    prepositions_in_text = extract_prepositions(text)
    if prepositions_in_text:
        result = "Знайдені прийменники, їх групи та правила написання:\n"
        for prep, group, rule in prepositions_in_text:
            result += f"- Прийменник: '{prep}', Група: {group}, Правило написання: {rule}\n"
    else:
        result = "У тексті не знайдено жодного прийменника."
    
    return result.strip()

# Gradio інтерфейс
interface = gr.Interface(
    fn=process_prepositions,
    inputs=gr.Textbox(
        label="Введіть текст",
        placeholder="Введіть текст для обробки...",
        lines=10,
        max_lines=100
    ),
    outputs=gr.Textbox(
        label="Результат",
        placeholder="Результат з'явиться тут...",
        lines=10,
        max_lines=100
    ),
    title="Обробка прийменників",
    description="Цей інтерфейс дозволяє обробляти текст і знаходити прийменники з відповідними правилами правопису."
)

# Запуск інтерфейсу
interface.launch()
