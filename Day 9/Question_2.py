my_age = 19
your_age = int(input("Enter your age: "))

if(your_age > my_age):
    print("You are ", your_age - my_age, "years older than me.")

elif(your_age == my_age):
    print("You are as old as me")

else:
    print("You are ", my_age - your_age, "years smaller than me.")    