def readmoney(msg):
	valid = False
	while not valid:
		enter = str(input(msg)).replace(',', '.').strip()
		if enter.isalpha() or enter == '':
			print(f'ERROR:{enter} is not a valid price')
		else:
			valid = True
			return float(enter)