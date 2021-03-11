call = int(input())
if call > 0:
    bill = 200
else:
    bill = 0
if call > 100:
    if call > 150:
        if call > 200:
            call = call - 200
            bill += 50*0.6 + 50*0.5 + call*0.4
        else:
            call = call - 150
            bill += 50*0.6 + call*0.5
     else:
         call  = call - 100
         bill += call * 0.6
