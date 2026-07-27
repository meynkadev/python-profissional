print("EXERCÍCIO 1")
print()

#variável que aponta para o valor inicial
numero = 1

#estrutura do bloco while
while numero <= 5:#determina a condição
    print(numero) #exibe a atual condição de cada repetição+
    numero += 1 #acrescenta adição de mais 1 a cada ciclo

print()
print("Fim")#após sair da condição verdadeira, vai para linha 17

print("-" * 20)
print()

#-----------------------

print("EXERCÍCIO 2")
print()

andar = 1 #variável que aponta para o valor inicial

while andar <= 10:#determina a condição
    print(f"Andar atual: {andar}") #exibe a atual condição de cada repetição
    andar += 1#acrescenta adição de mais 1 a cada ciclo


print()
print("Cheguei!")#após sair da condição verdadeira

print("-" * 20)
print()

#-----------------------

print("EXERCÍCIO 3")
print()

frutas = [
    "Maçã",
    "Banana",
    "Uva",
    "Laranja"
]

for fruta in frutas:#for percorre cada elemento da lista
    print(fruta)#exibe cada elemento percorrido 

print()
print("Fim da lista")

print("-" * 20)
print()

#-------------------------

print("EXERCÍCIO 4")
print()

#criação da lista
produtos = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor"
]

for produto in produtos:#for percorre cada elemento da lista
    print(f"Produto: {produto}")#exibe cada elemento percorrido

print()
print("Fim da lista")