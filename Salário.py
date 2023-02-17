#Bloco de Apresentação do Programa
print('Sistema para cálculo de reajuste salarial')

#Bloco de Recebimento de dados
salario=float(input('Digite o salário do funcionário:'))

#Bloco de Processamento de Dados
if salario > 1250:
    total = salario * (10 / 100)

else:
    total = salario * (15 / 100)

#Bloco de Saída de Dados
print('Antigo Salário:', salario)
print('Salário reajustado', salario+total)