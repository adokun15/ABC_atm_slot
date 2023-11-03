print("welcome to Abc Atm Slot!")

c_name = input("Enter Name: ")
bal = 67450

i = 3
while i > 0:
    acc_no = (input("Enter your Atm digit(Must be 10 digit): "))
    pin_no = (input("Enter your Pin (must be five digit): "))

    if len(acc_no) == 10 and len(pin_no) == 5:

        print(f"Login successful. Welcome {c_name} \n")
        print("Main Menu: ")
        print("1 - View My Balance")
        print("2 - Withdraw Cash")
        print("3 - Deposit Funds")
        print("4 - Exit")

        ques_1 = int(input())

        if ques_1 == 1:
            print("Your Balance is: $" + str(bal))
        if ques_1 == 2:
            print("Withdrawal Menu: ")

            print("1 - $1000 " + (" "*7) + "4 - $10000")
            print("2 - $2000 " + (" "*7) + "5 - $20000")
            print("3 - $5000 " + (" "*7) + "6 - Cancel Transaction")
            w_amt = int(input("Choose withdrawal Amount: "))

            if w_amt == 6:
                print("Withdrawal Transaction Cancelled!/n/n")
                print("No amount deducted")

                break
            if w_amt == 1:
                bal = bal - 1000
                print("Your balance is: $"+str(bal))
            if w_amt == 2:
                bal = bal - 2000
                print("Your balance is: $"+str(bal))

            if w_amt == 3:
                bal = bal - 5000
                print("Your balance is: $"+str(bal))
            if w_amt == 4:
                bal = bal - 10000
                print("Your balance is: $"+str(bal))
            if w_amt == 5:
                bal = bal - 20000
                print("Your balance is: $"+str(bal))

            if w_amt > bal:
                print("Amount is greater than balance. Try again!")
                w_amt = int(input("Enter a Smaller Amount: "))
            else:
                bal = bal - w_amt
                print("Your balance is: $" + str(bal))

        if ques_1 == 3:
            d_amt = int(input("ENTER AMOUNT TO DEPOSIT OR CLICK 0 TO CANCEL:"))
            if d_amt == 0:
                print("No amount has been deposited into your account")
                break
            else:
                bal = bal + d_amt
                print("Your balance is: $" + str(bal))
                break
        if ques_1 == 4:
            print("Thank you for using ABC atm slot!")

        break
    else:
        print("Invalid ATM Credential!, Trial left {y}".format(y=i - 1))
        if i == 1:
            print("Sorry We Cannot Validate Your details after 3 trials!")
        i = i - 1
