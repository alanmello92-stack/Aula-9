candidatos = []

for i in range (2):
    idade = int(input("Digite a idade do candidato: "))
    
    if idade >= 18:

        maior_de_idade = {}
        
        maior_de_idade.update({'idade':idade})
        maior_de_idade.update({'nome':input("Digite o nome do candidato: ")})
        maior_de_idade.update({'nascimento':input("Digite sua data de nascimento (separada por /): ")})
        maior_de_idade.update({'telefone':input("Digite seu telefone: ")})
        maior_de_idade.update({'email':input("Digite seu email: ")})
        maior_de_idade.update({'formação':input("Qual sua formação? ")})

        candidatos.append(maior_de_idade)
        
    else: continue


for candidato in candidatos:
    print(candidato['idade'], candidato['nome'], candidato['nascimento'], candidato['telefone'], candidato['email'], candidato["formação"])
