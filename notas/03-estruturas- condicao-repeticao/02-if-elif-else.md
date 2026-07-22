# Aula 02 - Estruturas Condicionais (`if`, `elif`, `else`)

## Objetivo

Aprender como fazer o programa tomar decisões com base em condições.

---

# Estruturas condicionais

As estruturas condicionais permitem que um programa execute diferentes blocos de código dependendo do resultado de uma condição.

Em Python, as principais estruturas são:

- `if`
- `if...else`
- `if...elif...else`
- Operador ternário

---

# Estrutura `if`

Executa um bloco de código somente quando a condição é verdadeira.

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
```

Se a condição for falsa, o bloco será ignorado.

---

# Estrutura `if...else`

Utilizada quando existem duas possibilidades.

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Sempre um dos dois blocos será executado.

---

# Estrutura `if...elif...else`

Utilizada quando existem várias possibilidades.

```python
nota = 8

if nota >= 9:
    print("Excelente")

elif nota >= 7:
    print("Aprovado")

elif nota >= 5:
    print("Recuperação")

else:
    print("Reprovado")
```

O Python verifica as condições de cima para baixo.

Assim que encontra uma condição verdadeira, executa aquele bloco e ignora os demais.

---

# Operador ternário

Permite escrever um `if...else` simples em apenas uma linha.

```python
saldo = 100

mensagem = "Positivo" if saldo > 0 else "Negativo"

print(mensagem)
```

Equivale a:

```python
if saldo > 0:
    mensagem = "Positivo"
else:
    mensagem = "Negativo"
```

---

# Diferença entre vários `if` e `if...elif`

## Vários `if`

Cada condição é analisada de forma independente.

```python
idade = 20

if idade >= 18:
    print("Maior")

if idade >= 16:
    print("Pode entrar")
```

As duas mensagens serão exibidas.

---

## `if...elif...else`

Apenas um bloco será executado.

```python
idade = 20

if idade >= 18:
    print("Maior")

elif idade >= 16:
    print("Pode entrar")
```

Depois que uma condição é satisfeita, as demais não são verificadas.

---

# Fluxo de execução

O Python avalia as condições na ordem em que aparecem.

```
if
 ↓
verdadeiro?
 ↓
Sim → executa o bloco → fim

Não
 ↓
elif
 ↓
verdadeiro?
 ↓
Sim → executa o bloco → fim

Não
 ↓
else
 ↓
executa o bloco
```

---

# Onde essa estrutura é utilizada?

- Sistemas de login
- Validação de usuários
- Controle de acesso
- Sistemas bancários
- Jogos
- Lojas virtuais
- Automações
- APIs
- Aplicações web

Praticamente todo software utiliza estruturas condicionais.

---

# Boas práticas

- Escreva condições simples e objetivas.
- Utilize `elif` quando houver várias possibilidades.
- Evite criar muitos níveis de indentação.
- Use nomes de variáveis claros.
- Organize os casos do mais específico para o mais geral.

---

# Resumo da aula

Nesta aula aprendi:

- Como utilizar o `if`.
- Como utilizar `if...else`.
- Como utilizar `if...elif...else`.
- Como funciona o operador ternário.
- A diferença entre vários `if` e uma cadeia `if...elif`.
- Que o Python executa apenas o primeiro bloco verdadeiro em uma estrutura `if...elif...else`.
- Como utilizar estruturas condicionais para controlar o fluxo de execução de um programa.

---

# Conceitos-chave

- `if` → executa um bloco se a condição for verdadeira.
- `else` → executa quando todas as condições anteriores forem falsas.
- `elif` → adiciona novas condições.
- Operador ternário → simplifica um `if...else` simples.
- O Python verifica as condições de cima para baixo.
- Apenas o primeiro bloco verdadeiro é executado em uma cadeia `if...elif...else`.