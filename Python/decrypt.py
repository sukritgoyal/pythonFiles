
def decryptPassword(s):
    result = ""
    nums = []
    i=0
    while i < len(s):     #pTo*Ta*O
        if s[i].isnumeric() and s[i] != "0":
            nums.append(s[i])
        elif s[i].isupper():
            try:    
                if s[i+1].islower() and s[i+2] == "*":
                    result+=s[i+1]+s[i]
                    i+=2
                else:
                    result += s[i]    
            except IndexError:
                result += s[i]
        elif s[i] == "0":
            result += nums.pop()
        else:
            result += s[i]
        i+=1    
    return result        
                    
                             
if __name__ == "__main__":
    print()
    s = input()
    result = decryptPassword(s)
    print(result)

