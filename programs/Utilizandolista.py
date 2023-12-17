num = []
while True:
    num.append(int(input('Digite um numero: ')))
    r = str(input('Quer continuar? S/N: '))
    if r in 'Nn':
        break
par = []
imp = []
for i, v in enumerate(num):
    if i % 2 == 0:
        par.append(i)
    else:
        imp.append(i)

print(f'os numeros digitados são {num}, os pares são {par}, e os impar são {imp}')

