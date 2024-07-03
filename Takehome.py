class BankAccount:
    def __init__(self, accName, accNo, accBal):
        self.accName = accName
        self.accNo = accNo
        self.accBal = accBal

    def deposit(self, amount):
        if amount > 0:
            self.accBal += amount
            print(f"Deposited {amount}, New balance is {self.accBal}.")
        else:
            print("Depo sit amount must be positive")


    def withdraw(self, amount):
        if 0 < amount <= self.accBal:
            self.accBal -= amount
            print(f"Withdraw {amount}, New balance is {self.accBal}.")
        else:
            print("Withdraw amount must be positive and not exceed the account balance.")


    def check_balance(self):
        print(f"Current balance is {self.accBal}.")    
        return self.accBal

account = BankAccount("Zainab", "0235467", 5600) 
account.deposit(600)
account.withdraw(300)
account.check_balance()

print()

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Student(Person):
        def __init__(self, name, age, address, student_id):
            super().__init__(name, age, address)  
            self.student_id = student_id

class Lecturer(Person):
        def __init__(self, name, age, address, employee_id):
             super().__init__(name, age, address)
             self.employee_id = employee_id


student = Student("Alice", 30, "60,tanke junction", "UIL2024")
lecturer = Lecturer("Mrs Zainab", 50, "40,University Rd", "UIL202555")

print(f"{student.name} is {student.age} years old living at {student.address} with {student.student_id} as her id.")
print(f"{lecturer.name} is {lecturer.age} years old living at {lecturer.address} and {lecturer.employee_id} as her id.")



       