idade = 22
possui_cnh = True

print(f"A pessoa é maior de idade? {idade >= 18}")

print(f"A pessoa possui CNH? {possui_cnh}")

print(f"Ela pode dirigir? {idade >= 18 and  possui_cnh}")

print(f"Ela atende pelo menos um dos requisitos? {idade >= 18 or possui_cnh}")

print(f"O oposto de possuir CNH é: {not possui_cnh}")

print()
print("-" * 20)
print()

usuario = "admin"
senha = "123456"

login_valido = usuario == "admin" and senha == "123456"
print(f"Login válido: {login_valido}")
print(f"Login inválido: {not login_valido}")
