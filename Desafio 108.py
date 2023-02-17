import moeda

p = float(input('Digite um valor R$:'))
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'10% a + de {p} é {moeda.aumentar(p)}')
print(f'10% a - de {p} é {moeda.diminuir(p)}')