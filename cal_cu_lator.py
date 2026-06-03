def calculator(first_num, oper, second_num):
    if oper=="+":
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    elif oper=="-":
        print(f"{first_num} - {second_num} = {first_num - second_num}")
    elif oper=="*":
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    elif oper=="/":
        print(f"{first_num} / {second_num} = {first_num / second_num}")
    else:
        print("invalid operator")


first_num = int(input("enter the first number:"))
print("+\n-\n*\n/\n")
oper=input("pick the operator:")
second_num = int(input("enter the second number:"))
res = calculator(first_num, oper, second_num)
choice=input(f"enter 'y' to continue calculation with {res} or 'n' to start new calculation or 'x' to exit:").lower()
while choice=='y':
    first_num=res
    print("+\n-\n*\n/\n")
    oper=input("pick the operator:")
    second_num = int(input("enter the second number:"))
    res = calculator(first_num, oper, second_num)
    choice=input(f"enter 'y' to continue calculation with {res} or 'n' to start new calculation or 'x' to exit:").lower()








