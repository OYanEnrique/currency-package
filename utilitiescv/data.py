'''def readmoney(msg):
	valid = False
	while not valid:
		enter = str(input(msg)).replace(',', '.').strip()
		if enter.isalpha() or enter == '':
			print(f'ERROR:{enter} is not a valid price')
		else:
			valid = True
			return float(enter)'''
			
def readint(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31m ERROR: please enter a valid integer.\033[m')
			continue
		except (KeyboardInterrupt):
			print('\033[31m User preferred not to enter a number. \033[m')
			return 0
		else:
			return n
			
def readfloat(msg):
	while True:
		try:
			n = float(input(msg))
		except (ValueError, TypeError):
			print('\033[31m ERROR: please enter a valid integer.\033[m')
			continue
		except (KeyboardInterrupt):
			print('\033[31m User preferred not to enter a number. \033[m')
			return 0
		else:
			return n
	