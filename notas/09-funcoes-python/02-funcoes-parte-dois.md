📘 Módulo 9 — Funções
Aula 2 — Argumentos Nomeados, `*args`, `**kwargs`, Parâmetros Especiais, Objetos de Primeira Classe e Escopo
---
🎯 Objetivo da aula
Nesta aula, aprofundamos o uso de funções em Python, aprendendo como:
usar argumentos nomeados;
receber quantidades variáveis de argumentos;
controlar como parâmetros podem ser fornecidos;
tratar funções como valores;
passar funções como argumentos;
compreender escopo local e global;
aplicar esses conceitos em situações próximas do desenvolvimento profissional.
> 💡 **Ideia central:** funções não servem apenas para organizar código. Elas também permitem criar código reutilizável, flexível, legível e mais fácil de manter.
---
1. 🏷️ Argumentos Nomeados
O que são?
Argumentos nomeados são argumentos fornecidos indicando explicitamente o nome do parâmetro.
```python
def create_user(name, age, city):
    return f"{name} tem {age} anos e mora em {city}"
```
Podemos chamar:
```python
create_user(
    name="Ana",
    age=25,
    city="Porto Alegre"
)
```
O Python consegue associar cada valor diretamente ao parâmetro correspondente.
Comparação
Posicionais:
```python
create_user("Ana", 25, "Porto Alegre")
```
Nomeados:
```python
create_user(
    name="Ana",
    age=25,
    city="Porto Alegre"
)
```
🧠 Como pensar
Imagine uma ficha:
```text
Nome:   Ana
Idade:  25
Cidade: Porto Alegre
```
O argumento nomeado funciona como uma etiqueta.
Em vez de depender apenas da posição, dizemos explicitamente qual parâmetro está recebendo o valor.
💼 Uso profissional
Argumentos nomeados são especialmente úteis quando uma função possui vários parâmetros e queremos deixar a chamada mais clara.
```python
send_email(
    recipient="cliente@email.com",
    subject="Pedido aprovado",
    priority="high"
)
```
---
2. 📦 `*args`
O que é?
`*args` permite que uma função receba uma quantidade variável de argumentos posicionais.
```python
def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```
Podemos fazer:
```python
calculate_sum(10, 20)
```
ou:
```python
calculate_sum(10, 20, 30, 40)
```
A função aceita quantidades diferentes de argumentos.
🔎 O que acontece com os valores?
O Python reúne os argumentos em uma tupla.
```python
calculate_sum(10, 20, 30)
```
Conceitualmente:
```python
numbers = (10, 20, 30)
```
Portanto:
```python
type(numbers)
```
seria:
```text
<class 'tuple'>
```
🧠 Visualização
```text
calculate_sum(10, 20, 30)
             │   │   │
             └───┴───┴──────► *numbers
                                │
                                ▼
                         (10, 20, 30)
                                │
                                ▼
                              tupla
```
💡 Importante
O nome `args` é apenas uma convenção.
Isto funciona:
```python
def calculate_sum(*numbers):
    ...
```
O que realmente importa é o `*`.
`*args` é apenas o nome convencional e amplamente utilizado.
---
3. 🗂️ `**kwargs`
O que é?
`**kwargs` permite receber uma quantidade variável de argumentos nomeados.
```python
def show_options(**kwargs):
    print(kwargs)
```
Podemos chamar:
```python
show_options(
    color="blue",
    size="large",
    material="cotton"
)
```
Dentro da função, teremos um dicionário:
```python
{
    "color": "blue",
    "size": "large",
    "material": "cotton"
}
```
🧠 Visualização
```text
show_options(
    color="blue",
    size="large",
    material="cotton"
)
        │
        ▼
     **kwargs
        │
        ▼
   ┌────────────────────────────┐
   │ "color"    → "blue"        │
   │ "size"     → "large"       │
   │ "material" → "cotton"      │
   └────────────────────────────┘
                 │
                 ▼
             dicionário
```
---
4. ⚖️ `*args` × `**kwargs`
Essa diferença é fundamental:
Recurso	Recebe	Estrutura
`*args`	argumentos posicionais	`tuple`
`**kwargs`	argumentos nomeados	`dict`
Exemplo:
```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)
```
Chamada:
```python
example(
    10,
    20,
    name="Ana",
    age=25
)
```
Conceitualmente:
```python
args
# (10, 20)

kwargs
# {"name": "Ana", "age": 25}
```
---
5. 🔗 `*args` + `**kwargs`
Podemos utilizar os dois na mesma função:
```python
def show_data(*args, **kwargs):
    print(args)
    print(kwargs)
```
Exemplo:
```python
show_data(
    "Python",
    "SQL",
    level="beginner",
    area="backend"
)
```
Teremos:
```python
args
# ("Python", "SQL")

kwargs
# {
#     "level": "beginner",
#     "area": "backend"
# }
```
💼 Aplicação profissional
Esse mecanismo aparece em bibliotecas e frameworks quando uma função precisa aceitar diferentes opções.
Por exemplo:
```python
def create_connection(**options):
    ...
```
Poderíamos passar:
```python
create_connection(
    host="localhost",
    port=5432,
    database="clientes"
)
```
> ⚠️ **Boa prática:** não use `*args` e `**kwargs apenas porque eles existem. Se você sabe exatamente quais parâmetros a função precisa, parâmetros explícitos normalmente deixam a interface mais clara.
---
6. 🚦 Parâmetros Especiais
Python permite controlar como os argumentos podem ser fornecidos.
Os símbolos mais importantes aqui são:
```text
/
*
```
Eles possuem funções diferentes.
---
7. `/` — Parâmetros Somente Posicionais
Quando colocamos `/` na definição:
```python
def calculate_total(price, quantity, /):
    return price * quantity
```
Os parâmetros anteriores ao `/` precisam ser fornecidos por posição.
Isso funciona:
```python
calculate_total(100, 2)
```
Mas isto não:
```python
calculate_total(
    price=100,
    quantity=2
)
```
🧠 Como pensar
O `/` funciona como uma barreira:
```text
price, quantity | /
               ↑
        somente posição
```
Tudo que estiver antes dele precisa ser passado posicionalmente.
---
8. `*` — Parâmetros Somente Nomeados
Agora temos o comportamento contrário:
```python
def create_product(*, name, price):
    return f"{name}: R$ {price}"
```
Os parâmetros depois do `*` precisam ser fornecidos por nome.
Isso funciona:
```python
create_product(
    name="Mouse",
    price=100
)
```
Mas isto não:
```python
create_product("Mouse", 100)
```
🧠 Visualização
```text
* | name, price
  ↑
  somente nomeados
```
---
9. 🧩 Os três tipos de parâmetros
Também podemos combinar os comportamentos:
```python
def function(a, b, /, c, d, *, e, f):
    ...
```
Podemos interpretar:
```text
a, b
 ↓
somente posicionais

c, d
 ↓
posicionais ou nomeados

e, f
 ↓
somente nomeados
```
Isso permite criar interfaces de funções com regras de chamada bem definidas.
---
10. 🧠 Objetos de Primeira Classe
Este é um conceito muito importante.
Em Python, funções são objetos de primeira classe.
Isso significa que uma função pode ser tratada como um valor.
Podemos:
armazená-la em uma variável;
passá-la como argumento;
retorná-la de outra função;
colocá-la em estruturas de dados.
Exemplo:
```python
def square(number):
    return number ** 2
```
Podemos fazer:
```python
operation = square
```
Agora:
```text
operation
   │
   ▼
square
```
As duas referências apontam para a mesma função.
Podemos executar:
```python
operation(5)
```
Resultado:
```text
25
```
---
11. ⚠️ `square` × `square()`
Essa diferença é fundamental:
```python
operation = square
```
Aqui estamos armazenando a função.
Já:
```python
operation = square()
```
estamos chamando a função imediatamente.
Pense assim:
```text
square
  ↓
"Estou apontando para a função."

square()
  ↓
"Estou executando a função."
```
---
12. 🔄 Passando uma Função para Outra Função
Como funções são objetos de primeira classe, podemos enviá-las como argumentos.
```python
def square(number):
    return number ** 2


def double(number):
    return number * 2


def execute_operation(operation, number):
    return operation(number)
```
Podemos fazer:
```python
execute_operation(square, 5)
```
O raciocínio é:
```text
execute_operation(square, 5)
             │       │
             │       └── number = 5
             │
             └── operation = square
```
Dentro da função:
```python
operation(number)
```
Nesse caso equivale a:
```python
square(5)
```
Então:
```text
square(5)
   ↓
25
   ↓
return 25
```
💼 Aplicação profissional
Esse conceito aparece em:
processamento de dados;
callbacks;
ordenação;
automação;
programação funcional;
frameworks;
decorators;
processamento de coleções.
Ele permite criar funções mais genéricas e reutilizáveis.
---
13. 🌎 Escopo
Escopo é a região do programa em que determinado nome pode ser acessado.
Uma maneira simples de pensar:
> O escopo determina onde uma variável existe e pode ser encontrada.
Nesta aula, trabalhamos principalmente com:
escopo local;
escopo global.
---
14. 📍 Escopo Local
Uma variável criada dentro de uma função normalmente pertence ao escopo local daquela função.
```python
def show_message():
    message = "Olá!"
    print(message)
```
A variável `message` foi criada dentro da função.
Ela pertence ao contexto local daquela execução.
Visualização
```text
PROGRAMA
│
├── variáveis globais
│
└── função
    │
    └── variáveis locais
```
O código dentro da função consegue trabalhar com sua variável local.
O código externo não pode simplesmente assumir que ela existe.
---
15. 🌍 Escopo Global
Uma variável criada fora das funções pode estar no escopo global.
```python
message = "Olá, mundo!"


def show_message():
    print(message)
```
Quando executamos:
```python
show_message()
```
a função consegue encontrar `message`.
---
16. 🔎 Mesmo nome em escopos diferentes
Podemos ter:
```python
name = "Maria"


def show_name():
    name = "João"
    print(name)
```
Ao executar:
```python
show_name()
```
teremos:
```text
João
```
Mas:
```python
print(name)
```
fora da função produzirá:
```text
Maria
```
🧠 Por que isso acontece?
Existem duas associações em contextos diferentes:
```text
GLOBAL
name → "Maria"

LOCAL DA FUNÇÃO
name → "João"
```
A variável local não substituiu automaticamente a global.
Ela criou uma associação local com o mesmo nome.
---
17. 🧭 Como raciocinar sobre escopo
Quando Python encontra um nome dentro de uma função, pense primeiro:
```text
Existe uma variável local com esse nome?
             │
        ┌────┴────┐
       SIM       NÃO
        │          │
        ▼          ▼
      usa      procura em
      local    escopos externos
```
Esse modelo será aprofundado futuramente com o conceito LEGB.
Por enquanto, o essencial é compreender:
> **Local = pertence ao contexto da função.**
> **Global = pertence ao contexto externo/global do programa.**
---
18. 🛠️ Aplicação Prática
Podemos combinar vários conceitos em uma função de relatório:
```python
def create_report(customer, *products, **options):

    print(f"Cliente: {customer}")

    print("\nProdutos:")

    for product in products:
        print(f"- {product}")

    print("\nConfigurações:")

    for key, value in options.items():
        print(f"- {key}: {value}")
```
Chamada:
```python
create_report(
    "João",
    "Notebook",
    "Mouse",
    "Teclado",
    delivery="express",
    payment="credit_card"
)
```
O raciocínio é:
```text
customer
    ↓
"João"

*products
    ↓
("Notebook", "Mouse", "Teclado")

**options
    ↓
{
    "delivery": "express",
    "payment": "credit_card"
}
```
Esse exemplo mostra como os recursos estudados podem trabalhar juntos.
---
19. 💼 Conexão com Desenvolvimento Profissional
Em um sistema real, uma função normalmente deve executar uma responsabilidade específica.
Por exemplo:
```text
Receber dados
      ↓
Validar dados
      ↓
Processar dados
      ↓
Retornar resultado
```
Podemos separar essas responsabilidades em funções:
```python
user = get_user()

validated_user = validate_user(user)

saved_user = save_user(validated_user)
```
Cada função possui uma responsabilidade.
Isso ajuda a produzir código:
organizado;
reutilizável;
testável;
legível;
mais fácil de modificar;
mais fácil de manter.
---
20. 📚 Resumo dos Conceitos
Argumentos nomeados
Indicam explicitamente o parâmetro que receberá o valor.
```python
function(name="Ana")
```
`*args`
Recebe quantidade variável de argumentos posicionais.
```python
def function(*args):
    ...
```
Dentro da função, `args` é uma tupla.
`**kwargs`
Recebe quantidade variável de argumentos nomeados.
```python
def function(**kwargs):
    ...
```
Dentro da função, `kwargs` é um dicionário.
`/`
Determina parâmetros somente posicionais.
```python
def function(value, /):
    ...
```
`*`
Pode determinar parâmetros somente nomeados.
```python
def function(*, value):
    ...
```
Objetos de primeira classe
Funções podem ser tratadas como valores.
```python
operation = function
```
Função como argumento
Uma função pode receber outra função:
```python
def execute(operation):
    return operation()
```
Escopo local
Variáveis criadas dentro de uma função normalmente pertencem ao escopo local daquela função.
Escopo global
Variáveis criadas fora das funções podem estar disponíveis no escopo global.
---
🎯 Conceito Mais Importante da Aula
> **Em Python, uma função não é apenas algo que executamos. Ela também é um objeto que pode ser armazenado, passado para outra função e utilizado para construir código mais flexível e reutilizável.**
Ao mesmo tempo, compreender escopo é essencial para saber onde as variáveis existem e como o Python encontra seus valores.
---
🗺️ Mapa Mental
```text
                         FUNÇÕES
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
     ARGUMENTOS          FLEXIBILIDADE      ESCOPO
          │                 │                 │
    ┌─────┴─────┐       ┌───┴────┐       ┌───┴────┐
    │           │       │        │       │        │
Posicionais  Nomeados  *args  **kwargs  Local   Global
                              │
                              ▼
                         Dicionário

                 PARÂMETROS ESPECIAIS
                         │
                  ┌──────┴──────┐
                  │             │
                  /             *
                  │             │
           Só posição     Só nome

                 OBJETOS DE PRIMEIRA CLASSE
                         │
                         ▼
                  Função como valor
                         │
                         ▼
                 Função como argumento
                         │
                         ▼
                  Código reutilizável
```
---
📌 Checklist — Aula 2
[ ] Sei explicar argumentos posicionais e nomeados.
[ ] Sei explicar `*args`.
[ ] Sei que `*args` é uma tupla.
[ ] Sei explicar `**kwargs`.
[ ] Sei que `**kwargs` é um dicionário.
[ ] Sei diferenciar `*args` de `**kwargs`.
[ ] Entendo o significado de `/`.
[ ] Entendo o significado de `*` em parâmetros.
[ ] Entendo o conceito de objetos de primeira classe.
[ ] Sei armazenar uma função em uma variável.
[ ] Sei passar uma função como argumento.
[ ] Entendo escopo local.
[ ] Entendo escopo global.
[ ] Entendo por que o mesmo nome pode representar valores diferentes em escopos diferentes.
[ ] Consigo reconhecer aplicações desses conceitos em código profissional.
---
🚀 Regra de Aprendizado
```text
ENTENDER
    ↓
PRATICAR
    ↓
RACIOCINAR
    ↓
APLICAR
    ↓
AVANÇAR
```
> 🧠 **Não memorize apenas a sintaxe. Tente sempre explicar o que o Python está fazendo e, principalmente, por que está fazendo.**
---
🔜 Continuação
O próximo conteúdo deve continuar a evolução natural do Módulo 9 — Funções, sem reiniciar os fundamentos já estudados.