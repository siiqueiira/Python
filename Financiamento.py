#Bloco de Apresentação do Programa
print('Sistema para aprovar empréstimo')

#Bloco de Recebimento de dados
casa=float(input('Digite o valor da casa: R$'))
salario=float(input('Digite o valor do seu salário: R$'))
tempo=int(input('Digite em quanto anos irá pagar:'))

#Bloco de Processamento de Dados
while tempo == 0:
    tempo = int(input('Digite em quanto anos irá pagar:'))

mensal=tempo*12
prestacao=casa/mensal

if prestacao >= (salario * (30 / 100)):
    print('''Empréstimo RECUSADO!
O valor da parcela excede 30% do seu salário.''')

else:
    print('Empréstimo APROVADO!')

#Bloco de Saída de Dados
print('Valor total da parcela de: R${:.2f}'.format(prestacao))