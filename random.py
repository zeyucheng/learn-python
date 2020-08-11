import random

r = random.randint(1, 100)
while True:
	user = input('plz input a number:')
	user = int(user)
	if user > r:
		print('greater than the number')
	elif user < r:
		print('smaller than the number')
	else:
		print('correct!')
		break
