ap = 'Annuity Plan'
pmt = input('What is PMT? ')
r = input('What is R? ')
t = input('What is t? ')
n = input('What is n? ')
a = int(pmt)*((1+(float(r)/int(n))**int(n)*int(t))-1)/(float(r)/int(t))
result = f' Your {ap} = {a}  '
print(result)