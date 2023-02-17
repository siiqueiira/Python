#Bloco de Apresentação do Programa
print('Sistema para alistamento')

#Bloco de Recebimento de dados
ano=int(input('Digite o ano de seu nascimento:'))
idade=2022-ano
excedido=(2022-ano)-18

#Bloco de Processamento de Dados
if idade < 18:
    print('Você ainda vai se alistar!')
    print('Aliste-se daqui: {} anos'.format(18-idade))

elif idade == 18:
    print('É hora de Alistar!')

elif idade > 18:
    print('Você passou do período de alistamento!')

    if excedido == 1:
        print('Atrasado em {} ano'.format(excedido))

    else:
        print('Atrasado em {} anos'.format(excedido))