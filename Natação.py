#Bloco de Apresentação do Programa
print('Sistema para definir categoria de natação')

#Bloco de Recebimento de dados
ano=int(input('Digite o ano de seu nascimento:'))
idade=2022-ano

#Bloco de Processamento de Dados
if idade <= 9:
    print('O atleta tem {} anos'.format(idade))
    print('Nadador(a) "MIRIM"')

elif idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Nadador(a) "INFANTIL"')

elif idade <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Nadador(a) "JÚNIOR"')

elif idade <= 25:
    print('O atleta tem {} anos'.format(idade))
    print('Nadador(a) "SÊNIOR"')

else:
    print('O atleta tem {} anos'.format(idade))
    print('Nadador(a) "MASTER"')