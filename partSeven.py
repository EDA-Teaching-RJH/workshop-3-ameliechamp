num1 = int(input("Enter number one:"))
num2 = int(input("Enter number two:"))
operator = input("Enter an operator (+,-,*,/,^,%): ")

match operator:
    case "+":
        add = num1+num2
        print(add)
    case "-":
        sub = num1-num2
        print(sub)
    case "+":
        mult = num1*num2
        print(mult)
    case "/":
        div = num1/num2
        print(div)
    case "^":
        power = num1^num2
        print(power)
    case "%":
        mod = num1%num2
        print(mod)
    case _:
        print("Quitting the program...")
            
        