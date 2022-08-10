import math
cto = float(input('Digite o valor do cateto oposto: '))
cta = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(cto, cta)
print(f'O valor da hipotenusa deste triangulo é: {hip:.2f}')
