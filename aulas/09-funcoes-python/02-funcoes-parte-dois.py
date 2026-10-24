#ARGUMENTOS NOMEADOS
def create_user(name, age, city):
    return f"{name} tem {age} anos e mora em {city}."

result = create_user(name="Ana", age=25, city="Porto Alegre")
print(result)

#CHAMADAS MISTURANDO ARGUMENTOS NOMEADOS E POSICIONAIS
result = create_user("Ana", age=25, city="Porto Alegre")
print(result)

#------------------------------------------

# *args permite que uma função receba uma quantidade
# variável de argumentos posicionais.
def calculate_sum(*numbers): # O Python reúne os valores recebidos dentro de uma TUPLA.
    total = 0
    for number in numbers:
        total += number

    return total

result = calculate_sum(10, 20, 10) 
print(result)

result = calculate_sum(25, 25, 10, 10, 10)
print(result)

# o que existe dentro de args?
def show_arguments(*args):
    print("Valores recebidos:")
    print(args)

    print("Tipo:")
    print(type(args))

show_arguments(1, "Oi", 1.80)

#**kwargs funciona de maneira semelhante ao *args,
# mas trabalha com ARGUMENTOS NOMEADOS.
#Os valores são reunidos em um DICIONÁRIO

def show_options(**kwargs):
    print("Valores recebidos:")
    print(kwargs)

    print("Tipo:")
    print(type(kwargs))

show_options(band="Camel", guitar="Andy Latimer", bass="Collin Bass")

#percorrendo kwargs
def show_user_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_user_data(name="Meynkâ", age=23, profession="Developer", city="Capela de Santana")

#*args + **kwargs
def show_data(*args, **kwargs):
    print("Argumentos posicionais:")
    print(args)

    print("Argumentos nomeados:")
    print(kwargs)

show_data(
    1903,
    3,
    time="Grêmio",
    jogador="Renato Gaúcho"
)

#-----------------------------------------

# PARÂMTROS ESPECIAIS /
# O "/" indica que os parâmetros anteriores a ele
# são SOMENTE POSICIONAIS.
def calculate_total(price, quantity, /):
    return price * quantity

result = calculate_total(3, 7)
print(result)

# O "*" funciona de maneira diferente.
# Os parâmetros que aparecem DEPOIS dele precisam
# ser fornecidos por nome.

def create_product(*, name, price):
    return f"{name}: R${price}"

result = create_product(name="Notebook", price=3.500)
print(result)

#---------------------------------------------

#OBJETOS DE PRIMEIRA CLASSE
# Em Python, funções são objetos de primeira classe.
# Isso significa que uma função pode ser tratada como
# um valor.
# Podemos, por exemplo, colocar uma função dentro de
# uma variável
def square(number):
    return number ** 2

operation = square
result = operation(2)
print(result)

#outra função como objeto
def double(number):
    return number * 2

operation = double
result = operation(10)
print(result)

#passando uma função para outra função
def square(number):
    return number ** 2

def double(number):
    return number * 2

def execute_operation(operation, number):
    return operation(number)

execute_operation = square
result = execute_operation(5)
print(result)

#--------------------------------------------

#ESCOPO LOCAL
def test_local_scope():
    message = "Olá, dentro da função!"
    print(message)

test_local_scope()

#ocorre erro porque a variável é local dentro da função

#ESCOPO GLOBAL
message = "Olá escopo global"

def show_global_message():
    print(message)

show_global_message()

#MESMO NOME, ESCOPOS DIFERENTES
name = "Maria"

def show_name():
    name = "João"
    print("Dentro da função:", name)

show_name()
print("Fora da função:", name)

#EXERCÍCIOS
# Agora vamos aproximar os conceitos de uma situação
# que poderia aparecer em uma aplicação.
# Imagine um sistema que precisa gerar um pequeno relatório
# de pedido
# customer → cliente
# *products → quantidade variável de produtos
# **options → configurações do pedido
def create_report(custumer, *products, **options):
    
    print(f"Cliente: {custumer}")

    print("\nProdutos:")

    for product in products:

        print(f"- {product}")

    print("\nConfigurações:")

    for key, value in options.items():

        print(f"- {key}: {value}")


relatorio = create_report(
    "Meynkâ",
    "Notebook",
    "Mouse",
    "Teclado",
    delivery="express",
    payment="credit_card"
)

#------------------------------------------
def process_numbers(*args, operation):

    if operation == "sum":
        return sum(args)

    elif operation == "max":
        return max(args)

    elif operation == "min":
        return min(args)

result = process_numbers(1, 2, 6, 8, operation="sum")
print(result)

result = process_numbers(1, 2, 6, 8, operation="max")
print(result)

result = process_numbers(1, 2, 6, 8, operation="min")
print(result)