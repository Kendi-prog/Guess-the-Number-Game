import random 

#the computer is the one to guess the random number that you have secretly come up with.
def guess(x, trials=5):
    low = 1   #the minimum value
    high = x  #the maximum value
    feedback = ""
    trial_count = 0

    while True:
      if trial_count >= trials :
        print("Sorry the computer has exhausted all the trials")
        break
      if low != high :
         computer_guess = random.randint(low, high)
         trial_count += 1

      else :
        computer_guess = low   #or high because low = high

      feedback = input(f"Is {computer_guess} too high (H), too low (L), or correct (C) :").lower()

      if feedback == 'c':
       print("Yeeiy, the computer guessed your number correctly.")
       break
      elif feedback == 'h':
       high = computer_guess - 1
      elif feedback == 'l':
       low = computer_guess + 1
    
guess(1000, 5)

