num_phone = '(49)646-550448'
num = num_phone.split(')')
codig = num[0]
numer0 = num[1]
cod = codig.split('(')
numero = numer0.split('-')
print('+'+cod[1]+'-'+numero[0]+numero[1])