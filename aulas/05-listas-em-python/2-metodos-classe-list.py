frutas = ["Maçã", "Banana"]

# Adicionando elementos
frutas.append("Uva")
frutas.insert(1, "Laranja")
frutas.extend(["Morango", "Pera"])

print(frutas)

# Consultando elementos
print(frutas.index("Uva"))
print(frutas.count("Banana"))

# Removendo elementos
frutas.remove("Banana")
item = frutas.pop(0)

print(item)
print(frutas)

# Organizando a lista
frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)