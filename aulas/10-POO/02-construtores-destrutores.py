# 1. __init__: inicializando atributos
class Pessoa:
    def __init__(self, nome, idade):
        # self representa a instância que está sendo inicializada.
        # Os valores recebidos são armazenados nos atributos do objeto.
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Marina", 28)
pessoa2 = Pessoa("Rafael", 35)

print("\n1. PESSOAS")
print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)

#2. Parâmetro com valor padrão
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

#Sem informar saldo: utiliza o padrão 0
conta1 = Conta("Meynkâ")

#inforando o saldo: 500 substitui o valor padrão
conta2 = Conta("Pedro", 500)

print("\n2. CONTAS")
print(conta1.titular, conta1.saldo)
print(conta2.titular, conta2.saldo)


#3. Atributo criando durante inicialização
class Pedido:
    def __init__(self, cliente, produto, quantidade, preco_uitário):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitário = preco_uitário

        #Este atributo não foi passado como argumento
        #O próprio _init_ calcula e armazena o resultado
        self.valor_total = quantidade * self.preco_unitário


pedido1 = Pedido("Ana", "Teclado", 2, 150)

print("\n3. PEDIDO")
print("Cliente: ", pedido1.cliente)
print("Produto: ", pedido1.produto)
print("Quantidade :", pedido1.quantidade)
print("Preço unitário: ", pedido1.preco_unitário)
print("Valor Total: ", pedido1.valor_total)

#4. Validando informações no construtor
class Funcionario:
    def __init__(self, nome, salario):
        #verificamos os dados antes de armazená-los
        if not nome:
            raise ValueError("O nome é obrigatório")
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")

        self.nome = nome
        self.salario = salario

print("\n4. FUNCIONÁRIO")
Funcionario1 = Funcionario("Carlos", 1500)
print(Funcionario1.nome, Funcionario1.salario)

#5. Valor padrão combinado combinado com calculo

class Compra: 
    def __init__(self, produto, quantidade, preco=50):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        self.total = quantidade * preco


compra1 = Compra("Cadero", 3)
compra2 = Compra("Caneta", 5, 4)

print("\n5. COMPRAS")
print(compra1.produto, compra1.preco, compra1.total)
print(compra2.produto, compra2.preco, compra2.total)

#6. Alterar atributo não executa _init_ novamente
compra1.quantidade = 10

print("\n6. ALTERAÇÃO POSTERIOR")
print("Quantidade atual:", compra1.quantidade)
print("Total armazenado:", compra1.total)

# 7. Demonstração de __del__
class ExemploFinalizacao:
    def __init__(self, identificacao):
        self.identificacao = identificacao
        print(f"Objeto {self.identificacao} inicializado.")

    def __del__(self):
        # Método de finalização. Não dependa dele para tarefas críticas.
        print(f"Objeto {self.identificacao} sendo finalizado.")

print("\n7. FINALIZAÇÃO")
objeto = ExemploFinalizacao("A")
del objeto  # Remove esta referência; não garante destruição imediata.


# 8. Para arquivos, prefira with
print("\n8. GERENCIAMENTO DE ARQUIVO")
with open("exemplo_pratica_python.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Praticando gerenciamento de contexto em Python.\n")
# Ao sair do bloco, o arquivo é fechado automaticamente.