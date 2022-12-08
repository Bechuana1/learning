import datetime

today = datetime.date.today();

now = datetime.datetime.now()


yesterday = today - datetime.timedelta(days=1)
print(today)
print("yesterday was: ", yesterday)