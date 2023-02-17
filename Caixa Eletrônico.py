print('*'*30)
print('{:^30}'.format('Bem-vindo ao BANCO MORUMBI'))
print('*'*30)
print('Notas disponiveis:  R$200, R$100, R$50, R$20, R$10 e R$5')
valor=int(input('Digite o valor que deseja sacar: R$:'))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced} reais')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break
print('*'*30)
print('{:^30}'.format('Obrigado e Volte Sempre!'))
print('*'*30)