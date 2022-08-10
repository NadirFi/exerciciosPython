matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
maior = 0
for l in range(0,5):
    for c in range(0,5):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] > maior:
            maior = matriz[l][c]
print('-='*30)
print(f'Maior número da matriz :{maior}')
print('-='*30)
for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
for l in range(0,5):
    for c in range(0,5):
        if c == l:
            matriz[l][c] *= maior
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

