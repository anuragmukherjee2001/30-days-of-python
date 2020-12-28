import re

file = open("Data/email_exchanges.txt", 'r')
content = file.read()

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", content)
print(emails)