
def return_lines(filename):

    file = open(filename,"r") 
    count = 0

    content = file.read() 
    line_list = content.split("\n") 
    
    for i in line_list: 
        if i: 
            count += 1
            
    print("Total number of lines in this file are: ") 
    print(count) 

def return_words(filename):

    file = open(filename,"r") 
    count = 0

    content = file.read() 
    word_list = content.split(" ") 
    
    for i in word_list: 
        if i: 
            count += 1
            
    print("Total numbers of words in this file are: ") 
    print(count)    

return_lines("Data/donald_speech.txt")    
return_words("Data/donald_speech.txt")    