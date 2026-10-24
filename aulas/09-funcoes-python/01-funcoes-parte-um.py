#FUNÇÃO SIMPLES
def say_hello():
    # Uma função pode executar uma ação sem receber informações
    # externas e sem precisar retornar um valor.
    print("Olá, python")

say_hello()

#-------------------------------------------

#FUNÇÃO COM PARÂMETROS
def greet(name):
    #name é o parâmetro
    #Ele vai funcionar como uma variável que receberá o valor
    #quando a função for chamada.
    print(f"Olá, {name}")

greet("Meynkadev")

#-------------------------------------------

#PARÂMETRO X ARGUMENTO
def calculate_square(number):
    #number é o parâmeto definido na função
    return number ** 2

#o valor 5 é o argumento eviado para a função
result = calculate_square(5)

#a função retorna 25, então 25 foi armazenado em result
print(result)

#------------------------------------------

#RETURN X PRINT

def add(a, b):
    #return devolve o resultado para quem chamou a função
    #Ele não serve simplesmente para exibir o resultado na tela
    return a + b

result = add(10, 5)

#como o resultado foi retornado, podemos armazená-lo
#reultiliza-lo ou passá-lo para outra função
print(result)

def show_sum(a, b):
    #Aqui temos print em vez de return
    #O resultado aparece na tela, mas não pé devolvido
    #pela função para ser reultilizado posteriormente
    print(a + b)

show_sum(10, 5)

#---------------------------------------------

#RASTREANDO O VALOR DE RETURN
def multiply(number, multiplier):
    #suponha que a chamada seja multiply(4, 3)
    #
    #number recebe 4
    #multiplier recebe 3
    #
    #a expressão abaixo será
    #4 * 3
    #
    #O resultado 12 será devolvido pelo return
    return number * multiplier

result = multiply(4, 3)
print(result)

#----------------------------------------------

#RETURN ENCERRA A FUNÇÃO
def chek_number(number):
    if number > 10:
    #se esta condição for verdadeira, a função retorna
    #maior e termina imediatamente
    #
    #o código abaixo deste return não será executado
        return "Maior"

    #este return só será alcançado quando number não for
    #maior que 10
    return "Menor"

result = chek_number(9)
print(result)

#------------------------------------------------

#VÁRIOS CAMINHOS DE EXECUÇÃO
def analyze_number(number):
    if number > 20:
        #para valores maiores que 20 este é o primeiro caminho
        return "alto"

    if number > 10:
        #este caminho só será alcançado se o primeiro if for false
        return "médio"

    #este caminho só será usado se as duas condições
    #anteriores forem falsas
    return "baixo"

print(analyze_number(25))
print(analyze_number(15))
print(analyze_number(9))

#---------------------------------------------

#RETURN COM UMA EXPRESSÃO
def calculate_discount(price):
    if price >= 100:
        #o python primeiro calcula a expressão:
        # price * 0.90
        # 
        # depois o valor calculado é retornado
        return price * 0.90

    #se o preço for menor que 100 devolvemos o próprio preço
    return price

result = calculate_discount(150)
print(result)

#FUNÇÃO COM MAIS DE UM PARÂMETRO
def calculate_total(price, quantity):
    # cada parâmetro recebe seu próprio argumento 
    # 
    # exemplo:
    # price = 25
    # quantity = 4
    #
    # o resultado será = 100
    return price * quantity

total = calculate_total(25, 4)
print(total)

#---------------------------------------

#FUNÇÃO RETORNANDO UMA STRING
def get_status(age):
    if age >= 18:
        return "Maior de idade"

    return "Menor de idade"

status = get_status(20)
print(status)

#O RETURN PODE SER USADO EM OUTRA EXPRESSÃO
def double(number):
    return number * 2

#a função retorna 10
#esse 10 pode ser usado com argumento de outra função
result = double(5)
print(result)

def result_multi(result, number):
    return result * number

result_final = result_multi(result, 4)
print(result_final)

#-------------------------------------

#FUNÇÃO RETORNANDO BOOLEANO
def is_positive(number):
    if number > 0:
        return True
    
    return False

result = is_positive(2)
print(result)

#----------------------------------

#EXERCÍCIO DE PRÁTICA
def classify_age(age):
    if age < 13:
        return "criança"

    if age >= 13 and age <= 17:
        return "adolescente"

    return "adulto"

result = classify_age(18)
print(result)

#---------------------------------

#EXERCÍCIO DE PRÁTICA
def classify_temperature(temperature):
    if temperature < 15:
        return "frio"

    if temperature >= 15 and temperature <= 25:
        return "agradável"

    return "quente"

result_temperature = classify_temperature(26)
print(result_temperature)
    