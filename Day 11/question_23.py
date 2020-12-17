def valied_variable(string):

    lst = []
    for i in string:
        if i == " ":
            print("The string is not a valied variable")
            exit(0)

    for i in string:
        lst.append(i)
    if(lst[0] >= '0' and lst[0] <= '1'):
        print("The string is not a valied variable")
        exit(0)

    else:
        print("The string is a valied variable")
        exit(0)     

    lst_symbols = ['!', '@','$', '%']

    if lst_symbols in lst:
        print("The string is not a valied variable")
        exit(0)  

    else:
        print("The string is a valied variable")
        exit(0)           


valied_variable("Anurag mu")            