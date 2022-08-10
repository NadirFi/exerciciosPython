while True:
    print('MENU DE OPÇÕES')
    print('1 - Média Aritimética ')
    print('2 - Media Ponderada ')
    print('3 - Sair ')
    op = int(input('Digite a opção desejada: '))
    print('-='*30)
    if op in (1, 2, 3):
        if op == 1:
            print('Você irá digitar dois valores')
            n1 = float(input('Digite o valor 1: '))
            n2 = float(input('Digite o valor 2: '))
            print(f'A media Aritimética do valor {n1} e {n2} é: {(n1+n2)/2:.2f}')

        elif op == 2:
            print('Você irá digitar três valores')
            n1 = float(input('Digite o valor 1: '))
            p1 = float(input('Digite o peso do valor 1: '))
            n2 = float(input('Digite o valor 2: '))
            p2 = float(input('Digite o peso do valor 2: '))
            n3 = float(input('Digite o valor 3: '))
            p3 = float(input('Digite o peso do valor 3: '))
            print('-=' * 30)
            print('Formula usada: MP = (((x¹*p¹) + (x²*p²) + (x³*p³))/(p¹+p²+p³))')
            print('-=' * 30)
            print(f'Valor 1: {n1}, Peso: {p1} -- Valor 2: {n2}, Peso: {p2} -- Valor 3: {n3}, Peso: {p3}')
            print('-='*30)
            print(f'A media Ponderada dos valores digitados é: {(((n1*p1) + (n2*p2) + (n3*p3))/(p1+p2+p3)):.2f}')
        else:
            print('Você digitou para sair do programa!!')
            print('Muito obrigado!!')
            break
    else:
        print('Opção invalida.. Digite uma opção descrita no menu!!')
        print('-=' * 30)
    c = str(input('Deseja tentar novamente: [S/N]: '))
    print('-=' * 30)
    if c in 'nN':
        print('Obrigado!!')
        break

