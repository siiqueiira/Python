print('*'*30)
print('Magazine dos Preços Baixos')
print('*'*30)

total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Digite o produto desejado:'))
    preco = float(input('Digite o preço do produto R$:'))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper() [0]
        print('*'*30)

    if resp == 'N':
        break

print('FIM DA COMPRA')
print('*'*30)
print(f'Total gasto: R${total}')
print(f'{totmil} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} custando R${menor}')