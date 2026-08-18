# Módulo 5 — Estruturas de Dados: Listas em Python

## Objetivo do módulo

Neste módulo foi estudada a estrutura de dados **lista (`list`)** em Python.

O objetivo foi aprender a criar listas, acessar e alterar seus elementos, percorrer seus dados e utilizar os principais métodos da classe `list` para adicionar, remover, consultar e organizar elementos.

---

## 1. O que é uma lista?

Uma lista é uma estrutura de dados utilizada para armazenar vários elementos dentro de uma única variável.

```python
fruits = ["Apple", "Banana", "Grape"]
```

Também é possível criar uma lista vazia:

```python
fruits = []
```

As listas são representadas utilizando **colchetes (`[]`)**.

---

## 2. Elementos e índices

Cada elemento de uma lista possui uma posição chamada **índice (`index`)**.

Os índices começam em `0`.

```text
Índice:    0          1          2
           ↓          ↓          ↓
         Apple      Banana     Grape
```

Para acessar um elemento:

```python
fruits[0]
```

Resultado:

```text
Apple
```

Uma lista com três elementos possui os índices `0`, `1` e `2`.

---

## 3. Índices negativos

Python também permite acessar elementos começando pelo final da lista.

```text
Índice:   -3         -2        -1
           ↓          ↓         ↓
         Apple      Banana     Grape
```

Exemplo:

```python
fruits[-1]
```

Resultado:

```text
Grape
```

O índice `-1` representa o último elemento da lista.

---

## 4. Alterando elementos

Listas são **mutáveis (`mutable`)**.

Isso significa que podemos alterar diretamente um elemento existente.

```python
fruits = ["Apple", "Banana", "Grape"]

fruits[1] = "Orange"
```

Resultado:

```python
["Apple", "Orange", "Grape"]
```

Essa característica diferencia listas de strings.

Strings são **imutáveis (`immutable`)**, enquanto listas são mutáveis.

---

## 5. Tamanho da lista — `len()`

A função `len()` retorna a quantidade de elementos da lista.

```python
fruits = ["Apple", "Banana", "Grape"]

print(len(fruits))
```

Resultado:

```text
3
```

É importante não confundir quantidade de elementos com índice.

Uma lista com três elementos possui:

```text
Quantidade de elementos: 3
Último índice:           2
```

Isso ocorre porque os índices começam em `0`.

---

## 6. Slicing — fatiamento

O **slicing (fatiamento)** permite obter uma parte da lista.

```python
fruits = ["Apple", "Banana", "Grape", "Orange"]

print(fruits[1:3])
```

Resultado:

```text
["Banana", "Grape"]
```

A regra do slicing é:

> O índice inicial é incluído e o índice final não é incluído.

Essa é a mesma lógica de fatiamento estudada anteriormente com strings.

---

## 7. Percorrendo listas com `for`

Uma lista pode ser percorrida utilizando um **loop (`for`)**.

```python
fruits = ["Apple", "Banana", "Grape"]

for fruit in fruits:
    print(fruit)
```

O `for` percorre cada elemento da lista individualmente.

---

## 8. Listas com diferentes tipos de dados

Python permite armazenar diferentes tipos de dados dentro de uma mesma lista.

```python
student = ["Meynkâ", 25, "Guitar", True]
```

Nesse exemplo existem valores dos tipos:

* `str`
* `int`
* `str`
* `bool`

Embora Python permita essa flexibilidade, em projetos profissionais a lista deve ter uma finalidade clara e uma estrutura coerente.

---

## 9. Lista como objeto

Uma lista é um objeto do tipo `list`.

Por isso, possui métodos próprios para manipulação dos seus elementos.

Exemplo:

```python
fruits.append("Strawberry")
```

Os métodos da classe `list` permitem realizar operações comuns sem precisar implementar manualmente cada comportamento.

---

# Métodos da classe `list`

## 10. Adicionando elementos

### `append()`

Adiciona um elemento ao final da lista.

```python
fruits = ["Apple", "Banana"]

fruits.append("Grape")
```

Resultado:

```python
["Apple", "Banana", "Grape"]
```

---

### `insert()`

Adiciona um elemento em uma posição específica.

Sintaxe:

```python
list.insert(index, value)
```

Exemplo:

```python
fruits.insert(1, "Grape")
```

O elemento é inserido na posição indicada pelo índice.

---

### `extend()`

Adiciona os elementos de outra sequência ao final da lista.

```python
fruits.extend(["Grape", "Orange"])
```

### Diferença entre `append()` e `extend()`

Com `append()`:

```python
fruits.append(["Grape", "Orange"])
```

A lista é adicionada como **um único elemento**.

Com `extend()`:

```python
fruits.extend(["Grape", "Orange"])
```

Os elementos são adicionados individualmente.

---

## 11. Removendo elementos

### `remove()`

Remove a primeira ocorrência de determinado valor.

```python
fruits.remove("Banana")
```

O método `remove()` trabalha com o **valor**, e não com o índice.

---

### `pop()`

Remove um elemento pelo índice e retorna o elemento removido.

```python
item = fruits.pop(1)
```

Também é possível utilizar:

```python
fruits.pop()
```

Quando nenhum índice é informado, o último elemento é removido.

### Diferença entre `remove()` e `pop()`

```text
remove() → remove pelo valor
pop()    → remove pelo índice e retorna o elemento removido
```

---

### `clear()`

Remove todos os elementos da lista.

```python
fruits.clear()
```

Resultado:

```python
[]
```

---

## 12. Consultando elementos

### `index()`

Retorna o índice da primeira ocorrência de determinado valor.

```python
fruits.index("Banana")
```

Esse método permite descobrir a posição de um elemento.

---

### `count()`

Conta quantas vezes determinado valor aparece na lista.

```python
names = ["Ana", "Carlos", "Ana", "Maria"]

names.count("Ana")
```

Resultado:

```text
2
```

---

## 13. Organizando elementos

### `sort()`

Ordena os elementos da lista.

```python
numbers = [5, 2, 8, 1]

numbers.sort()
```

Resultado:

```python
[1, 2, 5, 8]
```

Por padrão, a ordenação é crescente.

---

### `reverse()`

Inverte a ordem atual dos elementos.

```python
fruits = ["Apple", "Banana", "Grape"]

fruits.reverse()
```

Resultado:

```python
["Grape", "Banana", "Apple"]
```

É importante diferenciar `reverse()` de `sort()`.

`reverse()` **não ordena** os elementos. Ele apenas inverte a ordem atual.

---

# Mapa mental dos métodos

```text
LISTA — list

├── Adicionar
│   ├── append()
│   ├── insert()
│   └── extend()
│
├── Remover
│   ├── remove()
│   ├── pop()
│   └── clear()
│
├── Consultar
│   ├── index()
│   └── count()
│
└── Organizar
    ├── sort()
    └── reverse()
```

---

# Tabela de referência rápida

| Operação           | Método/Função | Finalidade                                   |
| ------------------ | ------------- | -------------------------------------------- |
| Tamanho            | `len()`       | Retorna a quantidade de elementos            |
| Adicionar no final | `append()`    | Adiciona um elemento ao final                |
| Inserir            | `insert()`    | Adiciona um elemento em um índice específico |
| Adicionar vários   | `extend()`    | Adiciona elementos de outra sequência        |
| Remover por valor  | `remove()`    | Remove a primeira ocorrência de um valor     |
| Remover por índice | `pop()`       | Remove e retorna um elemento                 |
| Limpar             | `clear()`     | Remove todos os elementos                    |
| Localizar          | `index()`     | Retorna o índice da primeira ocorrência      |
| Contar             | `count()`     | Conta ocorrências de um valor                |
| Ordenar            | `sort()`      | Ordena os elementos                          |
| Inverter           | `reverse()`   | Inverte a ordem atual                        |

---

# Conceitos fundamentais

Ao concluir o módulo, os principais conceitos estudados foram:

* listas são estruturas de dados;
* listas são criadas com `[]`;
* uma lista pode armazenar vários elementos;
* cada elemento possui um índice;
* os índices começam em `0`;
* índices negativos permitem acessar elementos a partir do final;
* listas são mutáveis;
* `len()` retorna a quantidade de elementos;
* listas podem utilizar slicing;
* listas podem ser percorridas com `for`;
* listas são objetos do tipo `list`;
* objetos `list` possuem métodos próprios;
* `append()` adiciona ao final;
* `insert()` adiciona em uma posição específica;
* `extend()` adiciona elementos de outra sequência;
* `remove()` remove pelo valor;
* `pop()` remove pelo índice e retorna o elemento;
* `clear()` remove todos os elementos;
* `index()` localiza a posição de um valor;
* `count()` conta ocorrências;
* `sort()` ordena a lista;
* `reverse()` inverte a ordem atual.

---

# Regra mental para trabalhar com listas

Ao trabalhar com uma lista, podemos raciocinar da seguinte forma:

```text
Tenho uma coleção de dados
        ↓
Preciso acessar um elemento?
        ↓
Índice / índice negativo

Preciso obter uma parte?
        ↓
Slicing

Preciso alterar um elemento?
        ↓
Atribuição por índice

Preciso adicionar?
        ↓
append() / insert() / extend()

Preciso remover?
        ↓
remove() / pop() / clear()

Preciso consultar?
        ↓
index() / count()

Preciso organizar?
        ↓
sort() / reverse()

Preciso percorrer os elementos?
        ↓
for
```

---

# Conclusão

O Módulo 5 apresentou as **listas (`list`)**, uma das principais estruturas de dados do Python.

O estudo começou pela criação e manipulação básica de listas e avançou para os principais métodos da classe `list`.

O conhecimento adquirido permite trabalhar com coleções de dados, acessando, modificando, adicionando, removendo, consultando e organizando seus elementos.

As listas representam uma base importante para a evolução no estudo de Python, pois estruturas de dados são utilizadas constantemente no desenvolvimento de software e serão fundamentais para compreender conceitos mais avançados da linguagem.

**Módulo 5 concluído.**
