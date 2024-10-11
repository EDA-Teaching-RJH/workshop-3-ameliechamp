age = int(input("Enter in your age: "))
student = input("Are you a student?: ").lower()
if age < 12 or age >= 65:
    print("Your ticket costs £5.")
elif 12<=age<=64 and student == "no":
    print("Your ticket costs £10")
elif 12<=age<=64 and student == "yes":
    print("Your ticket costs £8")
else:
    print("Not a valid input.")