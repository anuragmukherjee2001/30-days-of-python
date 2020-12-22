from datetime import datetime

now = datetime.now()

current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)