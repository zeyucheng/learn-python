password = 'a123456'
time = 0
while time < 3:
	input_password = input('plz input your password: ')
	if input_password == password:
		print('password is correct')
		break
	else:
		time = time + 1
		left = 3 - time
		print('password is incorrect,', 'you still have', left, 'chance')
