def total_bill(bill_amount,tip_percentage):
    tip_amount=(tip_percentage/100)*(bill_amount)
    total=tip_amount+bill_amount
    print(f"You'r bill amount is {bill_amount} \n You'r tip amount is {tip_amount} \n You'r total bill amount is {total} \n Have a very nice day ahead 😊")
ba=int(input("Please enter your Bill Amount "))
tp=int(input("Please enter your Tip Percentage "))
total_bill(ba,tp)


