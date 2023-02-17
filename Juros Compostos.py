#Bloco de Apresentação do Programa
print('Programa para cálculo de empréstimo')

#Bloco de recebimento de dados
c=float(input('Digite o valor para empréstimo necessário:'))
t=int(input('Digite o número de meses para pagamento, sendo eles 2, 6, 12 ou 24:'))

#Bloco de Processamento
if t==2:
    i=0.0690
elif t==6:
    i=0.0714
elif t==12:
    i=0.0921
elif t==24:
    i = 0.1246

for x in range(t):
    c=c*(1+i)

#Bloco de saída de dados
print(f"Valor final a ser pago: {c:.2f}")
