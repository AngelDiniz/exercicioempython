print('=========== SIMULADOR DA LOJINHA ANGEL ===========')
preço = float(input('Digite o valor das compras: R$'))
print('''DIGITE A FORMA DE PAGAMENTO 
[ 1 ] A VISTA DINHEIRO\CHEQUE 
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X NO CARTÃO SEM JUROS 
[ 4 ] 3X NO CARTÃO OU MAIS COM 20% DE JUROS ''')
opção = int(input('Qual a forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parecelada em 2x e ficara no valor de {}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 /100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('o valor das {} pacelas ficara {}'.format(totparc,parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA')
print('O valor de {} , ficara com o desconto {}'.format(preço,total))


