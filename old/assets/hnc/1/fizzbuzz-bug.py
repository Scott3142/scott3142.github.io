#Plays fizzbuzz for 1 to 20 - there are two bugs in this script!

for i in range(1,20): #loop from 1 to 20
  if i%3 == 0: #fancy way of checking if i is in the 3 times table
    print('Fizz')
  elif i%5 == 0:
    print('Buzz')
  elif i%3 == 0 and i%5 == 0:
    print('FizzBuzz')

#note: i%3 actually checks the remainder after division of 3 by i.
#e.g. 10 divided by 4 = 2 remainder 2. So 10%4 = 2
#e.g. 23 divided by 5 = 5 remainder 3. So 23%5 = 3
#Therefore, if the remainder is 0, the number is in the times table. Clever, no?
