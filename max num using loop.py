num = input("enter number:")
n=num.split(",")
max_num=n[0]
for i in range(len(n)):
    if int(n[i]) > int(max_num):
        max_num=n[i]
print("maximum number is: ",max_num)