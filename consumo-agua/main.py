# Função Main
def main():
  tipo = input('Tipo de Imóvel: ')
  consumo_agua = float(input('Consumo mensal de água (m³): '))

  classificar_consumo(tipo, consumo_agua)

# Classifica o consumo
def classificar_consumo(tipo: str, consumo_agua: float):
  if tipo == "comercial":
    return print("Tarifa comercial aplicada - consulte o plano corporativo.")
  elif tipo == "apartamento" and consumo_agua < 10:
    return print("Consumo econômico - excelente controle de água!")
  elif (tipo == "apartamento" or tipo == "casa") and consumo_agua <= 25:
    return print("Consumo moderado - dentro do padrão residencial.")
  else:
    return print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
  

main()