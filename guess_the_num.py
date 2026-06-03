import random
print("Let me think of a number between 1 to 50...")
real_num=random.randint(1, 50)
guess_num=0
choice = input("choose level of difficulty:easy or hard:").lower()
if choice == "easy":
    print("You have 10 attempts to guess the number.")
    for i in range(10):
        guess_num = int(input("Make a guess: "))
        if guess_num == real_num:
            print(f"You got it! The answer was {real_num}.")
            break
        elif guess_num < real_num:
            print("Too low.")
            print(f"you have {10-i} attempts left.")
        else:
            print("Too high.")
            print(f"you have {10-i} attempts left.")
    else:
        print(f"Game over! you lost.....The number was {real_num}.")
elif choice == "hard":
    print("You have 5 attempts to guess the number.")
    for i in range(5):
        guess_num = int(input("Make a guess: "))
        if guess_num == real_num:
            print(f"You got it! The answer was {real_num}.")
            break
        elif guess_num < real_num:
            print("Too low.")
            print(f"you have {5-i} attempts left.")
        else:
            print("Too high.")
            print(f"you have {5-i} attempts left.")
    else:
        print(f"Game over! you lost.....The number was {real_num}.")