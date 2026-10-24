# 📘 Módulo 9 — Funções

## 🎯 Objetivo

Aprender a criar e utilizar **funções** para organizar, reutilizar e estruturar o código.

Neste módulo, os principais conceitos estudados são:

* definição e chamada de funções;
* parâmetros e argumentos;
* `return`;
* diferença entre `return` e `print()`;
* fluxo de execução;
* `return` encerrando a função;
* condicionais dentro de funções;
* rastreamento do valor retornado;
* funções com diferentes tipos de retorno.

\---

# 📚 Aula 1 — Definição e chamada de funções

Uma **função** é um bloco de código criado para realizar uma determinada tarefa.

Ela pode ser executada sempre que for necessário realizar aquela tarefa.

## Criando uma função

```python
def minha\_funcao():
    print("Olá, Python!")
```

A palavra-chave `def` é utilizada para **definir** uma função.

Porém, definir uma função não significa executá-la.

## Chamando a função

```python
minha\_funcao()
```

É nesse momento que o código dentro da função é executado.

### Estrutura básica

```python
def nome\_da\_funcao():
    # código da função
```

Depois:

```python
nome\_da\_funcao()
```

> 💡 \*\*Definir\*\* uma função é criar sua lógica.  
> \*\*Chamar\*\* uma função é executar essa lógica.

\---

# 📚 Aula 2 — Parâmetros e argumentos

Uma função pode receber informações para trabalhar.

Essas informações são passadas por meio de **parâmetros** e **argumentos**.

## Exemplo

```python
def greet(name):
    print(f"Olá, {name}!")
```

Nesse caso:

```text
name
```

é o **parâmetro**.

Quando chamamos:

```python
greet("Menkadev")
```

`"Menkadev"` é o **argumento**.

### Resumindo

```text
Parâmetro → espaço reservado dentro da função
Argumento → valor enviado para esse espaço
```

## Outro exemplo

```python
def calculate\_square(number):
    return number \*\* 2
```

Chamando:

```python
calculate\_square(5)
```

Temos:

```text
number → parâmetro
5      → argumento
```

\---

# 📚 Aula 3 — `return`

O `return` é utilizado para **devolver um valor** para quem chamou a função.

## Exemplo

```python
def add(a, b):
    return a + b
```

Ao chamar:

```python
add(10, 5)
```

A função calcula:

```text
10 + 5
```

E retorna:

```text
15
```

Esse valor pode ser armazenado:

```python
result = add(10, 5)
```

Agora:

```text
result → 15
```

## O caminho do valor

```text
add(10, 5)
     ↓
a = 10
b = 5
     ↓
a + b
     ↓
15
     ↓
return 15
     ↓
result = 15
```

> 💡 O `return` permite que o resultado produzido pela função seja utilizado pelo restante do programa.

\---

# 📚 Aula 4 — `return` x `print()`

É importante não confundir `return` com `print()`.

## `print()`

Serve principalmente para **exibir uma informação na tela**.

```python
def show\_sum(a, b):
    print(a + b)
```

Ao executar:

```python
show\_sum(10, 5)
```

O programa mostra:

```text
15
```

## `return`

Serve para **devolver um valor**.

```python
def calculate\_sum(a, b):
    return a + b
```

Podemos armazenar o resultado:

```python
result = calculate\_sum(10, 5)
```

Agora podemos utilizar `result` novamente:

```python
print(result)
```

### Comparação

|`print()`|`return`|
|-|-|
|Exibe um valor|Devolve um valor|
|Mostra algo na tela|Permite reutilizar o resultado|
|Serve para saída visual|Serve para fornecer um resultado ao código que chamou a função|
|Útil para exibição|Fundamental para processamento e reutilização|

> ⚠️ Uma função pode utilizar `print()` sem retornar um valor.

\---

# 📚 Aula 5 — `return` encerra a função

Uma característica muito importante do `return` é:

> \*\*Quando um `return` é executado, a função é encerrada imediatamente.\*\*

Observe:

```python
def check\_number(number):

    if number > 10:
        return "maior"

    return "menor"
```

Se chamarmos:

```python
check\_number(15)
```

O Python verifica:

```python
15 > 10
```

Resultado:

```text
True
```

Então executa:

```python
return "maior"
```

Nesse momento, a função termina.

O Python **não continua** para:

```python
return "menor"
```

## Regra importante

```text
return executado
       ↓
valor é devolvido
       ↓
função é encerrada
       ↓
código restante da função não é executado
```

\---

# 🧠 Como rastrear uma função

Ao analisar uma função, pense passo a passo:

```text
1. Qual argumento foi enviado?
        ↓
2. Qual valor o parâmetro recebeu?
        ↓
3. Qual condição foi avaliada?
        ↓
4. A condição é True ou False?
        ↓
5. Qual caminho será seguido?
        ↓
6. Qual return será alcançado?
        ↓
7. Qual valor o return produz?
        ↓
8. O que acontece com esse valor?
```

Esse processo é uma forma de **rastrear o fluxo de execução**.

Essa habilidade é muito importante para desenvolver raciocínio de programação.

\---

# 📚 Aula 6 — Condicionais dentro de funções

Funções podem conter estruturas condicionais.

Isso permite que a função produza resultados diferentes dependendo dos dados recebidos.

## Exemplo

```python
def analyze\_number(number):

    if number > 20:
        return "alto"

    if number > 10:
        return "medio"

    return "baixo"
```

Podemos testar:

```python
analyze\_number(25)
```

Resultado:

```text
"alto"
```

Com:

```python
analyze\_number(15)
```

Resultado:

```text
"medio"
```

E:

```python
analyze\_number(5)
```

Resultado:

```text
"baixo"
```

## 🔎 Entendendo o fluxo

Se:

```python
number = 15
```

O Python verifica primeiro:

```python
if number > 20:
```

Ou seja:

```text
15 > 20
```

Resultado:

```text
False
```

Então não executa o primeiro `return`.

Depois verifica:

```python
if number > 10:
```

Ou seja:

```text
15 > 10
```

Resultado:

```text
True
```

Então executa:

```python
return "medio"
```

A função termina nesse ponto.

O último:

```python
return "baixo"
```

não é executado.

\---

# 📚 Aula 7 — O valor retornado pode ser armazenado

Uma função pode retornar um valor que será armazenado em uma variável.

Exemplo:

```python
def calculate\_square(number):
    return number \*\* 2
```

Chamando:

```python
result = calculate\_square(5)
```

O fluxo é:

```text
5
 ↓
number = 5
 ↓
5 \*\* 2
 ↓
25
 ↓
return 25
 ↓
result = 25
```

Portanto:

```python
print(result)
```

produz:

```text
25
```

> 💡 O argumento enviado para a função e o valor retornado pela função são coisas diferentes.

\---

# ⚠️ Atenção — Argumento não é necessariamente o retorno

Considere:

```python
def analyze\_number(number):

    if number > 10:
        return "maior"

    return "menor"
```

Chamando:

```python
result = analyze\_number(15)
```

O argumento foi:

```text
15
```

Mas o retorno foi:

```text
"maior"
```

Portanto:

```text
argumento → 15
retorno   → "maior"
result     → "maior"
```

O fato de a função receber `15` **não significa** que `15` será armazenado em `result`.

Isso depende do que o `return` devolve.

\---

# 📚 Aula 8 — `return` com expressões

O `return` também pode devolver o resultado de uma expressão.

## Exemplo

```python
def calculate\_discount(price):

    if price >= 100:
        return price \* 0.90

    return price
```

Se:

```python
price = 150
```

Temos:

```python
150 \* 0.90
```

Resultado:

```text
135.0
```

Então:

```python
return 135.0
```

Se fizermos:

```python
result = calculate\_discount(150)
```

teremos:

```text
result → 135.0
```

> 💡 O `return` não precisa devolver uma variável diretamente. Ele pode devolver o resultado de uma expressão ou cálculo.

\---

# 📚 Aula 9 — Funções com vários parâmetros

Uma função pode receber vários parâmetros.

```python
def calculate\_total(price, quantity):
    return price \* quantity
```

Chamando:

```python
total = calculate\_total(25, 4)
```

Temos:

```text
price = 25
quantity = 4
```

A função calcula:

```text
25 \* 4
```

E retorna:

```text
100
```

Portanto:

```text
total → 100
```

\---

# 📚 Aula 10 — Funções que retornam strings

Uma função não precisa retornar apenas números.

Ela também pode retornar strings.

```python
def get\_status(age):

    if age >= 18:
        return "maior de idade"

    return "menor de idade"
```

Chamando:

```python
status = get\_status(20)
```

Temos:

```text
status → "maior de idade"
```

\---

# 📚 Aula 11 — Funções que retornam `True` ou `False`

Funções também podem retornar valores booleanos.

```python
def is\_positive(number):

    if number > 0:
        return True

    return False
```

Exemplo:

```python
result = is\_positive(8)
```

Resultado:

```text
result → True
```

Essas funções são muito úteis para criar **validações e verificações**.

\---

# 🧠 Modelo mental de uma função

Uma forma muito útil de pensar sobre funções é:

```text
              FUNÇÃO
                 │
                 ▼
        ┌─────────────────┐
        │     ENTRADA      │
        │ parâmetros /     │
        │ argumentos       │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   PROCESSAMENTO  │
        │ lógica / cálculos│
        │ condicionais     │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │      SAÍDA       │
        │     return       │
        └─────────────────┘
```

Em termos simples:

> \*\*Entrada → processamento → saída\*\*

Esse modelo será extremamente importante conforme avançarmos para projetos maiores.

\---

# 💼 Aplicação profissional

Funções são fundamentais no desenvolvimento profissional porque ajudam a:

* organizar o código;
* evitar repetição;
* separar responsabilidades;
* facilitar manutenção;
* facilitar testes;
* reutilizar lógica;
* tornar o código mais legível.

Em um sistema real, podemos ter funções responsáveis por tarefas específicas:

```python
def validate\_email(email):
    ...


def calculate\_total(price, quantity):
    ...


def process\_customer(customer):
    ...


def format\_response(data):
    ...
```

Cada função possui uma responsabilidade específica.

Isso permite construir sistemas maiores a partir de pequenas partes organizadas.

\---

# 🔑 Conceitos principais do módulo

### `def`

Utilizado para **definir uma função**.

```python
def minha\_funcao():
    ...
```

### Parâmetro

Variável definida na declaração da função.

```python
def greet(name):
    ...
```

`name` é o parâmetro.

### Argumento

Valor enviado para a função.

```python
greet("Menkadev")
```

`"Menkadev"` é o argumento.

### `return`

Devolve um valor para quem chamou a função e **encerra a execução da função naquele ponto**.

```python
def square(number):
    return number \*\* 2
```

### `print()`

Exibe uma informação na tela.

```python
print("Olá!")
```

\---

# 🧩 Regra prática para analisar funções

Sempre que encontrar uma função que ainda não conhece, tente responder:

```text
1. O que entra na função?
2. Quais são os parâmetros?
3. Quais valores os parâmetros receberam?
4. O que a função faz com esses valores?
5. Existem condicionais?
6. Qual caminho será seguido?
7. Qual return será executado?
8. O que exatamente o return devolve?
9. Onde o resultado será armazenado?
10. Como esse resultado será utilizado?
```

\---

# 💡 Conceito mais importante

> \*\*Uma função pode receber informações através de argumentos, processar essas informações e devolver um resultado através de `return`.\*\*

E lembre-se:

> \*\*Quando um `return` é executado, a função termina imediatamente.\*\*

\---

# 💼 Por que funções são importantes profissionalmente?

Em projetos reais, funções ajudam a dividir um sistema grande em pequenas responsabilidades.

Por exemplo, uma aplicação poderia ter funções para:

```python
def validate\_user(user):
    ...


def calculate\_order\_total(order):
    ...


def save\_customer(customer):
    ...


def send\_email(email):
    ...


def format\_api\_response(data):
    ...
```

Cada função pode cuidar de uma tarefa específica.

Isso facilita:

* leitura do código;
* manutenção;
* testes;
* reutilização;
* identificação de erros;
* evolução do sistema.

> 🎯 Aprender funções bem agora será importante para tudo que virá depois: módulos, POO, APIs, bancos de dados, automação e projetos profissionais.

\---

# 🚀 Próximo passo

Depois de consolidar o funcionamento de `return` e o rastreamento da execução, o próximo conteúdo de **Funções** poderá avançar para recursos que tornam as funções mais flexíveis e reutilizáveis.

A prioridade continua sendo:

**Entendimento > memorização**

**Raciocínio > copiar código**

**Prática > teoria isolada**

**Aplicação > decorar sintaxe**

