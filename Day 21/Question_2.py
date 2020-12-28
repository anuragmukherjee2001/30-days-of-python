class PersonAccount:
    def __init__(self, firstname, lastname, income, expense):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income
        self.expense = expense

    def total_income(self):
        return self.income

    def total_expense(self):
        return self.expense

    def account_info(self):
        return f'The name of the person is {self.firstname} {self.lastname}. Total expenses is {self.expense} and the total income is {self.income}. Account balance is {self.income - self.expense}.  '  

    def add_income(self):
        new_income = int(input("Enter the amount of income: "))
        self.income =  self.income + new_income
        return self.income 

    def add_expense(self):
        new_expense = int(input("Enter the amount of expense: "))
        self.expense = self.expense + new_expense
        return self.expense    

    def acc_bal(self):
        return self.income - self.expense


fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
inc = int(input("Enter the income: "))
exp = int(input("Enter the expenses: "))

PA1 = PersonAccount(fname, lname, inc, exp)
print(PA1.firstname)        
print(PA1.lastname)        
print(PA1.income)        
print(PA1.expense) 
print((PA1.total_expense()))       
print((PA1.total_income()))       
print((PA1.acc_bal()))       
print((PA1.add_expense()))       
print((PA1.add_income()))       
print((PA1.account_info()))       