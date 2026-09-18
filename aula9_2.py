turma = []

for i in range(5):
#CHAVE 1 - nome
    turma.append({"nome":input("Digite o nome do aluno: ")})


    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

#CHAVE 2 - media 
    media = (nota1 + nota2) / 2
    turma[i].update({"media": media})
    print(media)

    #CHAVE 3 - status
if turma [i]["media"]>= 7:
    turma[i].update({"status":"Aprovado"})
elif turma [i]["media"]>= 5 <= 6.9:
    turma[i].update({"status":"recuperação"})
else:
    turma[i].update({"status": "reprovado"})

for i in range(5):
    print("nome do aluno: ", turma[i]["nome"])
    print("media do aluno: ", turma[i]["media"])
    print("status do aluno: ", turma[i]["status"])