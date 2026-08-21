# Exemplos — Módulo 6: Tuplas em Python

# 1. Criando uma tupla
# Objetivo: armazenar uma sequência fixa de valores.
languages = ("Python", "Java", "C++")
print(languages)

# 2. Tupla vazia
# Objetivo: representar uma tupla sem elementos.
empty_tuple = ()
print(empty_tuple)

# 3. Tupla com um elemento
# Objetivo: criar uma tupla contendo apenas um valor.
number = (10,)
print(number)

# 4. Acessando elementos
# Objetivo: obter um elemento específico pelo índice.
print(languages[0])

# 5. Índice negativo
# Objetivo: acessar elementos a partir do final da tupla.
print(languages[-1])

# 6. Slicing
# Objetivo: obter uma parte da tupla.
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# 7. len()
# Objetivo: descobrir quantos elementos existem.
print(len(numbers))

# 8. Percorrendo uma tupla
# Objetivo: processar cada elemento da sequência.
for language in languages:
    print(language)

# 9. Imutabilidade
# Objetivo: demonstrar que elementos de uma tupla não podem ser alterados.
person = ("Meynkâ", 25, "Python")
# person[0] = "Carlos"  # TypeError

# 10. Desempacotamento (unpacking)
# Objetivo: distribuir os valores da tupla em variáveis.
name, age, language = person

print(name)
print(age)
print(language)

# 11. Atribuição múltipla
# Objetivo: trocar valores entre variáveis de forma simples.
a = 10
b = 20

a, b = b, a

print(a)
print(b)

# 12. count()
# Objetivo: contar quantas vezes um valor aparece.
values = (10, 20, 10, 30, 10)
print(values.count(10))

# 13. index()
# Objetivo: encontrar o índice da primeira ocorrência de um valor.
print(values.index(10))

# 14. Escolhendo entre list e tuple
# Objetivo: usar uma lista quando os dados precisam ser alterados.
cart = ["Notebook", "Mouse"]
cart.append("Keyboard")
print(cart)

# Objetivo: usar uma tupla quando os dados devem permanecer fixos.
coordinates = (10, 20)
print(coordinates)


product = ("Notebook", 3500.00, "Dell")
name, price, brand = product

print(f"Produto: {name}\nPreço: {price}\nMarca: {brand}")

print()

user = ("Meynkâ", "Python Developer", True)
nome, profissao, ativo = user

print(f"Nome: {nome}\nProfissão: {profissao}\nAtivo: {ativo}")

