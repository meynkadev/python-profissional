# Aula 1 – Indentação e Blocos

## Objetivo da aula

Compreender o funcionamento da indentação em Python e entender como ela define os blocos de código da aplicação.

---

# O que é indentação?

Indentação é o espaço existente no início de uma linha de código.

Diferente de muitas linguagens de programação, em Python a indentação faz parte da sintaxe da linguagem.

Ela não serve apenas para organizar visualmente o código, mas também para indicar quais instruções pertencem ao mesmo bloco.

---

# O que é um bloco de código?

Um bloco é um conjunto de instruções que pertencem à mesma estrutura.

Exemplo:

```python
idade = 20

if idade >= 18:
    print("Maior de idade")

print("Fim do programa")
```

Neste exemplo existem dois blocos:

- Bloco principal do programa.
- Bloco pertencente ao `if`.

Quando a indentação retorna ao nível anterior, o Python entende que o bloco foi encerrado.

---

# Como o Python interpreta os blocos?

Sempre que uma estrutura termina com dois pontos (`:`), o Python espera um novo bloco indentado.

Exemplo:

```python
if idade >= 18:
    print("Maior de idade")
```

Se a condição for verdadeira, todas as instruções indentadas serão executadas.

---

# Blocos aninhados

Um bloco pode conter outro bloco.

Exemplo:

```python
idade = 20

if idade >= 18:
    print("Maior de idade")

    if idade >= 60:
        print("Pessoa idosa")

print("Fim")
```

Neste código existem três blocos:

- Bloco principal.
- Bloco do primeiro `if`.
- Bloco do segundo `if`.

Cada novo nível de indentação cria um novo bloco.

---

# Erros de indentação

Se um bloco obrigatório não estiver indentado corretamente, o Python gera um erro.

Exemplo incorreto:

```python
if True:
print("Olá")
```

Resultado:

```text
IndentationError
```

Outro erro comum é utilizar uma indentação sem existir um bloco correspondente.

Exemplo:

```python
print("Olá")
    print("Python")
```

Nesse caso, o Python também gera um erro de indentação.

---

# Fluxo de execução

O Python executa o código de cima para baixo.

Quando encontra uma estrutura condicional, verifica se a condição é verdadeira.

- Se for verdadeira, executa o bloco indentado.
- Se for falsa, ignora esse bloco e continua a execução normalmente.

---

# Boas práticas

- Utilize sempre quatro espaços para cada nível de indentação.
- Mantenha todas as instruções do mesmo bloco alinhadas.
- Evite misturar espaços e tabulações.
- Utilize a indentação para tornar o código mais legível.

---

# Resumo

- A indentação faz parte da sintaxe do Python.
- Um bloco de código é definido pela indentação.
- Sempre que um bloco termina, a indentação retorna ao nível anterior.
- Blocos podem conter outros blocos (blocos aninhados).
- Uma indentação incorreta gera erro de execução.

---

# O que aprendi nesta aula

- Compreendi que a indentação define a estrutura do programa.
- Aprendi a identificar blocos de código.
- Entendi como o Python interpreta blocos aninhados.
- Aprendi a reconhecer erros de indentação.
- Desenvolvi a habilidade de acompanhar o fluxo de execução de um programa por meio dos blocos de código.