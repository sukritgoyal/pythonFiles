import random
n = 1
x = random.randint(1,100)
while n <= 9:
    guess = int(input("Enter your guess: "))
    if guess < x:
        print("Increase the number.")
        n+=1
    elif guess > x:
        print("Decrease the number.")
        n+=1
    else:
        print("Congrats you guesses it correctly!")
        break
if n >= 9:
    print("Sorry You Lose")
print(f"The number was {x}!")    
