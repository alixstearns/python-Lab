try:
 a = int(input("enter a number1:  ")) 
 b = int(input("enter a number2: "))

 sum = a + b
 print("Sum:", sum)
except  ValueError:
 print('please enter a valid integer:')

