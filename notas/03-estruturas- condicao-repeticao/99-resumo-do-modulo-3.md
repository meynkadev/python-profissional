# Resumo do Módulo 3 — Estruturas Condicionais e de Repetição

## Objetivo do módulo

Aprender a controlar o fluxo de execução de um programa, permitindo tomar decisões e executar blocos de código repetidamente de acordo com determinadas condições.

---

# Conteúdos estudados

## 1. Indentação e blocos

A indentação faz parte da sintaxe do Python.

Ela define quais instruções pertencem ao mesmo bloco de código.

Principais conceitos:

- Todo bloco termina quando a indentação termina.
- Python utiliza a indentação no lugar de chaves ({ }).
- Uma indentação incorreta gera `IndentationError`.

---

## 2. Estruturas condicionais

### if

Executa um bloco apenas se a condição for verdadeira.

```python
if idade >= 18:
    print("Maior de idade")
```

---

### if / else

Permite escolher entre duas possibilidades.

```python
if idade >= 18:
    print("Maior")
else:
    print("Menor")
```

---

### elif

Permite testar várias condições em sequência.

```python
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

---

### if aninhado

Um bloco `if` pode existir dentro de outro.

```python
if idade >= 18:
    if idade >= 21:
        print("Pode consumir bebidas nos EUA")
```

---

### Operador ternário

Permite escrever uma decisão simples em uma única linha.

```python
mensagem = "Positivo" if saldo > 0 else "Negativo"
```

---

# Estruturas de repetição

## while

Repete um bloco enquanto uma condição permanecer verdadeira.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Características:

- Baseado em condição.
- O programador controla a repetição.
- Pode gerar loop infinito caso a condição nunca se torne falsa.

---

## for

Percorre automaticamente uma sequência.

```python
frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print(fruta)
```

Características:

- Ideal para listas, tuplas, strings e ranges.
- O Python controla a repetição.
- Não necessita contador manual.

---

## range()

Gera sequências numéricas.

```python
range(5)
```

Resultado:

```
0
1
2
3
4
```

Também pode receber:

```python
range(início, fim)
```

ou

```python
range(início, fim, passo)
```

---

# Diferença entre while e for

| while | for |
|--------|-----|
| Baseado em condição | Baseado em sequência |
| Você controla o contador | O Python controla a repetição |
| Pode gerar loop infinito | Não gera loop infinito por sequência |
| Usado quando não sabemos quantas repetições ocorrerão | Usado quando conhecemos a quantidade de elementos |

---

# Aplicações práticas

## Estruturas condicionais

- Login
- Sistema bancário
- Controle de acesso
- Validação de dados
- Menus

---

## while

- Validação de senha
- Jogos
- Menus
- Tentativas de conexão
- Processos contínuos

---

## for

- Percorrer listas
- Ler arquivos
- Enviar e-mails
- Processar dados
- Automatizar tarefas

---

# Boas práticas

- Utilizar indentação consistente.
- Escrever condições simples e legíveis.
- Evitar muitos níveis de if aninhado.
- Atualizar corretamente a variável de controle do while.
- Utilizar for sempre que houver uma sequência conhecida.
- Escolher nomes descritivos para variáveis.

---

# Resumo Final

Neste módulo aprendi a controlar o fluxo de execução de um programa utilizando estruturas condicionais (`if`, `elif`, `else`) e estruturas de repetição (`while` e `for`).

Também aprendi a utilizar o `range()` para gerar sequências numéricas e compreendi quando utilizar cada estrutura de repetição.

Esse módulo representa a base da lógica de programação em Python e será utilizado praticamente em todos os programas desenvolvidos a partir daqui.