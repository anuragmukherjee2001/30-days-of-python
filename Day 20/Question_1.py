import requests
from collections import Counter

response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
cont = response.content

split = cont.split() 
 
count = Counter(split) 
top_10 = count.most_common(10) 
  
print(top_10) 

