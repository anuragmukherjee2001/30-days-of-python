from datetime import date

past_time = date(year=1970, month=1, day=1)
today = date(year=2020, month=12, day=22)

difference = today - past_time
print("The difference is: ", difference)