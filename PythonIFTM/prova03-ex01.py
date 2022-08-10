import math
while True:
    print('Digite a medida dos 3 lados do triangulo')
    print('-='*30)
    while True:
        n1 = float(input('Lado 1:  '))
        if n1 <= 0:
            print('Valores menores ou iguais a zero nao são permitidos..')
        else:
            break
    while True:
        n2 = float(input('Lado 2:  '))
        if n2 <= 0:
            print('Valores menores ou iguais a zero nao são permitidos..')
        else:
            break
    while True:
        n3 = float(input('Lado 3:  '))
        if n3 <= 0:
            print('Valores menores ou iguais a zero nao são permitidos..')
        else:
            break
    print('-=' * 30)
    print(f'Lado 1: {n1}, Lado 2: {n2}, Lado 3: {n3}.')
    print('-=' * 30)
    a = abs(n2 - n3)
    b = abs(n1 - n3)
    c = abs(n1 - n2)
    if (a < n1 < (n2 + n3)) or (b < n2 < (n1 + n3)) or (c < n3 < (n1 + n2)):
        if n1 == n2 == n3:
            print('Triangulo EQUILATERO!!')
            print('-=' * 30)
        elif n1 != n2 != n3:
            print('Triangulo ESCALENO!!')
            print('-=' * 30)
        else:
            print('Triangulo ISÓSCELES!!')
            print('-=' * 30)
        p = (n1 + n2 + n3) / 2
        s = math.sqrt(p*((p-n1)*(p-n2)*(p-n3)))
        print(f'A area do triangulo digitado é: {s:.2f} cm²')
        print('Obrigado!!!')
    else:
        print('Os valores digitados nao formam um triangulo..')
    r = str(input('Deseja tentar novamente ? [S/N] '))
    if r in 'Nn':
        print('Obrigado!!!')
        break

