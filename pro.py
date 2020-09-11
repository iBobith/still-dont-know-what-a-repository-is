import random

points = 0

while True:
	randomgenerated = random.randint(1, 10)
	inputnumber = input('Guess the number: ')
	if int(inputnumber) == randomgenerated:
		points += 1
	print('points = ' + str(points) + ', the number was ' + str(randomgenerated))