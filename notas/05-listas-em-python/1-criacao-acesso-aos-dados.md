# Listas em Python

## Objetivo

Aprender a criar listas, acessar seus elementos, alterar valores e percorrer seus dados.

---

# O que é uma lista?

Uma lista é uma estrutura de dados utilizada para armazenar vários elementos dentro de uma única variável.

Exemplo:

```python
frutas = ["Maçã", "Banana", "Uva"]
```

Em vez de criar uma variável para cada fruta, podemos armazenar todas dentro da mesma lista.

---

# Criação de listas

Uma lista é criada utilizando colchetes:

```python
frutas = ["Maçã", "Banana", "Uva"]
```

Também é possível criar uma lista vazia:

```python
frutas = []
```

---

# Elementos e índices

Cada elemento possui uma posição chamada índice.

Exemplo:

```text
Índice:    0        1        2
           ↓        ↓        ↓
         Maçã    Banana     Uva
```

Para acessar um elemento:

```python
frutas[0]
```

Resultado:

```text
Maçã
```

---

# Índices negativos

Python também permite acessar elementos começando pelo final.

```text
Índice:   -3       -2       -1
           ↓        ↓        ↓
         Maçã    Banana     Uva
```

Exemplo:

```python
frutas[-1]
```

Resultado:

```text
Uva
```

---

# Alterando elementos

Listas são **mutáveis**.

Isso significa que podemos alterar diretamente um elemento.

```python
frutas = ["Maçã", "Banana", "Uva"]

frutas[1] = "Laranja"
```

Agora:

```python
["Maçã", "Laranja", "Uva"]
```

---

# Tamanho da lista

A função `len()` retorna a quantidade de elementos.

```python
frutas = ["Maçã", "Banana", "Uva"]

print(len(frutas))
```

Resultado:

```text
3
```

Importante:

A quantidade de elementos não é igual ao último índice.

Uma lista com 3 elementos possui:

```text
Quantidade: 3
Último índice: 2
```

Isso acontece porque os índices começam em `0`.

---

# Fatiamento de listas

A mesma lógica aprendida com strings também pode ser aplicada às listas.

```python
frutas = ["Maçã", "Banana", "Uva", "Laranja"]

print(frutas[1:3])
```

Resultado:

```text
["Banana", "Uva"]
```

Regra:

> O índice inicial entra e o índice final não entra.

---

# Percorrendo uma lista

Podemos utilizar `for` para percorrer os elementos.

```python
for fruta in frutas:
    print(fruta)
```

O Python percorre cada elemento da lista.

---

# Listas com diferentes tipos de dados

Uma lista pode armazenar diferentes tipos de dados.

```python
aluno = ["Meynkâ", 25, "Violão", True]
```

Nesse exemplo existem:

- `str`
- `int`
- `str`
- `bool`

Embora Python permita essa mistura, em projetos profissionais é importante que a estrutura tenha uma finalidade clara e coerente.

---

# Listas são mutáveis

Essa é uma diferença importante em relação às strings.

## String

```python
texto = "Python"
```

Strings são imutáveis.

Não podemos alterar diretamente um caractere existente.

## Lista

```python
frutas = ["Maçã", "Banana", "Uva"]

frutas[1] = "Laranja"
```

Listas são mutáveis.

Podemos alterar diretamente seus elementos.

---

# Lista como objeto

Uma lista é um objeto do tipo `list`.

Por isso possui métodos próprios.

Exemplo:

```python
frutas.append("Morango")
```

Na próxima parte da aula estudaremos os principais métodos da classe `list`.

---

# Conceitos importantes

- Listas são criadas com `[]`.
- Uma lista pode armazenar vários elementos.
- Cada elemento possui um índice.
- Os índices começam em `0`.
- Índices negativos começam pelo final.
- Listas são mutáveis.
- `len()` retorna a quantidade de elementos.
- Listas podem ser percorridas com `for`.
- O fatiamento de listas segue a mesma lógica das strings.

---

# Regra mental

Ao trabalhar com uma lista, pense:

```text
Quais elementos existem?
↓
Qual é o índice do elemento?
↓
Preciso acessar, alterar ou percorrer?
```

Essa forma de pensar ajuda a escolher a operação correta.

---

# Resumo

Nesta aula aprendi a:

- Criar listas.
- Criar listas vazias.
- Acessar elementos por índice.
- Utilizar índices negativos.
- Alterar elementos.
- Verificar a quantidade de elementos com `len()`.
- Fazer fatiamento de listas.
- Percorrer listas com `for`.
- Diferenciar listas mutáveis de strings imutáveis.