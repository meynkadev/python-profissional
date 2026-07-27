# Estruturas de Repetição

## Objetivo

As estruturas de repetição permitem executar um bloco de código várias vezes sem precisar escrevê-lo repetidamente.

Python possui duas estruturas principais:

- while
- for

---

# Quando utilizar cada uma?

## while

Utilize quando **não souber quantas vezes** a repetição acontecerá.

A repetição continua enquanto uma condição for verdadeira.

Exemplos:

- Enquanto a senha estiver incorreta.
- Enquanto houver conexão.
- Enquanto a bateria for maior que 10%.
- Enquanto o usuário não desejar sair.

Estrutura:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Fluxo:

1. Verifica a condição.
2. Executa o bloco.
3. Atualiza a variável.
4. Volta para a condição.
5. Repete até que a condição seja falsa.

---

# for

Utilize quando **já souber a quantidade de repetições** ou quando desejar percorrer uma coleção de dados.

Exemplos:

- Lista de alunos.
- Produtos.
- Arquivos.
- Caracteres de uma string.

Estrutura:

```python
frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print(fruta)
```

O Python percorre automaticamente todos os elementos.

---

# range()

O range() gera uma sequência numérica.

Exemplo:

```python
for numero in range(5):
    print(numero)
```

Saída:

0
1
2
3
4

O valor final não é incluído.

---

Também pode receber início e fim.

```python
for numero in range(3, 8):
    print(numero)
```

Saída:

3
4
5
6
7

---

Também aceita passo.

```python
for numero in range(0, 11, 2):
    print(numero)
```

Saída:

0
2
4
6
8
10

---

# Diferenças entre while e for

while

- Baseado em condição.
- Você controla a variável.
- Pode gerar loop infinito.
- Ideal quando não sabe quantas repetições ocorrerão.

for

- Baseado em sequência.
- O Python controla a repetição.
- Percorre listas, strings e ranges.
- Ideal quando conhece a quantidade de elementos.

---

# Comparação

while

Pergunta continuamente:

"A condição ainda é verdadeira?"

Se sim, continua.

Se não, termina.

---

for

Pergunta:

"Ainda existe algum elemento para percorrer?"

Se sim, continua.

Quando acabar a sequência, termina automaticamente.

---

# Cuidados

No while:

- Atualizar a variável de controle.
- Evitar loops infinitos.

No for:

- Utilizar nomes claros para a variável de iteração.
- Aproveitar o range() quando a repetição for numérica.

---

# Aplicações práticas

while

- Login
- Validação de senha
- Menus
- Conexões
- Jogos

for

- Processamento de listas
- Leitura de arquivos
- Relatórios
- Automações
- Análise de dados

---

# Resumo

Use while quando a repetição depende de uma condição.

Use for quando a repetição depende de uma quantidade de elementos.

Essa é uma das decisões mais importantes na programação em Python.