# Interpolação de Variáveis

## Objetivo

Aprender a inserir valores de variáveis dentro de uma string de forma organizada e legível.

---

# O que é interpolação?

Interpolar significa inserir o valor de uma variável ou de uma expressão dentro de uma string.

Exemplo:

```python
nome = "Meynkâ"

print(f"Olá, {nome}!")
```

Saída:

```
Olá, Meynkâ!
```

---

# Formas de interpolação

## 1. f-string (Recomendada)

É a forma mais moderna e utilizada atualmente.

```python
nome = "Meynkâ"
idade = 25

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Também permite utilizar expressões.

```python
print(f"Daqui a um ano terei {idade + 1} anos.")
```

É possível chamar métodos diretamente.

```python
nome = "meynkâ"

print(f"{nome.upper()}")
```

---

## 2. Método format()

Forma muito utilizada antes das f-strings.

```python
print("Nome: {}".format(nome))
```

Também aceita múltiplos valores.

```python
print("Nome: {} | Idade: {}".format(nome, idade))
```

E parâmetros nomeados.

```python
print("Nome: {n} | Idade: {i}".format(n=nome, i=idade))
```

---

## 3. Operador %

Forma mais antiga de interpolação.

```python
print("Nome: %s" % nome)
```

Para números inteiros:

```python
print("Idade: %d" % idade)
```

Ainda aparece em códigos antigos, mas raramente é utilizada em novos projetos.

---

# Comparação

| Método | Situação atual |
|---------|----------------|
| f-string | ✅ Recomendado |
| format() | Ainda bastante encontrado |
| % | Código legado |

---

# Expressões em f-strings

As chaves não servem apenas para variáveis.

Também podem conter expressões.

```python
print(f"{10 + 5}")
```

Resultado:

```
15
```

Também é possível utilizar métodos.

```python
print(f"{nome.strip().title()}")
```

---

# Conceitos importantes

- Interpolação cria uma nova string.
- As variáveis originais não são alteradas.
- f-strings são mais legíveis e rápidas.
- Dentro das chaves podem existir variáveis, expressões e chamadas de métodos.

---

# Boas práticas

- Preferir f-strings em projetos novos.
- Utilizar nomes claros para as variáveis.
- Evitar concatenação quando houver interpolação.
- Aproveitar expressões simples dentro das chaves.

---

# Resumo

Nesta aula aprendi que:

- Existem três formas principais de interpolar strings.
- A forma recomendada é utilizar f-strings.
- As chaves aceitam variáveis, expressões e métodos.
- A interpolação apenas constrói uma nova string e não altera as variáveis utilizadas.