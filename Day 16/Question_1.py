from datetime import datetime

now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print(current_day)
print(current_month)
print(current_year)
print(current_hour)
print(current_minute)
print(current_timestamp)