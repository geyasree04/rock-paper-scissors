def prime(num):
    flag = False
    if num ==1 :
        print("1 is not a prime number")
    elif num >1:
        for i in range(2,num):
            if num % i == 0:
                flag = True
                break   
    if flag == False:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
number=int(input("Enter a number: "))
prime(number)