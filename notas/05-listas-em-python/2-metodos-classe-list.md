# Métodos da classe `list`

## Objetivo

Aprender a utilizar os principais métodos da classe `list` para adicionar, remover, consultar e organizar elementos.

---

# Adicionando elementos

## `append()`

Adiciona um elemento ao final da lista.

```python
frutas = ["Maçã", "Banana"]

frutas.append("Uva")
```

Resultado:

```text
["Maçã", "Banana", "Uva"]
```

---

## `insert()`

Adiciona um elemento em uma posição específica.

Sintaxe:

```python
lista.insert(indice, valor)
```

Exemplo:

```python
frutas.insert(1, "Uva")
```

---

## `extend()`

Adiciona os elementos de outra sequência ao final da lista.

```python
frutas.extend(["Uva", "Laranja"])
```

### Diferença entre `append()` e `extend()`

```python
frutas.append(["Uva", "Laranja"])
```

Adiciona a lista inteira como **um único elemento**.

```python
frutas.extend(["Uva", "Laranja"])
```

Adiciona os elementos individualmente.

---

# Removendo elementos

## `remove()`

Remove a primeira ocorrência de um determinado valor.

```python
frutas.remove("Banana")
```

O método trabalha com o **valor**, não com o índice.

---

## `pop()`

Remove um elemento pelo índice e retorna o elemento removido.

```python
item = frutas.pop(1)
```

Se o índice não for informado:

```python
frutas.pop()
```

o último elemento será removido.

### Diferença entre `remove()` e `pop()`

```text
remove() → remove pelo valor
pop()    → remove pelo índice e retorna o elemento removido
```

---

## `clear()`

Remove todos os elementos da lista.

```python
frutas.clear()
```

Resultado:

```text
[]
```

---

# Consultando elementos

## `index()`

Retorna o índice da primeira ocorrência de um valor.

```python
frutas.index("Banana")
```

---

## `count()`

Conta quantas vezes um valor aparece na lista.

```python
nomes = ["Ana", "Carlos", "Ana", "Maria"]

nomes.count("Ana")
```

Resultado:

```text
2
```

---

# Organizando elementos

## `sort()`

Ordena os elementos da lista.

```python
numeros = [5, 2, 8, 1]

numeros.sort()
```

Resultado:

```text
[1, 2, 5, 8]
```

Por padrão, a ordenação é crescente.

---

## `reverse()`

Inverte a ordem atual dos elementos.

```python
frutas = ["Maçã", "Banana", "Uva"]

frutas.reverse()
```

Resultado:

```text
["Uva", "Banana", "Maçã"]
```

Importante:

`reverse()` apenas inverte a ordem atual. Ele não realiza uma ordenação.

---

# Mapa mental dos métodos

```text
LISTAS

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

# Conceitos importantes

- `append()` adiciona um elemento ao final.
- `insert()` adiciona em um índice específico.
- `extend()` adiciona elementos de outra sequência.
- `remove()` remove pelo valor.
- `pop()` remove pelo índice e retorna o elemento.
- `clear()` esvazia a lista.
- `index()` localiza a posição de um valor.
- `count()` conta ocorrências.
- `sort()` ordena a lista.
- `reverse()` inverte a ordem atual.

---

# Resumo

Nesta aula aprendi a manipular listas utilizando métodos específicos para:

- adicionar elementos;
- remover elementos;
- consultar elementos;
- ordenar elementos;
- inverter a ordem dos elementos.

Esses métodos são fundamentais para trabalhar com listas em Python e aparecem constantemente em aplicações reais.