# Aula 2 — Métodos de Dicionários
# Exemplos práticos dos métodos estudados.

# 1. update()

product = {
    "name": "Keyboard",
    "price": 150,
    "stock": 20
}

product.update({
    "price": 180,
    "brand": "Logitech"
})

print(product)


# 2. setdefault()

user = {
    "name": "Carlos",
    "age": 30
}

user.setdefault("city", "Porto Alegre")
user.setdefault("age", 40)  # A chave já existe; o valor permanece 30.

print(user)


# 3. copy()

original = {
    "name": "Carlos",
    "age": 30
}

backup = original.copy()
backup["age"] = 50

print(original)
print(backup)


# 4. fromkeys()

fields = ["name", "email", "phone"]
contact = dict.fromkeys(fields, "")

print(contact)


# 5. pop()

product = {
    "name": "Notebook",
    "price": 3500,
    "stock": 10
}

removed = product.pop("price")

print(product)
print(removed)


# 6. popitem()

data = {
    "a": 10,
    "b": 20,
    "c": 30
}

key, value = data.popitem()

print(data)
print(key, value)


# 7. clear()

user = {
    "name": "Carlos",
    "age": 30,
    "city": "Porto Alegre"
}

user.clear()

print(user)


# 8. keys()

user = {
    "name": "Carlos",
    "age": 30,
    "city": "Porto Alegre"
}

for key in user.keys():
    print(key)


# 9. values()

for value in user.values():
    print(value)


# 10. items() + desempacotamento

for key, value in user.items():
    print(key, value)


# 11. items() sem desempacotamento

for item in user.items():
    print(item)


# 12. Exercício integrado

user = {
    "name": "Carlos",
    "age": 30,
    "email": "carlos@email.com"
}

user.update({"age": 31})
user.setdefault("city", "Porto Alegre")

phone = user.get("phone", "Not informed")

for key, value in user.items():
    print(key, value)

print(phone)


#testes pessoais
user = {
    "name": "Carlos",
    "age": 30,
    "email": "carlos@email.com"
}

#1. Atualizar a idade para 31
user.update({"age": 31})
print(user)

#2. Adicionar chave "city" com o valor "Porto Alegre"
user.setdefault("city", "Porto Alegre")
print(user)

#3. Tentar obter o "phone" sem gerar KeyError. Caso não exista, retornar "Not informed"
print(user.get("phone", "Not informed"))

#4. Percorrer o dicionário mostrando cada chave junto com seu valor
for key, value in user.items():
    print(key, value)