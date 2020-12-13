it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.update(["Twitter"])
print(it_companies)

it_companies.update(["Samsung", "Alphabet", "Intel"])
print(it_companies)

it_companies.remove('Apple')
print(it_companies)

# remove() only removes the element from the set if the element is present in the set, otherwise it will show an error. discard() function removes the element from the set if present, but produces no error, if the element is not present in the set.

C = A.union(B)
print(C)
print(A.intersection(B))

if A.issubset(B):
    print("True")

else:
    print("False")  

if A.isdisjoint(B):
    print("True")

else:
    print("False") 

D = A.union(B)          
E = B.union(A)
print(D)          
print(E)    

print(A.symmetric_difference(B))  

del A
del B

set_age = set(age)
print(len(set_age))
print(len(age))

# The list is bigger

sentence = {"I", "am", "a", "teacher", "and", "I", "love", "to", "inspire", "and", "teach", "people"}
print(len(sentence))