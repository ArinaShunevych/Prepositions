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
with gr.Blocks() as interface:
    gr.Markdown("# Обробка прийменників")
    gr.Markdown("Цей інтерфейс дозволяє обробляти текст і знаходити прийменники з відповідними правилами правопису.")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Введіть текст", 
                placeholder="Введіть текст для обробки...", 
                lines=10, 
                max_lines=100
            )
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Результат", 
                placeholder="Результат з'явиться тут...", 
                lines=10, 
                max_lines=100
            )
    
    examples = gr.Examples(
        label="Приклади текстів для обробки",
        examples=[
            "Поперед будинком виднілися високі дерева. Попід старими дубами лежали великі камені. Згідно з планом, тут мала бути нова дорога. Довкола ділянки натягнули стрічку. Поблизу стояли будівельні машини. Внаслідок зсуву ґрунту роботи тимчасово призупинили. Навколо місця працювали охоронці.",
            "У напрямі до міста виднілися новобудови. Відповідно до вказівок, усе було виконано точно. На шляху до місця зустрічі вони зупинилися для відпочинку. У зв’язку з погодними умовами подію перенесли. Близько опівдня все було завершено. Під час роботи було дотримано всіх правил. У результаті вони досягли успіху.",
            "Незважаючи на труднощі, він завершив роботу вчасно. Завдяки підтримці команди проект був реалізований успішно. З-за річки долинали звуки музики. Край дороги стояла невелика капличка. З-під землі били джерела. Поблизу знаходився невеликий парк. Услід за ними вирушили туристи.",
            "Навпроти будинку розташувався великий магазин. Наприкінці вулиці був красивий фонтан. Під час святкування виступали кілька оркестрів. За допомогою нових технологій роботу вдалося оптимізувати. Заради успіху він працював без вихідних. Довкола площі були розташовані клумби. Напередодні свят була проведена генеральна репетиція.",
            "В силу обставин їм довелося змінити маршрут. У результаті їхній план став більш ефективним. Шляхом аналізу вони знайшли найкраще рішення. Навкруги були розкидані уламки старих будівель. Відповідно до умов договору всі сторони дотрималися своїх обов’язків. На шляху до перемоги вони подолали багато перешкод. У зв’язку з цим було прийнято нову стратегію."
        ],
        inputs=input_text
    )

    process_button = gr.Button("Обробити текст")
    process_button.click(process_prepositions, inputs=input_text, outputs=output_text)


# Запуск інтерфейсу
interface.launch()
