tot18 = toth = totm = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M]')).strip().upper() [0]
    if idade >= 18:
        tot18 += + 1
    if sexo == 'M':
        toth += +1
    if sexo == 'F' and idade < 20:
        totm += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper() [0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'Total de mulheres abaixo de 20 anos cadastradas: {totm}')