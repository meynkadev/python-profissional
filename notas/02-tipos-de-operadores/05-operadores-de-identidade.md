# Aula 5 – Operadores de Identidade

## Objetivo da aula

Aprender a diferença entre comparar valores e comparar identidades de objetos utilizando os operadores `is` e `is not`.

---

# O que são operadores de identidade?

Os operadores de identidade verificam se duas variáveis apontam para o **mesmo objeto na memória**, e não apenas se possuem o mesmo valor.

---

# Operador `==`

O operador `==` compara os valores de dois objetos.

## Exemplo

```python
x = 10
y = 10

print(x == y)
```

Resultado:

```text
True
```

O resultado é `True` porque os valores são iguais.

---

# Operador `is`

O operador `is` verifica se duas variáveis apontam para o mesmo objeto na memória.

## Exemplo

```python
x = 10
y = 10

print(x is y)
```

Em muitos casos, o resultado será:

```text
True
```

Isso acontece porque o Python reutiliza alguns objetos imutáveis (como pequenos números inteiros e algumas strings) para otimizar o uso da memória.

> **Importante:** esse comportamento é uma otimização da implementação do Python e não deve ser utilizado para comparar valores.

---

# Operador `is not`

O operador `is not` verifica se duas referências **não** apontam para o mesmo objeto.

## Exemplo

```python
usuario = None

print(usuario is not None)
```

Resultado:

```text
False
```

---

# O objeto `None`

`None` representa a ausência de um valor.

Uma variável pode existir, mas ainda não possuir um valor útil.

Exemplo:

```python
usuario = None
```

Nesse caso, a variável existe, mas aponta para o objeto especial `None`.

---

# Forma recomendada de verificar `None`

A comunidade Python recomenda utilizar:

```python
if usuario is None:
    print("Usuário não informado")
```

Em vez de:

```python
if usuario == None:
    print("Usuário não informado")
```

Essa recomendação faz parte do guia de estilo da linguagem (PEP 8).

---

# Diferença entre `==` e `is`

| Operador | O que compara? |
|----------|----------------|
| `==` | Os valores dos objetos |
| `is` | A identidade (mesmo objeto na memória) |
| `is not` | Objetos diferentes na memória |

---

# Exemplos práticos

## Comparação de valores

```python
a = 100
b = 100

print(a == b)
```

Resultado:

```text
True
```

---

## Comparação de identidade

```python
a = 100
b = 100

print(a is b)
```

O resultado pode ser `True` porque o Python reutiliza alguns objetos na memória.

Entretanto, isso não deve ser usado como regra para comparar números.

---

## Verificando se um usuário foi informado

```python
usuario = None

print(usuario is None)
```

Resultado:

```text
True
```

---

## Verificando se um login foi preenchido

```python
usuario = "Meynkâ"
senha = "123456"

login_preenchido = usuario is not None and senha is not None

print(login_preenchido)
```

Resultado:

```text
True
```

---

# Boas práticas

- Utilize `==` para comparar valores.
- Utilize `is` para verificar identidade.
- Utilize `is None` e `is not None` para verificar ausência de valor.
- Evite utilizar `is` para comparar números, strings ou outros valores comuns.

---

# Resumo

- `==` compara valores.
- `is` compara identidade.
- `is not` verifica se são objetos diferentes.
- `None` representa ausência de valor.
- A forma recomendada de verificar `None` é utilizando `is None`.

---

# O que aprendi nesta aula

- Entendi a diferença entre igualdade e identidade.
- Aprendi que variáveis armazenam referências para objetos.
- Compreendi que o Python reutiliza alguns objetos para otimizar memória.
- Aprendi a utilizar `is None` e `is not None`.
- Entendi quando utilizar `==` e quando utilizar `is`.