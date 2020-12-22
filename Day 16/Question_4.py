from datetime import date

today = date(year=2020, month=12, day=22)
new_year = date(year=2021, month=1, day=1)

time_left_for_new_year = new_year - today
print("The time left for new year is: ", time_left_for_new_year)