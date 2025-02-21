'''
Author: Tin
KUID: 3175049
Date: 02/14/2025
Lab: lab3
Last modified: 02/21/2025
Purpose: Using Loops
'''
number_guess = int(input("Guess a number:"))
guess_count = 0
closest_guess = 900000000000000
number=36
Play_again = "y"
while Play_again !="n":
    
    if number_guess < number:
        print("Sorry, your guess is too low")
        if abs(number-number_guess)  <  abs(number - closest_guess) and number_guess != number:
            closest_guess = number_guess
            print ("test", closest_guess)
        number_guess = int(input("Guess a number:"))
        guess_count = guess_count + 1
        
    elif number_guess > number:
        print("Sorry, your guess is too high")
        if abs(number-number_guess)  <  abs(number - closest_guess) and number_guess != number:
            closest_guess = number_guess
        number_guess = int(input("Guess a number:"))
        guess_count = guess_count + 1
    elif number_guess == number:
        print ("You Win!")
        print ("You guessed the secret number after", guess_count+1, "guess(es)")
        if guess_count == 0:
            print ("Your closest guess was .....UMM. YOU DID IT ON YOUR FIRST TRY....... IGNORE THIS")
        else:
            print ("Your closest guess was", closest_guess)
        guess_count = 0
        number_guess = 0
        closest_guess = 900000000000000
        Play_again = input("Would you like to play again? (y/n):")
        if Play_again == "y":
            number_guess = int(input("Guess a number:"))
