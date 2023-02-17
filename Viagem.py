#Bloco de Apresentação do Programa
print('Sistema para valor da viagem')

#Bloco de Recebimento de dados
km=float(input('Digite a distância em quilômetros:'))

#Bloco de Processamento de Dados
if km <= 200:
    total=km*0.50

else:
    total=km*0.45

#Bloco de Saída de Dados
print('''Custo até 200km = $0.50/km
Custo + 200km = $0.45/km''')
print('Valor total da viagem:', total)