# Entrada
valor_total = float(input("Valor total da compra: R$"))

# Decisão do valor da porcentagem de desconto conforme o valor
if valor_total < 200:
  porcentagem = 5
elif valor_total < 300: 
  porcentagem = 10
else:
  porcentagem = 15

# Calculo do desconto e o valor final
desconto = valor_total * porcentagem / 100
valor = valor_total - desconto

# Saída
print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Valor total a pagar: R${valor:.2f}")
