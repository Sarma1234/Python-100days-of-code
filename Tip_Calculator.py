print("Welcome to the tip calculator !")
Total_bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15\n"))
num_of_people = int(input("How many people to split the bill?\n"))
bill_per_person = "{:.2f}".format((Total_bill+tip)/num_of_people)
print(f"Each person should pay {bill_per_person}rs")
