# Python — Módulo 10
## Programação Orientada a Objetos: Construtores e Destrutores

**Objetivo:** entender como uma instância é inicializada, como recebe atributos, como funcionam os valores padrão, como validar e calcular dados durante a inicialização e qual é o papel de `__del__()`.

---

## 1. O método `__init__()`

Quando criamos um objeto, muitas vezes precisamos fornecer informações iniciais. Em Python, o método associado à inicialização é:

```python
def __init__(self):
    ...
```

Ele é chamado automaticamente quando uma instância é criada.

**Precisão técnica:** é comum chamar `__init__()` de construtor no aprendizado. Tecnicamente, ele é o inicializador: `__new__()` cria e retorna a instância; `__init__()` prepara essa instância.

### Exemplo

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Marina", 28)
```

Ao criar `pessoa1`, o Python chama `__init__()` e passa `"Marina"` e `28`.

---

## 2. Entendendo `self`

`self` representa a própria instância que está sendo inicializada ou utilizada.

```python
self.nome = nome
```

- `self.nome`: atributo armazenado no objeto.
- `nome`: parâmetro que recebe o valor enviado na criação.

Uma forma de pensar:
- O parâmetro é a informação que chega.
- O atributo é a informação guardada no objeto.

Cada instância possui seus próprios valores:

```python
pessoa1 = Pessoa("Marina", 28)
pessoa2 = Pessoa("Rafael", 35)

print(pessoa1.nome)  # Marina
print(pessoa2.nome)  # Rafael
```

---

## 3. Parâmetros com valores padrão

Podemos definir um valor utilizado quando o argumento não é informado.

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

conta1 = Conta("Ana")
conta2 = Conta("Pedro", 500)
```

- `conta1.saldo` será `0`, pois o argumento foi omitido.
- `conta2.saldo` será `500`, pois esse valor foi informado.

**Regra:** o valor padrão só é utilizado quando o argumento correspondente não é fornecido. Ele não obriga todos os objetos a terem o mesmo valor.

---

## 4. Atributos calculados no inicializador

O `__init__()` pode calcular informações além de armazenar os argumentos recebidos.

```python
class Pedido:
    def __init__(self, cliente, produto, quantidade, preco_unitario):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.valor_total = quantidade * preco_unitario

pedido1 = Pedido("Ana", "Teclado", 2, 150)
print(pedido1.valor_total)  # 300
```

Passamos quatro argumentos, mas o objeto termina com cinco atributos. `valor_total` é calculado durante a inicialização:

`valor_total = quantidade * preco_unitario`

Isso é útil quando o objeto precisa guardar dados recebidos e informações derivadas deles.

---

## 5. Validando dados durante a inicialização

Um objeto deve começar em um estado coerente com as regras do sistema.

```python
class Funcionario:
    def __init__(self, nome, salario):
        if not nome:
            raise ValueError("O nome é obrigatório.")

        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")

        self.nome = nome
        self.salario = salario
```

- `raise` levanta uma exceção.
- `ValueError` indica um valor inadequado.
- A mensagem explica o problema.

Se a validação falhar, a inicialização normal é interrompida.

**Aplicação profissional:** o inicializador pode impedir que objetos sejam criados com dados que violem as regras do sistema.

---

## 6. Valor padrão combinado com cálculo

```python
class Compra:
    def __init__(self, produto, quantidade, preco=50):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        self.total = quantidade * preco

compra1 = Compra("Caderno", 3)
compra2 = Compra("Caneta", 5, 4)
```

| Atributo | `compra1` | `compra2` |
|---|---:|---:|
| Produto | Caderno | Caneta |
| Quantidade | 3 | 5 |
| Preço | 50 | 4 |
| Total | 150 | 20 |

No primeiro objeto, `preco` utiliza o padrão `50`. No segundo, o argumento `4` substitui o padrão.

---

## 7. Alterar um atributo não executa `__init__()` novamente

```python
compra1 = Compra("Caderno", 3)
compra1.quantidade = 10

print(compra1.quantidade)  # 10
print(compra1.total)       # 150
```

O total continua `150` porque o cálculo foi executado durante a inicialização. Alterar `quantidade` depois não executa novamente o `__init__()` e não recalcula automaticamente `total`.

Quando um atributo depende de outro, precisamos decidir como manter essa relação atualizada. Uma solução é criar um método de instância para recalcular o total — assunto que será aprofundado nas próximas aulas.

---

## 8. O método `__del__()`

O método especial `__del__()` pode ser chamado quando uma instância está sendo finalizada.

```python
class Exemplo:
    def __init__(self, identificacao):
        self.identificacao = identificacao
        print("Objeto inicializado.")

    def __del__(self):
        print("Objeto sendo finalizado.")
```

Ele é conhecido informalmente como destrutor. É mais preciso entendê-lo como um método de finalização.

### O que faz `del objeto`?

```python
objeto = Exemplo("A")
del objeto
```

`del objeto` remove a referência chamada `objeto`. Isso **não garante que o objeto será destruído naquele exato instante**. Se outras referências apontarem para a mesma instância, ela continuará acessível por elas.

O momento da finalização depende do gerenciamento de memória da implementação do Python.

### Cuidado profissional

Não dependa de `__del__()` para fechar arquivos, conexões com bancos de dados ou outros recursos importantes. O momento da finalização não é uma garantia adequada para esse tipo de tarefa.

---

## 9. Gerenciamento de recursos com `with`

Para arquivos, prefira:

```python
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, Python!")
```

Ao sair do bloco `with`, o arquivo é fechado automaticamente, inclusive se ocorrer uma exceção dentro do bloco.

Esse mecanismo é chamado de **gerenciamento de contexto**. Também pode ser utilizado com outros recursos que implementam o protocolo de gerenciador de contexto.

---

## 10. Resumo para consulta

| Conceito | Função |
|---|---|
| `__init__()` | Inicializa a instância e prepara seus atributos |
| `self` | Referência à própria instância |
| Parâmetro padrão | Valor utilizado quando o argumento não é informado |
| Atributo | Dado armazenado no objeto |
| Atributo calculado | Informação derivada de outros dados durante a inicialização |
| `raise ValueError` | Levanta uma exceção relacionada a um valor inadequado |
| `__del__()` | Método de finalização, sem garantia de execução em momento específico |
| `del objeto` | Remove uma referência; não garante destruição imediata |
| `with` | Gerencia a entrada e a saída de um contexto, como o fechamento de arquivos |

### Ideias principais

1. `__init__()` é chamado automaticamente durante a criação de uma instância.
2. `self` permite armazenar informações no próprio objeto.
3. Cada instância possui seus próprios valores de atributos.
4. Parâmetros padrão são usados quando os argumentos correspondentes são omitidos.
5. O inicializador pode validar dados e calcular atributos.
6. Alterar um atributo depois da inicialização não executa novamente o `__init__()`.
7. Não devemos depender de `__del__()` para liberar recursos importantes; prefira mecanismos explícitos, como `with`.

---

## 11. Prática recomendada

Use o arquivo `modulo_10_construtores_destrutores_pratica.py` para executar os exemplos e resolver os desafios:

- Crie uma classe `Livro` com título, autor e número de páginas com valor padrão.
- Crie uma classe `Produto` que calcule o valor total em estoque.
- Adicione validações para impedir valores negativos.
- Altere a quantidade de uma compra e observe por que o total não é atualizado automaticamente.
- Crie um método `atualizar_total()` para recalcular esse valor.

**Objetivo:** conseguir explicar o que acontece desde a criação de um objeto até o momento em que seus atributos ficam disponíveis para uso.
