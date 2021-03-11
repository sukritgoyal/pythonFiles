try:
    while True:
        oper = input("Enter the operator you want to use: ")
        if oper == "exit":
            break
        digit1 = float(input("Enter the first digit: "))
        digit2 = float(input("Enter the second digit: "))
        if oper == "+":
            print("Your answer is %d"%(digit1+digit2))
        elif oper == "-":
            print("Your answer is %d"%(digit1-digit2))
        elif oper == "*":
            print("Your answer is %d"%(digit1*digit2))
        elif oper == "/":
            print("Your answer is %d"%(digit1/digit2))
        else:
            raise Exception

except:
    print("Error processing your request")
finally:
    print("See you soon!")
#122.162.161.200
