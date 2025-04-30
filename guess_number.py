# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
secret_number = random.randint(0,9)
print(secret_number)
attempt = 4
while attempt >0:
    guess=int(input("Guess the number "))
    if guess == secret_number:
        print(True)
        print("Hurreh ! You have successfully guessed the number when  the ",attempt ," left")
        break
    elif guess > secret_number:
        print(f"Your guess number {guess} is higher then secret number ")
        attempt -=1
    elif guess< secret_number:
        print("Guessed number" ,guess, "is lower than the secret number ")
        
        attempt -=1
    print(f"only {attempt} left" )
    

