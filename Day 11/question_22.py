def same_data_type(lst):
    lst_type = []
    for i in lst:
        lst_type.append(type(i))
        
    if len(set(lst_type)) == len(set(lst)):
        print("all the data types are same")  
    else:
        print("All the data types are not same")     


lst = [1,2,'Anurag',4]

same_data_type(lst)