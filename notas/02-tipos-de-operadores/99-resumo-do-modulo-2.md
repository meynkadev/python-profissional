# Resumo — Módulo 2: Operadores

## Objetivo do módulo

Aprender os principais operadores da linguagem Python e compreender como eles são utilizados para realizar cálculos, comparações, atribuições e tomadas de decisão.

---

# Operadores Aritméticos

Realizam operações matemáticas.

| Operador | Função |
|----------|---------|
| `+` | Soma |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `//` | Divisão inteira |
| `%` | Resto da divisão (módulo) |
| `**` | Exponenciação |

Exemplo:

```python
a = 10
b = 3

print(a + b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# Operadores de Comparação

Comparam dois valores e retornam um valor booleano (`True` ou `False`).

| Operador | Significado |
|----------|-------------|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior |
| `<` | Menor |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

Exemplo:

```python
idade = 20

print(idade >= 18)
```

---

# Operadores de Atribuição

Atualizam o valor de uma variável.

| Operador | Equivalente |
|----------|-------------|
| `=` | Atribuição |
| `+=` | Soma e atribui |
| `-=` | Subtrai e atribui |
| `*=` | Multiplica e atribui |
| `/=` | Divide e atribui |
| `//=` | Divisão inteira e atribui |
| `%=` | Módulo e atribui |
| `**=` | Potência e atribui |

Exemplo:

```python
saldo = 100

saldo += 50
```

---

# Formatação de Strings

Utilizando f-strings para inserir variáveis diretamente em textos.

Exemplo:

```python
nome = "Meynkâ"

print(f"Olá, {nome}!")
```

---

# Operadores Lógicos

Permitem combinar ou inverter condições.

| Operador | Função |
|----------|--------|
| `and` | Todas as condições devem ser verdadeiras |
| `or` | Pelo menos uma condição deve ser verdadeira |
| `not` | Inverte o valor lógico |

Exemplo:

```python
idade = 20
possui_cnh = True

print(idade >= 18 and possui_cnh)
```

---

# Operadores de Identidade

Comparam se duas variáveis fazem referência ao mesmo objeto.

| Operador | Função |
|----------|--------|
| `is` | Mesmo objeto |
| `is not` | Objetos diferentes |

Para comparar valores, utilize `==`.

Para verificar ausência de valor, utilize:

```python
if usuario is None:
```

---

# Operadores de Associação

Verificam se um elemento pertence a uma sequência.

| Operador | Função |
|----------|--------|
| `in` | Pertence |
| `not in` | Não pertence |

Exemplo:

```python
curso = "Python"

print("Py" in curso)
print("Java" not in curso)
```

---

# Boas práticas aprendidas

- Utilize `==` para comparar valores.
- Utilize `is None` para verificar ausência de valor.
- Prefira `in` para verificar se um elemento pertence a uma coleção.
- Utilize f-strings para construir mensagens.
- Escreva expressões simples e legíveis.
- Escolha nomes claros para variáveis.

---

# O que aprendi neste módulo

- Realizar operações matemáticas.
- Comparar valores.
- Atualizar variáveis utilizando operadores de atribuição.
- Construir mensagens com f-strings.
- Trabalhar com lógica booleana.
- Diferenciar igualdade (`==`) de identidade (`is`).
- Verificar se elementos pertencem a uma sequência utilizando `in` e `not in`.

---

# Resumo Final

Ao concluir este módulo, passei a dominar os principais operadores da linguagem Python. Com eles, consigo realizar cálculos, comparar valores, modificar variáveis, construir mensagens dinâmicas e criar expressões lógicas, formando a base necessária para desenvolver estruturas condicionais (`if`, `elif` e `else`) e estruturas de repetição (`for` e `while`) nos próximos módulos.