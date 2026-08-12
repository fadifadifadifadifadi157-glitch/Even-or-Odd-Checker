while True:
    try:
        number = int(input("Enter a number: "))

        if number %2== 0:
            print("The number is even!")
        else:
            print("The number is odd!")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

    again =input("Do you want to check another number? (yes/no): ")

    if again.lower() !="yes":
        print("Goodbye!")
        break
