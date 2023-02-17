#Bloco de Apresentação do Programa
print('*'*155)
print('Cálculo para Aposentadoria')
print('*'*155)

#Bloco de Recebimento de dados
nome=str(input('Digite seu Nome:'))
cpf=int(input('Digite seu CPF:'))
rg=int(input('Digite seu RG:'))
sexo=str(input('Digite seu Sexo:'))
idade=int(input('Digite sua Idade:'))

#Bloco de Processamento de Dados
if sexo == 'Masculino' or 'masculino':
    apos=65-idade
    ano=(65-idade)+2022
    print('''O seu nome é: {}
CPF: {}
RG {}
Sexo: {}
Idade: {} anos'''.format(nome,cpf,rg,sexo,idade))
    print('''Ano de aposentadoria: {}
Faltam: {} anos'''.format(ano, ano-2022))

elif sexo == 'Feminino' or 'feminino':
    apos = 60 - idade
    ano = (60 - idade) + 2022
    print('''O seu nome é: {}
CPF: {}
RG {}
Sexo: {}
Idade: {} anos'''.format(nome, cpf, rg, sexo, idade))
    print('''Ano de aposentadoria: {}
Faltam: {} anos'''.format(ano, ano - 2022))