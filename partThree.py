score = int(input("What is your score?: "))
if 90>=score<=100:
    print("A")
elif 89>=score<=80:
    print("B")
elif 79>=score<=70:
    print("C")
elif 69>=score<=60:
    print("D")
elif 60>=score:
    print("F")
else:
    print("That is not a valid input.")
