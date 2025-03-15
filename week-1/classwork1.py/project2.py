ci = 'compound Interest'
p = input('What is P? ')
r = input('What is R? ')
t = input('What is t? ')
n = input('What is n? ')
a = int(p)*(1 + (float(r)/int(n))**int(t)*int(n))
result = f' Your {ci} = {a}  '
print(result)