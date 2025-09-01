from utilitiescv import coin, data

p = data.readint('Enter the price: $')

coin.summary(p, 20, 12)

n1 = data.readint('Enter an integer: $')
n2 = data.readfloat('Enter a real number: $')
print(f'The integer value entered was {n1} and the real value was {n2}')