import random

user_name = input("Enter your name : ")
print(f"Hello {user_name}🤗. A number is chosen between 1 and 10.")
print("Guess the number within 3 trials.😁" )
def guess(x, trials=3) :
    random_number = random.randint(1, x)
    user_guess = 0
    trial_count = 0
    
    
    while user_guess != random_number:
        if trial_count >= trials:
            print(f"Sorry, you have exhausted your {trials} trials. The correct number was {random_number}.")
            break

        user_guess = int(input(f"Enter the random number between 1 and {x} : "))
        trial_count += 1

        if user_guess == random_number:
            print (f"Congrats🎉.You guessed the correct number {random_number}.")
        elif user_guess < random_number :
            print(f"The number is greater than {user_guess}.Try Again😪.")
            
        elif user_guess > random_number:
            print(f"The number is less than {user_guess}.Try Again😪.")
            
guess(10, 3)
