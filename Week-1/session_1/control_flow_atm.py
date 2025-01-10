balance = int(50000)
pin = int(4325) 
input_pin = input("Welcome! Please enter your pin!")
if int(input_pin) == pin:
    print("You have " +  str(balance) + " pounds")
    input_money = input("Would you like to withdraw or deposit money?")
    if input_money == "withdraw":
        input_withdraw = input("Please enter the amount of money you wish to withdraw.")
        balance_after_withdraw = balance - int(input_withdraw)
        if balance_after_withdraw < 0:
            print("Sorry, you cannot withdraw that much") 
        else:
            print("You have " + str(balance_after_withdraw) + " pounds remaining. Have a wonderful day!")
    elif input_money == "deposit":
        input_deposit = input("Please enter the amount of money you wish to deposit.")   
        balance_after_deposit = balance + int(input_deposit)
        print("You now have " + str(balance_after_deposit) + " pounds. Have a wonderful day!")       
    else:
        print("Thank you for visiting!")
else:
    print("This is the wrong pin. Please try again.") 