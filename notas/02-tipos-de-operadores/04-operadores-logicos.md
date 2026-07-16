# Aula 4 – Operadores Lógicos

## Objetivo da aula

Aprender a combinar e inverter condições utilizando os operadores lógicos `and`, `or` e `not`. Esses operadores são essenciais para construir regras de decisão em programas, sendo amplamente utilizados em estruturas condicionais (`if`, `elif` e `else`).

---

# O que são operadores lógicos?

Operadores lógicos permitem combinar duas ou mais condições, produzindo um único resultado booleano (`True` ou `False`).

---

# Operador `and`

O operador `and` retorna `True` somente quando **todas** as condições são verdadeiras.

## Sintaxe

```python
condicao1 and condicao2
```

## Exemplos

```python
idade = 20

print(idade >= 18 and idade <= 30)
```

Resultado:

```text
True
```

Outro exemplo:

```python
idade = 15

print(idade >= 18 and idade <= 30)
```

Resultado:

```text
False
```

---

# Operador `or`

O operador `or` retorna `True` quando **pelo menos uma** das condições é verdadeira.

## Sintaxe

```python
condicao1 or condicao2
```

## Exemplo

```python
idade = 16

print(idade >= 18 or idade <= 30)
```

Resultado:

```text
True
```

Porque uma das condições é verdadeira.

---

# Operador `not`

O operador `not` inverte o valor lógico de uma expressão.

## Sintaxe

```python
not expressao
```

## Exemplo

```python
ativo = True

print(not ativo)
```

Resultado:

```text
False
```

Outro exemplo:

```python
ativo = False

print(not ativo)
```

Resultado:

```text
True
```

---

# Exemplos práticos

## Verificando se uma pessoa pode dirigir

```python
idade = 22
possui_cnh = True

print(f"Maior de idade: {idade >= 18}")
print(f"Possui CNH: {possui_cnh}")
print(f"Pode dirigir: {idade >= 18 and possui_cnh}")
print(f"Atende a pelo menos um requisito: {idade >= 18 or possui_cnh}")
print(f"Não possui CNH? {not possui_cnh}")
```

---

## Validação de login

```python
usuario = "admin"
senha = "123456"

login_valido = usuario == "admin" and senha == "123456"

print(f"Login válido: {login_valido}")
print(f"Login inválido: {not login_valido}")
```

Esse exemplo demonstra como os operadores lógicos são utilizados em sistemas reais para validar usuários e senhas.

---

# Tabela resumo

| Operador | Significado | Exemplo | Resultado |
|----------|-------------|---------|-----------|
| `and` | Todas as condições devem ser verdadeiras | `True and True` | `True` |
| `or` | Pelo menos uma condição deve ser verdadeira | `True or False` | `True` |
| `not` | Inverte o valor lógico | `not True` | `False` |

---

# Onde os operadores lógicos são utilizados?

Os operadores lógicos aparecem constantemente em:

- Estruturas condicionais (`if`, `elif` e `else`);
- Sistemas de login;
- Controle de acesso;
- Validação de formulários;
- Regras de negócio;
- Jogos;
- Sistemas bancários;
- Comércio eletrônico.

---

# Boas práticas

- Utilize nomes de variáveis claros para representar condições.
- Divida expressões muito grandes em variáveis auxiliares para facilitar a leitura.
- Utilize parênteses quando necessário para tornar expressões complexas mais legíveis.
- Evite criar condições excessivamente longas em uma única linha.

---

# Resumo

- `and` → todas as condições precisam ser verdadeiras.
- `or` → basta uma condição ser verdadeira.
- `not` → inverte o valor lógico de uma expressão.
- Operadores lógicos retornam sempre um valor booleano (`True` ou `False`).
- São fundamentais para a tomada de decisões em programas.

---

# O que aprendi nesta aula

- Compreendi o funcionamento dos operadores `and`, `or` e `not`.
- Aprendi a combinar múltiplas condições.
- Entendi como inverter uma condição utilizando `not`.
- Desenvolvi programas para verificar regras de negócio, como autorização para dirigir e validação de login.
- Percebi que operadores lógicos são essenciais para construir programas que tomam decisões.

---

# Próxima aula

Na próxima aula começaremos a utilizar esses operadores em conjunto com estruturas condicionais, permitindo que os programas executem diferentes ações conforme as condições avaliadas.