#Bloco de Apresentação do Programa
print('Sistema para cálculo do valor alugado')

#Bloco de Recebimento de dados
km=float(input('Digite a quantidade de quilômetros percorrido:'))
dia=int(input('Por quantos dias foi alugado:'))

#Bloco de Processamento de Dados
custo=60*dia
rodado=km*0.15
total=custo+rodado

#Bloco de Saída de Dados
print('''Custo por dia = $60
Custo por km = $0.15''')
print('Valor total da locação:', total)

