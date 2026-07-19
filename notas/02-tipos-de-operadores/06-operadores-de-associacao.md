# Operadores de Associação (`in` e `not in`)

## Objetivo

Os operadores de associação verificam se um elemento pertence ou não a uma sequência, como strings, listas, tuplas, conjuntos e dicionários.

---

# Operadores

| Operador | Significado |
|----------|-------------|
| `in` | Verifica se o elemento existe |
| `not in` | Verifica se o elemento não existe |

---

# Exemplos com String

```python
curso = "Python"

print("Py" in curso)       # True
print("Java" in curso)     # False
print("Java" not in curso) # True
```

---

# Exemplos com Lista

```python
disciplinas = [
    "Python",
    "Git",
    "Linux"
]

print("Git" in disciplinas)      # True
print("Docker" in disciplinas)   # False
print("Docker" not in disciplinas) # True
```

---

# Como funciona

O Python percorre a sequência procurando o elemento informado.

Se encontrar:

```python
True
```

Se não encontrar:

```python
False
```

---

# Onde são utilizados?

- Verificar se um usuário existe.
- Procurar palavras em textos.
- Validar opções de menus.
- Conferir itens em listas.
- Verificar permissões.
- Buscar valores em coleções.

---

# Boas práticas

- Utilize `in` em vez de várias comparações com `or`.
- Prefira nomes claros para listas e variáveis.
- Lembre-se de que a comparação diferencia letras maiúsculas e minúsculas.

Exemplo:

```python
"Python" == "python"
```

Resultado:

```python
False
```

---

# Resumo

- `in` verifica se um elemento pertence à sequência.
- `not in` verifica se o elemento não pertence.
- Funciona com strings, listas, tuplas, conjuntos e dicionários.
- É muito utilizado em validações, buscas e regras de negócio.