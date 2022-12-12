total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
spliting_people = int(input("How many people to splite the bill? "))
tipping_price = (tip/100)+1
paying_amount = (total_bill/spliting_people)*tipping_price
round_off = round(paying_amount,2)
print(f"Each person should pay: ${round_off}")