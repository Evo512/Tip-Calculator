print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (tip/100)
complete_amount = (bill + bill_with_tip) / (people)
final_bill = round(complete_amount, 2)
print(f"Each person should pay ${final_bill}")
