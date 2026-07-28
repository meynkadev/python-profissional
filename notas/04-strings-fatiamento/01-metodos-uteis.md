# Métodos da classe `str`

## Objetivo

Aprender a utilizar os principais métodos da classe `str` para manipular textos em Python.

---

# O que é uma string?

Uma string é um objeto da classe `str`.

Isso significa que ela possui métodos próprios que podem ser utilizados através do operador ponto (`.`).

Exemplo:

```python
nome = "Python"

print(nome.upper())
```

---

# Importante

As strings em Python são **imutáveis**.

Isso significa que os métodos **não alteram** a string original.

Eles retornam uma **nova string**.

Exemplo:

```python
nome = "python"

nome.upper()

print(nome)
```

Saída:

```
python
```

Para alterar a variável:

```python
nome = nome.upper()
```

Agora:

```
PYTHON
```

---

# Métodos estudados

## upper()

Converte todos os caracteres para letras maiúsculas.

```python
nome.upper()
```

Resultado:

```
PYTHON
```

---

## lower()

Converte todos os caracteres para letras minúsculas.

```python
nome.lower()
```

Resultado:

```
python
```

---

## title()

Converte a primeira letra de cada palavra para maiúscula.

```python
nome.title()
```

Resultado:

```
Meynkâ Nascimento
```

---

## strip()

Remove espaços do início e do fim da string.

```python
texto.strip()
```

---

## lstrip()

Remove apenas os espaços da esquerda.

```python
texto.lstrip()
```

---

## rstrip()

Remove apenas os espaços da direita.

```python
texto.rstrip()
```

---

## join()

Une caracteres ou elementos utilizando um separador.

Exemplo:

```python
"-".join("Python")
```

Resultado:

```
P-y-t-h-o-n
```

---

# Encadeamento de métodos

É possível executar vários métodos na mesma linha.

Exemplo:

```python
nome = nome.strip().title()
```

Ordem de execução:

1. Remove os espaços.
2. Converte a primeira letra de cada palavra para maiúscula.
3. Retorna a nova string.

---

# Conceitos importantes

- Strings são objetos da classe `str`.
- Métodos são funções pertencentes ao objeto.
- Strings são imutáveis.
- Métodos retornam uma nova string.
- Para modificar uma variável é necessário fazer uma nova atribuição.

---

# Resumo

Nesta aula aprendi que:

- Strings possuem métodos próprios.
- Posso converter letras para maiúsculas e minúsculas.
- Posso remover espaços.
- Posso unir caracteres com `join()`.
- Posso encadear métodos.
- Os métodos não alteram a string original; eles retornam uma nova string.