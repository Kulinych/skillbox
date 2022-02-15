import random

from nltk import edit_distance

BOT_CONFIG = {
    "intents": {
        "hello": {
            "examples": ["Привет", "Здравствуйте", "Добрый вечер"],
            "responses": ["Здравствуй", "Хеллоу", "Хай"]
        },
        "thanks": {
            "examples": ["Спасибо", "Большое спасибо"],
            "responses": ["Пожалуйста", "Не за что", "Обращайтесь еще"]
        },
        "do": {
            "examples": ["Как дела", "How are you"],
            "responses": ["Отлично", "Нормально", "Пока не радила:)"],
        },
        "name": {
            "examples": ["Как тебя зовут", "Как твое имя", "Назовитесь"],
            "responses": ["Тестик", "Можете звать меня, Тестик", "Май нэйм из Тестик"],
        },    
        "mood": {
            "examples": ["Как настроение", "какой настрой", "что с настроением"],
            "responses": ["в норме", "все Ок", "все плохо"],                 
        }
    }
}

def clean_text(text):
  output_text = ""
  for char in text:
    if char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuioplkjhgfdsazxcvbnm":
      output_text = output_text + char
  return output_text

def get_intent(input_text):
  for intent in BOT_CONFIG["intents"].keys():
    for example in BOT_CONFIG["intents"][intent]["examples"]:
      text1 = clean_text(input_text.lower())
      text2 = clean_text(example.lower())
      if edit_distance(text1, text2) / max(len(text1), len(text2)) < 0.34:
        return intent
  return "Not found"

def bot(input_text):
  intent = get_intent(input_text)
  if intent == "Not found":
    return "Мы вас не поняли :( Попробуйте снова"
  else:
    return random.choice(BOT_CONFIG["intents"][intent]["responses"])

input_text = ""
print("Для выхода из диалога напишите Пока")
print("------")

while True:
  input_text = input()
  if input_text == "":
    print("Вы ничего не ввели")
    continue
  if input_text == "Пока":
    break
  else:
    print(bot(input_text))
