#CRIANDO UMA CLASSE

#uma classe é um molde/modelo
#quero definir um molde/modelo de objeto chamado Carro
class Carro:
    pass #pass significa não colocamos implementação dentro da classe

#CRIANDO UM OBJETO

#agora criamos um objeto a partir do molde/modelo da classe carro
carro1 = Carro() #carro1 passa a representar u carro de verdade

#ATRIBUTOS
#são dados ou características do objeto
#"O que este objeto TEM?"
carro1.modelo = "Civic"
carro1.cor = "Preto"
carro1.ano = 2025

print(carro1.modelo)
print(carro1.cor)
print(carro1.ano)

#OUTRO OBJETO
#uma classe pode gerar vários objetos
#carro2 pertence à mesma classe de carro1, mas seus dados podem ser diferentes
carro2 = Carro()

carro2.modelo = "Corolla"
carro2.cor = "Branco"
carro2.ano = "2026"

print(carro2.modelo)
print(carro2.ano)
print(carro2.cor)


# OBJETOS POSSUEM SEUS PRÓPRIOS DADOS
# Alterar o atributo de carro1 não altera automaticamente
# o atributo correspondente de carro2
carro1.cor = "Vermelho"

print(carro1.cor)
print(carro2.cor)

#MÉTODOS
#é uma função definida dentro de uma classe. Representa o que o objeto faz
class Banda:

    def tocar_musica(self):#self representa o objeto banda_Camel
        print("A banda está tocando")

    def mudar_musica(self):
        print("A banda mudou de música")

banda_Camel = Banda()

banda_Camel.tocar_musica()
banda_Camel.mudar_musica()

#EXERCICIO

class Bicicleta:

    def __init__(self, cor, modelo, ano, marca):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def Buzinar(self):
        print("Plim Plim....")

    def Andar(self):
        print("Andando.....")

    def Parar(self):
        print("Parando....")


bicicleta_1 = Bicicleta("verde", "passeio", 1998, "Caloi")
bicicleta_1.Andar()
bicicleta_1.Buzinar()
bicicleta_1.Parar()
print(bicicleta_1)