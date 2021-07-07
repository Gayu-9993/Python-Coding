print("Welcome to the Tip Calculator!")

bill = float(input("Total Bill Amount: $"))
tip = int(input("How much tip would you like to give? 10, 20 or 30? "))
people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill / people

final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
