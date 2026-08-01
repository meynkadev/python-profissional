# Strings de Múltiplas Linhas

## Objetivo

Aprender a criar textos com várias linhas utilizando aspas triplas (`"""` ou `'''`).

---

# O que são?

Strings de múltiplas linhas permitem escrever textos exatamente como eles devem aparecer na saída.

Exemplo:

```python
mensagem = """
Olá!

Bem-vindo ao curso de Python.
Bom estudo!
"""

print(mensagem)
```

---

# Formas de criar

Com aspas duplas:

```python
texto = """
Primeira linha
Segunda linha
"""
```

Com aspas simples:

```python
texto = '''
Primeira linha
Segunda linha
'''
```

As duas funcionam da mesma forma.

---

# Utilizando f-string

Também é possível interpolar variáveis.

```python
nome = "Meynkâ"

texto = f"""
Olá, {nome}!

Bem-vindo!
"""

print(texto)
```

---

# Aplicações

- Menus de terminal
- Mensagens de boas-vindas
- Relatórios
- E-mails
- Consultas SQL
- Templates HTML
- Documentação (Docstrings)

---

# Vantagens

- Código mais organizado.
- Evita vários `print()`.
- Facilita manutenção.
- Preserva a formatação do texto.

---

# Boas práticas

- Utilize múltiplas linhas apenas quando o texto realmente possuir várias linhas.
- Utilize f-string quando precisar inserir variáveis.
- Organize o texto para facilitar a leitura.

---

# Resumo

Nesta aula aprendi que:

- Posso utilizar `"""` ou `'''`.
- As quebras de linha são preservadas.
- Posso utilizar f-strings normalmente.
- É muito utilizado para menus, documentação e mensagens longas.