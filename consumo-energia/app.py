nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia(W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_mensal = consumo_mensal * 0.75
print(f"Aparelho: {nome}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R${custo_mensal:.2f}")