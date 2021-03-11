import re
while True:
    exp = input("Enter your Problem: ")
    if exp == "exit":
        break
    reg = re.match(r'^([0-9\.]+)(\+|\-|\*|\/)([0-9\.]+)$',exp)
    try:
        if reg:
            x = float(reg.group(1))
            y = float(reg.group(3))
            z = reg.group(2)
            if z == "+":
                print("Your Answer is : {}".format(x+y))
            elif z == "-":
                print("Your Answer is : {}".format(x-y))
            elif z == "*":
                print("Your Answer is : {}".format(x*y))
            else:
                print("Your Answer is : {}".format(x/y))    
        else:
            print("Enter a valid expression...")
    except:
        print("Error processing your request...")
        
