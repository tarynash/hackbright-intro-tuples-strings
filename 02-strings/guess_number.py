from random import randint

random_variable = randint(1,10)
print random_variable

guess = int(raw_input("Guess a number from 1 to 10: "))

while(guess != random_variable):
	if(guess > random_variable):
		print "too high!"
	else:
		print "too low!"

	guess = int(raw_input("Guess again: "))

print "You win!"