peixes = int(input("Digite quantos kg de peixe foram pescados: "))

def calcular_multa(peixes):
  multa = (peixes-100) * 4
  return multa
valor_da_multa = calcular_multa(peixes)

if peixes > 100:
  calcular_multa(peixes)
  print(valor_da_multa)

else:
  print("Nenhuma cobrança gerada!")