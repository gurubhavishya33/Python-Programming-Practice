balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance and amount % 100 == 0:
    print("Transaction Successful")
else:
    print("Transaction Failed")