a = {"привет" : "hi",
     "пока" : "bye"}
b = {"Как тебя зовут?" : "what is your name?",
     "Меня зовут *Имя*" : "My name is *Name*"}
c = {"Откуда ты?" : "Where are you from?",
     "Я из Киева" : "I'm from Kyiv"}

def slovary():
    d = {**a, **b, **c}
    print("Словари:")
    print(d)

slovary()
