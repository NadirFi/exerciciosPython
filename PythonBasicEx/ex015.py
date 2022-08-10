k = float(input('Digite quantos Km foram percorridos: '))
a = int(input('Digite por quantos dias o carro foi alugado: '))

km = k * 0.15
alu = a * 60

print('Custo por Km = R$ 0.15')
print('Custo por dias = R$ 60.00')
print(f'Por {a} dias, irá pagar R${alu:.2f}. Por {k} Km, irá pagar R${km:.2f}')
print(f'O total a pagar é: R${km+alu}')
