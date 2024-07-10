attempts = 3
pin = "password123"
while attempts > 0:
    password = input("enter pin : ")
    if password == pin:
        print("access granted !")
        break
    else:
        attempts  += 1
        print("access denied !")

print("WELCOME TO HBL ATM".center(100))  

balance = 1000

while True:
    print("1. withdraw")
    print("2. deposit")
    print("3. check balance")
    print("4. exit")
    
    choice = int(input("enter number you want to perform : "))
    if choice == 1:
        amount = int(input(("enter amount you want to withdraw : ")))
        if amount > balance:
            print("insufficent balance")
        else:
            balance -= amount
    elif choice == 2:
        int(input('enter amount you want to deposit : '))
        balance += amount
        print("updated balance is {}".format(balance))
    elif choice == 3:
        print("your current balance is {}".format(balance))
    elif choice == 4:
        print("you are now exiting the hbl atm")
        break
    else:
        print("invalid option please try again")
                        
        