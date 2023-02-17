classificacao = ('Nulo', 'Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Fortaleza', 'Botafogo', 'América-MG', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('='*30)
print('{:^30}'.format('5 PRIMEIROS COLOCADOS'))
print('='*30)

for cont in range(1, 6):
    print(f'{cont}.', classificacao[cont])

print('='*30)
print('{:^30}'.format('4 ÚLTIMOS COLOCADOS'))
print('='*30)

for cont in range(17, 21):
    print(f'{cont}.', classificacao[cont])

print('='*30)
print('{:^30}'.format('LISTA ALFABÉTICA'))
print('='*30)

print(sorted(classificacao))

print('='*30)
print('{:^30}'.format('BUSCA TIME'))
print('='*30)

print(f'O Santos está na {classificacao.index("Santos")}° posição')
print('='*30)

print(f'Sendo assim, {classificacao[1]} CAMPEÃO')
print('🏆'*11)