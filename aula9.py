resultado = {}
turma = []

for i in range(5):
#CHAVE 1 - nome
    resultado.update({"nome":input("Digite o nome do aluno: ")})


    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

#CHAVE 2 - media 
    media = (nota1 + nota2) / 2
    resultado.update({"media": media})
    print(media)

    #CHAVE 3 - status
if media >= 7:
    resultado.update({"status": print("Aprovado")})
elif media >= 5 <= 6.9:
    resultado.update({"status": print("Recuperação")})
else:
    resultado.update({"status": print("Reprovado")})

