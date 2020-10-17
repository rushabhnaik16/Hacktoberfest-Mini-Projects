import random

print("Hi what's your name?")
name = raw_input()
print("Nice to meet you", name)
print("Let's Play a game!!")
print("I will think of a number between 1 and 20 and you have to guess it in less than 5 guesses.")
number = random.randint(1, 20)
guesses_no = 0
while (guesses_no < 5):
    print("Take a guess:")
    guess = input()
    guess = int(guess)
    guesses_no = guesses_no + 1
    if (guess < number):
        print("Number is greater than Guess.")
    if (guess > number):
        print("Number is smaller than Guess.")
    if (guess == number):
        break;
if (guess == number):
    print("Yaaaay Good Job", name, " You have guessed the Number correctly in", guesses_no, "Guesses!")
if (guess != number):
    print("Sorry. The number I was thinking of was ",number)
    print("You Should Try Again!")
    