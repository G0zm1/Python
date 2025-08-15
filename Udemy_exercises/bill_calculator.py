print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many People split the bill? "))

tip_as_percent = tip / 100 * bill
bill_with_tip = bill + tip_as_percent
final_bill = bill_with_tip / people
final_amount = round(final_bill, 2)

print(f"Every person should pay: $ {final_amount}")
