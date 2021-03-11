inp = input("Enter a word: ")
lis = []
for i in inp:
    lis.append(i)

j = len(lis) - 1
print("It's reverse is: ")
while j>=0:
    print(lis[j],end='')
    j-=1
