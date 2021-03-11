def FirstFactorial(num):
  exp = str(num)
  val = num - 1 
  while val >= 1:
    exp += '*' + str(num) 
  # code goes here
  num = eval(exp)
  return num

# keep this function call here
c = int(input())
print(FirstFactorial(c))
