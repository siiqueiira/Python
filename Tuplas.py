                    #AULA DE TUPLA

# --------------------------------------------------------------

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#len mostra a quantidade de itens em uma tupla

#--------------------------------------------------------------

for comida in lanche:
    print(f'Eu vou comer {comida}')

#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')

#for cont in range (0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#print(sorted(lanche)) #[] vira uma lista

#--------------------------------------------------------------

#a = (2, 5 , 4)
#b = (5, 8 , 1, 2)
#c = b + a
#print(f'O número de componentes é {len(c)}, sendo eles:', c)
#print(c.count(5))
#print(c)
#print(c.index(5, 1))