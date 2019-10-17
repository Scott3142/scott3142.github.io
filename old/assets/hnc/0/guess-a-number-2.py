import random

print('Think of a whole number between 1 and 10. I am going to try and guess it!')

#generate random number and store as variable rnd
rnd = random.randint(1,10)

#initialise uans (or else the while loop won't know what to look for)
uans = 'no'

while (uans != 'yes'):
    
    #take the variable uans as the user input. It should be higher, lower or yes. Anything else will fail.
    uans = str(input('Is your number ' + str(rnd) + '? Please answer higher, lower or yes. '))
    
    if (uans == 'lower'):
        #only use values lower than the number guessed
        rnd = random.randint(1,rnd)
    elif (uans == 'higher'):
        #only use values higher than the number guessed
        rnd = random.randint(rnd,10)
    elif (uans == 'yes'):
        #prints success if answers are equal. Then ends loop because while is satisfied.
        print('Great! I knew computers were smarter than humans!')
    else:
        #error if input is something other than higher, lower or yes
        print("Sorry. I didn't get that. Please answer higher, lower or yes.")1
