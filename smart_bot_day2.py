# Day 2

import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 42

with open ("BOT_CONFIG.json", "r") as file:
  BOT_CONFIG = json.load(file)

BOT_CONFIG["intents"]["hello"]

x = []
y = []

count = 0

for intent in BOT_CONFIG["intents"].keys():
  try:
    for example in BOT_CONFIG["intents"][intent]["examples"]: 
      x.append(example)
      y.append(intent)
  except KeyError:
    print(BOT_CONFIG["intents"][intent])


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=RANDOM_STATE)

len(x_train), len(x_test)

vectorizer = CountVectorizer(ngram_range=(1, 5), analyzer="char")
X_train_vectorized = vectorizer.fit_transform(x_train)
X_test_vectorized = vectorizer.transform(x_test)

 #model = LogisticRegression(random_state=RANDOM_STATE, C=10)
model = RandomForestClassifier(random_state=RANDOM_STATE, n_estimators=200)

model.fit(X_train_vectorized, y_train)

# model.predict(vectorizer.transform(["твоя любимая пицца? Как дела?"]))

model.score(X_train_vectorized, y_train)

model.score(X_test_vectorized, y_test)

def get_intent(input_text):
  return model.predict(vectorizer.transform([input_text]))[0]

def bot(input_text):
  intent = get_intent(input_text)
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
