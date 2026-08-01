# Fatiamento de Strings (Slice)

## Objetivo

Aprender a acessar caracteres e partes de uma string utilizando índices e fatiamento.

---

# Índices

Cada caractere de uma string possui uma posição (índice).

Exemplo:

```text
String:

P  y  t  h  o  n

Índices:

0  1  2  3  4  5
```

Também é possível acessar utilizando índices negativos.

```text
P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
```

Exemplos:

```python
texto = "Python"

print(texto[0])   # P
print(texto[-1])  # n
```

---

# Fatiamento (Slice)

A sintaxe é:

```python
texto[início:fim]
```

O índice inicial é incluído.

O índice final **não é incluído**.

Exemplo:

```python
texto = "Python"

print(texto[0:3])
```

Resultado:

```
Pyt
```

Porque são utilizados os índices:

```
0
1
2
```

O índice 3 não faz parte do resultado.

---

## Omitindo o início

Quando o início é omitido, o Python considera o índice 0.

```python
texto[:3]
```

Resultado:

```
Pyt
```

---

## Omitindo o final

Quando o final é omitido, o Python considera o último caractere da string.

```python
texto[3:]
```

Resultado:

```
hon
```

---

## Copiando toda a string

```python
texto[:]
```

Resultado:

```
Python
```

---

# Passo (Step)

Também é possível definir de quantos em quantos caracteres a sequência será percorrida.

Sintaxe:

```python
texto[início:fim:passo]
```

Exemplo:

```python
texto[::2]
```

Resultado:

```
Pto
```

São utilizados os índices:

```
0
2
4
```

---

# Invertendo uma string

Utilizando passo negativo.

```python
texto[::-1]
```

Resultado:

```
nohtyP
```

O passo `-1` faz a leitura da string do final para o início.

---

# Regra mais importante

Sempre lembre:

- O índice inicial entra.
- O índice final não entra.

Essa regra vale para qualquer fatiamento.

---

# Conceitos importantes

- Strings são sequências de caracteres.
- Cada caractere possui um índice.
- Os índices podem ser positivos ou negativos.
- O fatiamento permite acessar apenas parte da string.
- O passo controla como a sequência será percorrida.
- Um passo negativo percorre a sequência ao contrário.

---

# Boas práticas

- Utilize índices negativos quando precisar acessar elementos a partir do final.
- Evite decorar exemplos; entenda a lógica dos índices.
- Sempre pense em três perguntas:

1. Onde começa?
2. Onde termina?
3. De quantos em quantos caracteres será percorrido?

---

# Resumo

Nesta aula aprendi que:

- Posso acessar caracteres utilizando índices.
- Posso utilizar índices negativos.
- Posso selecionar apenas parte da string com slices.
- O índice inicial é incluído e o índice final não.
- Posso definir um passo para percorrer a sequência.
- Posso inverter uma string utilizando `[::-1]`.