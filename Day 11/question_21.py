def all_unique(lst):
    if(len(set(lst))) == len(lst):
        return True

    else:
        return False

lst = [1, 5, 66, 89]

if(all_unique(lst) == True):
    print("All the elements are unique")
else:
    print("All the elements are not unnique")                