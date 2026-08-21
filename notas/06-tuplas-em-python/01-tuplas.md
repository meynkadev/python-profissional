# Tuplas em Python

## O que é uma tupla?

Uma tupla (`tuple`) é uma estrutura de dados utilizada para armazenar vários elementos em uma única variável.

```python
languages = ("Python", "Java", "C++")
```

A principal característica das tuplas é que elas são **imutáveis**.

---

# Criação de tuplas

Tupla vazia:

```python
numbers = ()
```

Tupla com vários elementos:

```python
numbers = (10, 20, 30)
```

## Tupla com um elemento

Em uma tupla de um único elemento, a vírgula é obrigatória:

```python
number = (10,)
```

Já:

```python
number = (10)
```

é um `int`, não uma tupla.

A vírgula é o que caracteriza a tupla de um único elemento.

Também é possível criar uma tupla sem os parênteses:

```python
numbers = 10, 20
```

---

# Acessando elementos

Tuplas utilizam índices, assim como listas.

```python
languages = ("Python", "Java", "C++")

print(languages[0])
```

Resultado:

```text
Python
```

Também podemos utilizar índices negativos:

```python
print(languages[-1])
```

Resultado:

```text
C++
```

---

# Slicing

Tuplas também permitem fatiamento (`slicing`):

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Resultado:

```text
(20, 30, 40)
```

Regra:

> O índice inicial entra. O índice final não entra.

---

# Percorrendo uma tupla

Podemos utilizar `for` para percorrer seus elementos:

```python
colors = ("red", "green", "blue")

for color in colors:
    print(color)
```

---

# Tamanho da tupla

A função `len()` retorna a quantidade de elementos:

```python
numbers = (10, 20, 30)

print(len(numbers))
```

Resultado:

```text
3
```

---

# Imutabilidade

Tuplas são **imutáveis**.

Não podemos alterar diretamente seus elementos:

```python
languages = ("Python", "Java", "C++")

languages[0] = "JavaScript"
```

Essa operação gera um erro.

Comparação:

```text
list  → mutável
tuple → imutável
```

---

# Desempacotamento (Unpacking)

O desempacotamento permite distribuir os valores de uma tupla entre variáveis.

```python
person = ("Meynkâ", 25, "Python")

name, age, language = person
```

Resultado:

```text
name     → "Meynkâ"
age      → 25
language → "Python"
```

A distribuição acontece pela ordem dos elementos.

A quantidade de variáveis deve ser compatível com a quantidade de valores.

---

# Atribuição múltipla

O desempacotamento também permite trocar valores entre variáveis:

```python
a = 10
b = 20

a, b = b, a
```

Resultado:

```text
a → 20
b → 10
```

---

# Métodos de tuplas

Como tuplas são imutáveis, elas possuem poucos métodos.

## `count()`

Retorna a quantidade de ocorrências de um valor:

```python
numbers = (10, 20, 10, 30, 10)

numbers.count(10)
```

Resultado:

```text
3
```

## `index()`

Retorna o índice da primeira ocorrência de um valor:

```python
numbers = (10, 20, 30)

numbers.index(20)
```

Resultado:

```text
1
```

---

# Diferença entre lista e tupla

```text
list  → mutável
tuple → imutável
```

Lista:

```python
items = ["Python", "Java"]
items[0] = "C++"
```

Tupla:

```python
items = ("Python", "Java")
items[0] = "C++"  # Erro
```

A escolha entre `list` e `tuple` depende da necessidade da estrutura de dados.

---

# Conceitos importantes

- `tuple` é uma estrutura de dados.
- Tuplas são imutáveis.
- Tuplas utilizam índices.
- Índices negativos funcionam em tuplas.
- Tuplas permitem slicing.
- Tuplas podem ser percorridas com `for`.
- `len()` retorna a quantidade de elementos.
- Uma tupla de um elemento precisa da vírgula.
- `count()` conta ocorrências.
- `index()` retorna o índice da primeira ocorrência.
- `unpacking` distribui os valores entre variáveis.
