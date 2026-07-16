# Operadores Aritméticos

## Objetivo

Os operadores aritméticos são utilizados para realizar operações matemáticas entre valores numéricos. Eles permitem efetuar cálculos, criar fórmulas e resolver problemas de lógica dentro dos programas.

---

# Operadores

## Adição (`+`)

Realiza a soma entre dois valores.

```python
a = 10
b = 5

resultado = a + b
print(resultado)
```

**Saída:**

```text
15
```

---

## Subtração (`-`)

Realiza a diferença entre dois valores.

```python
a = 10
b = 5

resultado = a - b
print(resultado)
```

**Saída:**

```text
5
```

---

## Multiplicação (`*`)

Multiplica dois valores.

```python
a = 10
b = 5

resultado = a * b
print(resultado)
```

**Saída:**

```text
50
```

---

## Divisão (`/`)

Realiza a divisão comum.

Sempre retorna um número do tipo **float**, mesmo quando o resultado é inteiro.

```python
print(10 / 2)
```

**Saída:**

```text
5.0
```

Tipo retornado:

```python
type(10 / 2)
```

```text
<class 'float'>
```

---

## Divisão Inteira (`//`)

Retorna apenas a parte inteira da divisão, descartando a parte decimal.

```python
print(10 // 3)
```

**Saída:**

```text
3
```

Outro exemplo:

```python
print(10 // 2)
```

```text
5
```

Tipo retornado:

```python
<class 'int'>
```

---

## Operador Módulo (`%`)

Retorna o resto da divisão.

```python
print(20 % 6)
```

**Saída:**

```text
2
```

Outro exemplo:

```python
print(10 % 2)
```

```text
0
```

Esse operador é muito utilizado para verificar números pares e ímpares.

Exemplo:

```python
numero = 7

print(numero % 2)
```

Como o resto é **1**, o número é ímpar.

---

## Potenciação (`**`)

Eleva um número a outro.

```python
print(10 ** 2)
```

**Saída:**

```text
100
```

Outro exemplo:

```python
print(2 ** 5)
```

```text
32
```

---

# Ordem de Precedência

O Python segue uma ordem de prioridade nas operações matemáticas.

1. Parênteses `()`
2. Potenciação `**`
3. Multiplicação `*`
4. Divisão `/`
5. Divisão inteira `//`
6. Módulo `%`
7. Adição `+`
8. Subtração `-`

Exemplo:

```python
print(10 + 3 * 2)
```

Primeiro:

```text
3 × 2 = 6
```

Depois:

```text
10 + 6 = 16
```

Resultado:

```text
16
```

Agora:

```python
print((10 + 3) * 2)
```

Primeiro:

```text
10 + 3 = 13
```

Depois:

```text
13 × 2 = 26
```

Resultado:

```text
26
```

---

# Observações Importantes

- `/` sempre retorna um `float`.
- `//` retorna apenas a parte inteira da divisão.
- `%` retorna o resto da divisão.
- `**` representa potência.
- O uso de parênteses altera a prioridade das operações e torna o código mais legível.

---

# Erro que cometi durante os estudos

Durante os exercícios, confundi o operador:

```python
&
```

com

```python
%
```

O operador correto para obter o resto da divisão é:

```python
%
```

Já o operador:

```python
&
```

é um operador **bit a bit (AND)**, estudado posteriormente.

Foi apenas uma coincidência que:

```python
20 & 6
```

e

```python
20 % 6
```

retornaram o mesmo valor (`4`) nesse caso específico.

---

# O que aprendi nesta aula

- Como utilizar todos os operadores aritméticos.
- Diferença entre divisão comum e divisão inteira.
- Como obter o resto de uma divisão usando `%`.
- Como calcular potências utilizando `**`.
- Como funciona a ordem de precedência dos operadores.
- A importância de utilizar parênteses para controlar a ordem dos cálculos.