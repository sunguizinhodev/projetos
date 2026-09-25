def main():
  print(pesquisa(50))
  return

def pesquisa(candidatos: int):

  excelente = 0
  bom = 0
  ruim = 0

  for i in range(candidatos):

    print(f'\nCandidato #{i + 1}')
    input('Digite seu nome:\n')
    input('Digite sua idade:\n')
    opiniao = int(input('Como foi seu atendimento?\n1: Excelente\n2: Bom\n3: Ruim\nOpção:\n'))

    if opiniao == 1:
      excelente += 1
    elif opiniao == 2:
      bom += 1
    elif opiniao == 3:
      ruim += 1
    else:
      print("Opção inválida, não contabilizada.")

  return f"\nResultado:\nExcelente: {excelente}\nRuim: {ruim}"

main()