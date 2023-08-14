valorHamburguer = 10.00
quantidadeHamburguer = 2
valorBebida = 5.00
quantidadeBebida = 1
valorPago = 30.00

# Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebidas = valorBebida * quantidadeBebida
total = totalHamburguer + totalBebidas

# Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
troco = valorPago - total

# Imprimir a saída .
print(f"O preço final do pedido é R$ {total:.2f}. Seu troco é R$ {troco:.2f}.")
