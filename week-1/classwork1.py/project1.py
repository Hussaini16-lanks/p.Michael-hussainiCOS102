si = 'simple Interest'
p = input('What is P? ')
r = input('What is R? ')
t = input('What is T? ')
a = int(p)*(1 + (float(r)/100.0)*int(t))
result = f' Your {si} = {a}  '
print(result)