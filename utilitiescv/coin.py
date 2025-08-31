# Coin

def increase(price = 0, tax = 0, format = False):
	result = price + (price * tax / 100)
	return result if format is False else currency(result)

def decrease(price = 0, tax = 0, format = False):
	result = price - (price * tax / 100)
	return result if format is False else currency(result)
	
def double(price = 0, format = False):
	result = price * 2
	return result if format is False else currency(result)

def half(price = 0, format = False):
	result = price / 2
	return result if format is False else currency(result)
	
def currency(price = 0):
	return f'${price:.2f}'.replace('.', ',')
	
def summary(price = 0, tax_inc = 10, tax_dec = 5):
	print('-' * 30)
	print('Value Summary'.center(30))
	print('-' * 30)
	
	print(f'Analyzed price: \t{currency(price)}')
	print(f'Double the price: \t{double(price, True)}')
	print(f'Half the price: \t{half(price, True)}')
	print(f'{tax_inc}% increase: \t{increase(price, tax_inc, True)}')
	print(f'{tax_dec}% reduction: \t{decrease(price, tax_dec, True)}')