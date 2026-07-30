age = int(input("Enter your age: "))
salary = int(input("Enter your monthly salary: "))
experience = int(input("Enter your years of experience: "))

if age >= 21 and salary >= 30000 and experience >= 2:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")