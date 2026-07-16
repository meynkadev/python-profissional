# Aula 04 - Entrada de Dados (`input()`)

## O que é a função `input()`?

A função `input()` permite que o programa receba informações digitadas pelo usuário através do teclado.

Quando o Python encontra um `input()`, a execução do programa é interrompida até que o usuário digite uma informação e pressione a tecla **Enter**.

### Sintaxe

```python
nome = input("Digite seu nome: ")
```

Neste exemplo, o texto **"Digite seu nome:"** é exibido na tela, e o valor digitado pelo usuário é armazenado na variável `nome`.

---

# Funcionamento do `input()`

Fluxo de execução:

```
Programa inicia
        ↓
Encontra o input()
        ↓
Exibe a mensagem ao usuário
        ↓
Espera o usuário digitar
        ↓
Usuário pressiona Enter
        ↓
O programa continua a execução
```

---

# O tipo de dado retornado pelo `input()`

Independentemente do que o usuário digite, o `input()` sempre retorna uma **string** (`str`).

Exemplo:

```python
idade = input("Digite sua idade: ")

print(type(idade))
```

Se o usuário digitar:

```
25
```

O resultado será:

```
<class 'str'>
```

Mesmo que o usuário digite apenas números, o Python interpreta a entrada como texto.

---

# Conversão de tipos após o `input()`

Quando for necessário realizar operações matemáticas, é preciso converter a entrada para o tipo adequado.

Exemplo:

```python
idade = int(input("Digite sua idade: "))
```

Agora a variável `idade` será do tipo inteiro (`int`) e poderá ser utilizada em cálculos.

Outro exemplo:

```python
altura = float(input("Digite sua altura: "))
```

---

# Por que o `input()` retorna uma string?

O Python não tenta adivinhar o significado da informação digitada.

Por exemplo:

```
001234
```

Pode representar:

- um número;
- um CEP;
- um código de cliente;
- uma matrícula;
- uma conta bancária.

Por isso, o Python retorna exatamente o que foi digitado, deixando para o programador decidir como tratar aquela informação.

---

# Operadores com strings

## Concatenação (`+`)

Quando o operador `+` é utilizado entre duas strings, elas são unidas.

Exemplo:

```python
print("Olá " + "Mundo")
```

Resultado:

```
Olá Mundo
```

Outro exemplo:

```python
idade = input("Idade: ")

print(idade + idade)
```

Se o usuário digitar:

```
10
```

Resultado:

```
1010
```

Neste caso, não ocorre uma soma matemática, mas sim uma concatenação de textos.

---

## Repetição (`*`)

O operador `*` pode ser utilizado para repetir uma string várias vezes.

Exemplo:

```python
print("=" * 30)
```

Resultado:

```
==============================
```

Outro exemplo:

```python
print("Python " * 3)
```

Resultado:

```
Python Python Python
```

Esse recurso é muito utilizado para criar separadores e organizar a saída de programas no terminal.

---

# Resumo da aula

- `input()` recebe dados digitados pelo usuário.
- O programa fica pausado até que o usuário pressione **Enter**.
- O retorno do `input()` é sempre uma **string**.
- Para realizar cálculos, é necessário converter a entrada usando `int()` ou `float()`.
- O operador `+` entre strings realiza concatenação.
- O operador `*` entre string e inteiro realiza repetição da string.

---

# Boas práticas

- Sempre verifique qual tipo de dado será necessário antes de utilizar uma entrada do usuário.
- Faça a conversão de tipos logo após o `input()` quando o valor precisar ser utilizado em cálculos.
- Utilize mensagens claras para orientar o usuário durante a digitação.

Exemplo:

```python
idade = int(input("Digite sua idade: "))
```

Em vez de:

```python
idade = input("Idade")
```

Mensagens claras tornam o programa mais fácil de utilizar.

---

# O que aprendi nesta aula

✓ Programas podem receber informações digitadas pelo usuário através da função `input()`.

✓ O `input()` sempre retorna uma string, independentemente do conteúdo digitado.

✓ Quando necessário, o programador deve converter a entrada para o tipo adequado utilizando funções como `int()` e `float()`.

✓ O comportamento dos operadores depende do tipo dos dados:

- `+` entre números realiza soma.
- `+` entre strings realiza concatenação.
- `*` entre número e string realiza repetição da string.