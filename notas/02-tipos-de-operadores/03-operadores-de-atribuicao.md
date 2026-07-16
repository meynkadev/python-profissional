# Aula 3 – Operadores de Atribuição

## Objetivo da aula

Aprender a utilizar os operadores de atribuição para modificar o valor de uma variável de forma mais simples e legível, evitando repetir o nome da variável em operações matemáticas.

---

# Operador de atribuição

O operador de atribuição (`=`) é utilizado para armazenar um valor em uma variável.

Exemplo:

```python
saldo = 1000
```

Nesse exemplo, a variável `saldo` passa a armazenar o valor `1000`.

---

# Operadores de atribuição compostos

Os operadores de atribuição compostos combinam uma operação matemática com a atribuição do resultado à própria variável.

## Adição (`+=`)

```python
saldo = 100

saldo += 50
```

Equivale a:

```python
saldo = saldo + 50
```

Resultado:

```text
150
```

---

## Subtração (`-=`)

```python
saldo = 100

saldo -= 20
```

Equivale a:

```python
saldo = saldo - 20
```

Resultado:

```text
80
```

---

## Multiplicação (`*=`)

```python
saldo = 100

saldo *= 3
```

Equivale a:

```python
saldo = saldo * 3
```

Resultado:

```text
300
```

---

## Divisão (`/=`)

```python
saldo = 100

saldo /= 4
```

Equivale a:

```python
saldo = saldo / 4
```

Resultado:

```text
25.0
```

> O operador `/=` sempre retorna um valor do tipo `float`.

---

## Divisão inteira (`//=`)

```python
saldo = 17

saldo //= 5
```

Resultado:

```text
3
```

A parte decimal é descartada.

---

## Módulo (`%=`)

```python
saldo = 10

saldo %= 4
```

Resultado:

```text
2
```

Esse operador atribui à variável o resto da divisão.

---

## Potenciação (`**=`)

```python
valor = 2

valor **= 5
```

Resultado:

```text
32
```

Equivale a:

```python
valor = valor ** 5
```

---

# Vantagens dos operadores de atribuição

- Reduzem a quantidade de código.
- Tornam o código mais limpo e legível.
- Evitam repetir o nome da variável.
- São amplamente utilizados no desenvolvimento profissional.

---

# Exemplos práticos

```python
salario = 2500
bonus = 300
desconto = 150

salario += bonus
print(f"Salário após o bônus: R$ {salario:.2f}")

salario -= desconto
print(f"Salário após o desconto: R$ {salario:.2f}")

salario *= 2
print(f"Salário dobrado: R$ {salario:.2f}")

salario /= 5
print(f"Salário dividido por 5: R$ {salario:.2f}")
```

---

# F-strings

Durante esta aula também pratiquei a utilização de f-strings.

Forma correta:

```python
print(f"Salário: R$ {salario:.2f}")
```

Forma incorreta:

```python
print(f"Salário:", {salario})
```

As chaves `{}` fazem parte da própria f-string e devem estar dentro da string.

---

# Formatação de números

É possível controlar a quantidade de casas decimais utilizando:

```python
:.2f
```

Exemplo:

```python
preco = 1899.9

print(f"Preço: R$ {preco:.2f}")
```

Resultado:

```text
Preço: R$ 1899.90
```

Esse recurso é muito utilizado em sistemas financeiros, relatórios e aplicações comerciais.

---

# Boas práticas

- Utilize operadores de atribuição sempre que desejar atualizar o valor de uma variável.
- Utilize nomes de variáveis claros e descritivos.
- Prefira utilizar f-strings para exibir mensagens.
- Formate valores monetários utilizando duas casas decimais (`:.2f`).

---

# Resumo

- `=` atribui um valor.
- `+=` soma e atribui.
- `-=` subtrai e atribui.
- `*=` multiplica e atribui.
- `/=` divide e atribui.
- `//=` realiza divisão inteira e atribui.
- `%=` calcula o resto da divisão e atribui.
- `**=` realiza potenciação e atribui.

---

# O que aprendi nesta aula

- Compreendi o funcionamento dos operadores de atribuição.
- Aprendi a atualizar valores de variáveis utilizando operadores compostos.
- Pratiquei a utilização de f-strings.
- Aprendi a formatar números com duas casas decimais utilizando `:.2f`.
- Entendi que os operadores de atribuição tornam o código mais limpo, legível e profissional.