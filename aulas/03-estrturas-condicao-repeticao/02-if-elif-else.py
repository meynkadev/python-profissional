#CRIAÇÃO DO PROGRAMA

print("---AVALIAÇÃO DE NOTAS---")

nota = int(input("Digite e nota do aluno: "))

if nota >= 9:
    print("Excelente!")

elif nota >= 7:
    print("Aprovado!")

elif nota >= 5:
    print("Recuperação.")

else:
    print("Reprovado.")

    