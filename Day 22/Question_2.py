import urllib.request 
import json
from pprint import pprint 
from html_table_parser import HTMLTableParser
 
def url_get_contents(url): 

    req = urllib.request.Request(url=url) 
    f = urllib.request.urlopen(req) 

    return f.read() 

xhtml = url_get_contents('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States').decode('utf-8') 

p = HTMLTableParser() 
 
p.feed(xhtml) 

data = p.tables[1]

json_string = json.dumps(data)
print(json_string)
