print('-' * 20)
print('PROGRAMA DE FINANCIAMENTO IMOVEL')
print('-'* 20)
casa = float(input('Qua o valor da casa?: '))
salario = float(input('Qual o seu salario?: '))
anos = int(input('Quantos anos irá pagar?: '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('{:.2f}'.format(prestação))
if salario <= minimo:
    print("aceito")
else:
    print("negado")