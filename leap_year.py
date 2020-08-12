
def is_leap(years):
	if years % 4 == 0 and years % 100 != 0:
		return True
	elif years % 100 == 0 and years % 400 != 0:
		return False
	elif years % 400 == 0 and years % 3200 != 0:
		return True
	else:
		return False
y = int(input('plz input a year:'))
print(is_leap(y))