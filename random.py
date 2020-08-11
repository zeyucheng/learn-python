import random
r = random.randint(1, 100)
i = 0
while True:
	i = i + 1
	user = input('plz input a number:')
	user = int(user)
	if user > r:
		print('greater than the number')
	elif user < r:
		print('smaller than the number')
	else:
		print('correct!')
		print(i,'times')
		break
	print(i,'times')
