import random
names=input("enter the names:")
n=names.split(",")
res=random.choice(n)
print(n)
print(f"{res} will pay the bill")
