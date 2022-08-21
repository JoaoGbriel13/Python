import numpy

preco = numpy.array([72.35, 43.93, 17.84, 23.19])
loja1 = numpy.array([373, 1228, 4135, 1139])
loja2 = numpy.array([558, 1448, 2059, 1450])
loja3 = numpy.array([358, 907, 3122, 843])

estoque1 = sum(loja1)
estoque2 = sum(loja2)
estoque3 = sum(loja3)

print(f'O estoque da loja 1 é de: {estoque1}')
print(f'O estoque da loja 2 é de: {estoque2}')
print(f'O estoque da loja 3 é de: {estoque3}')

produto1 = numpy.sum([loja1[0],loja2[0],loja3[0]])
produto2 = numpy.sum([loja1[1],loja2[1],loja3[1]])
produto3 = numpy.sum([loja1[2],loja2[2],loja3[2]])
produto4 = numpy.sum([loja1[3],loja2[3],loja3[3]])

print(f'O total de estoque do produto 1 é de {produto1}')
print(f'O total de estoque do produto 2 é de {produto2}')
print(f'O total de estoque do produto 3 é de {produto3}')
print(f'O total de estoque do produto 4 é de {produto4}')

redeEstoque = estoque1 + estoque2 + estoque3
print(f'O estoque total da rede é de {redeEstoque}')

loja1Orçamento = preco[0] * loja1[0] + preco[1] * loja1[1] + preco[2] * loja1[2] + preco[3] * loja1[3]
loja2Orçamento = preco[0] * loja2[0] + preco[1] * loja2[1] + preco[2] * loja2[2] + preco[3] * loja2[3]
loja3Orçamento = preco[0] * loja3[0] + preco[1] * loja3[1] + preco[2] * loja3[2] + preco[3] * loja3[3]

print(f'O valor total da loja 1 é de R$ {loja1Orçamento:,.2f}')
print(f'O valor total da loja 2 é de R$ {loja2Orçamento:,.2f}')
print(f'O valor total da loja 3 é de R$ {loja3Orçamento:,.2f}')


valorProduto1 = produto1 * preco[0]
valorProduto2 = produto2 * preco[1]
valorProduto3 = produto3 * preco[2]
valorProduto4 = produto4 * preco[3]

print(f'O valor total em produto 1 é de R${valorProduto1: ,.2f}')
print(f'O valor total em produto 2 é de R${valorProduto2: ,.2f}')
print(f'O valor total em produto 3 é de R${valorProduto3: ,.2f}')
print(f'O valor total em produto 4 é de R${valorProduto4: ,.2f}')

valorGeral = valorProduto1 + valorProduto2 + valorProduto3 + valorProduto4
print(f'O valor total na rede é de R$ {valorGeral:,.2f}')






