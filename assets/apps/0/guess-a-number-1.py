import random

#generate random number and store as variable rnd
rnd = random.randint(1,10)

#take user input and store in variable uans
print('I am thinking of a whole number between 1 and 10. I want you to try and guess it!')
uans = int(input('Guess a whole number: '))

#repeat until number is guessed correctly
while (rnd != uans):
    if (rnd > uans):
        #tell the player they need to guess a higher number, because theirs was too low
        uans = int(input('Higher! Guess again: '))
    elif (rnd < uans):
        #tell the player they need to guess a lower number, because theirs was too high
        uans = int(input('Lower! Guess again: '))
        
print('Congratulations! You guessed the number correctly!')
