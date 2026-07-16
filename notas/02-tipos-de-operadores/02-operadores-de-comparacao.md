# Aula 2 – Operadores de Comparação

## Objetivo da aula

Aprender a comparar valores em Python utilizando operadores relacionais. Essas comparações retornam valores booleanos (`True` ou `False`) e são fundamentais para estruturas de decisão, como `if`, `elif` e `while`.

---

# Operadores de Comparação

| Operador | Significado | Exemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `10 == 10` | `True` |
| `!=` | Diferente de | `10 != 5` | `True` |
| `>` | Maior que | `10 > 5` | `True` |
| `<` | Menor que | `10 < 5` | `False` |
| `>=` | Maior ou igual a | `10 >= 10` | `True` |
| `<=` | Menor ou igual a | `5 <= 10` | `True` |

---

# Operador de atribuição × Operador de comparação

É importante não confundir os operadores `=` e `==`.

## Operador de atribuição (`=`)

É utilizado para armazenar um valor em uma variável.

```python
idade = 18
```

## Operador de comparação (`==`)

É utilizado para verificar se dois valores são iguais.

```python
idade == 18
```

---

# Valores booleanos

Toda comparação retorna um valor booleano.

```python
print(10 > 5)
```

Resultado:

```text
True
```

Outro exemplo:

```python
print(5 > 10)
```

Resultado:

```text
False
```

---

# Exemplos

```python
idade = 20

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)
```

Saída:

```text
False
True
True
False
True
False
```

---

# Comparando duas variáveis

```python
numero1 = 25
numero2 = 40

print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 > numero2)
print(numero1 < numero2)
print(numero1 >= numero2)
print(numero1 <= numero2)
```

---

# Onde esses operadores são utilizados?

Os operadores de comparação são amplamente utilizados em:

- Estruturas condicionais (`if`, `elif` e `else`);
- Estruturas de repetição (`while`);
- Validação de dados;
- Regras de negócio;
- Comparação entre valores e variáveis.

---

# Boas práticas

- Utilize nomes de variáveis claros e descritivos.
- Evite comparações desnecessárias.
- Utilize f-strings para organizar melhor a saída do programa.
- Faça testes alterando os valores das variáveis para compreender o comportamento de cada operador.

---

# Resumo

- `=` → atribui um valor a uma variável.
- `==` → verifica se dois valores são iguais.
- `!=` → verifica se dois valores são diferentes.
- `>` → verifica se um valor é maior que outro.
- `<` → verifica se um valor é menor que outro.
- `>=` → verifica se um valor é maior ou igual ao outro.
- `<=` → verifica se um valor é menor ou igual ao outro.
- Toda comparação retorna um valor booleano: `True` ou `False`.

---

# O que aprendi nesta aula

- Compreendi a diferença entre atribuição (`=`) e comparação (`==`).
- Aprendi a utilizar todos os operadores de comparação.
- Entendi que qualquer comparação retorna um valor booleano (`True` ou `False`).
- Pratiquei comparações entre variáveis e valores numéricos.
- Resolvi exercícios utilizando todos os operadores de comparação.

---

# Próxima aula

Na próxima aula estudaremos os **operadores lógicos** (`and`, `or` e `not`), que permitem combinar múltiplas condições para criar expressões mais poderosas e são essenciais para construir decisões mais complexas em Python.