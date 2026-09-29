#dicionarios em python - Aula 01
#Objetivo: praticar criacao, acesso, alteracao, iteracao e remocao.

#1. Criacao
person = {
    "name": "Meynkâ",
    "age": 25,
    "language": "Python"
}

print(person)

#2. Acesso por chave
print(person["name"])
print(person["language"])

#3. Alteracao de valor
person["age"] = 26
print(person)

#4. Adicao de uma nova chave
person["city"] = "Porto Alegre"
print(person)

#5. get()
print(person.get("email"))
print(person.get("email", "Not informed"))

#6. Verificacao de chave
print("name" in person)
print("email" in person)

#7. Percorrendo as chaves
for key in person:
    print(key)

#8. keys
for key in person.keys():
    print(key)

#9. values()
for value in person.values():
    print(value)

#10. items()
for key, value in person.items():
    print(key, value)

#11. pop()
product = {
    "name": "Notebook",
    "price": 3500,
    "stock": 10
}

removed_price = product.pop("price")

print(removed_price)
print(product)

#12. del
del product["stock"]
print(product)

#13. popitem()
product = {
    "name": "Notebook",
    "price": 3500,
    "stock": 10 
}

removed_item = product.popitem()

print(removed_item)
print(product)

#14. clear()
product.clear()
print(product)