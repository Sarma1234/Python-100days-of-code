print("Welcome to the rollercoaster ride!!")
height = int(input("What is your height in cm?\n"))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    bill = 0
    if age < 12:
        bill = 5
        print("Child tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to click photos? Y or N \n")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")