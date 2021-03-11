n = int(input())
i = 0
emps = []
while i < n:
    emps.append(input())
    i+=1
empsChar = []
for emp in emps:
    empChar = []
    for letter in emp:
        empChar.append(letter)
    empsChar.append(empChar)

for chars in empsChar:
    if chars != sorted(chars):
        print("YES")
    else:
        print("NO")
