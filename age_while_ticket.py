while True:

    age = int(input("Enter the age: "))

    if age <= 3:
        print("Ticket is free!")
    elif age > 3 and age < 12:
        print("the ticket is $10")
    else:
        print("the ticket is $12")