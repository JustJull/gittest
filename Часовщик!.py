from datetime import datetime, timedelta

def watchmaker():
   sec = timedelta(seconds = int(input("введите количество секунд для перевода: ")))
   d = datetime(1, 1, 1) + sec

   print("Дни : часы : минуты : секунды")
   print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
watchmaker()
