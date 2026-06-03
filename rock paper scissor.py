import random
<<<<<<< HEAD
user=int(input("enter  ur choice(rock,paper,scissors):"))
=======
user =int(input("enter  ur choice(rock,paper,scissors):"))
>>>>>>> cf1ce63cfbb92bf67784f4c35b0f65e802f98e27
com_choice=random.randint(0,2)
if user == 0 and com_choice == 0:
    print("tie")
elif user == 0 and com_choice == 1:
    print("you win...")
elif user == 0 and com_choice == 2:
    print("you lose... computer wins")
elif user == 1 and com_choice == 0:
    print("you lose... computer wins")
elif user == 1 and com_choice == 1:
    print("tie")
elif user == 1 and com_choice == 2:
    print("you win...")
elif user == 2 and com_choice == 0:
    print("you win...")
elif user == 2 and com_choice == 1:
    print("you lose... computer wins")
elif user == 2 and com_choice == 2:
    print("tie")