import math
num = float(input("enter a number:"))
if num <= 0:
    print("Error: Please enter a positive number.")
else:
    result = math.log(num)
    print("The natural logarithm of", num, "is:", result)