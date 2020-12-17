def evens_and_odds (num_range):
    Even = 0
    odd = 0

    for i in range(0, num_range + 1):
        if i % 2 == 0:
            Even += 1

        else:
            odd = odd + 1    
    
    print("The number of odds are ", odd)
    print("The number of evens are ", Even)

evens_and_odds(100)            