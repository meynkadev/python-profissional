# Conhecendo Python

## Conversão de tipos

Conversão de tipos (Casting) é o processo de transformar um valor de um tipo de dado em outro.

Exemplos:

```python
int("10")
float("10")
str(10)
bool(10)
```

---

# int()

Converte um valor para um número inteiro.

### Exemplo

```python
idade = int("25")
```

Resultado

```python
25
```

Tipo retornado

```python
<class 'int'>
```

### Quando utilizar

- Converter valores digitados pelo usuário (`input()`)
- Transformar textos contendo números em inteiros
- Fazer cálculos matemáticos

---

# float()

Converte um valor para um número decimal.

### Exemplo

```python
altura = float("1.75")
```

Resultado

```python
1.75
```

Tipo retornado

```python
<class 'float'>
```

### Quando utilizar

- Trabalhar com números decimais
- Médias
- Porcentagens
- Valores monetários

---

# str()

Converte qualquer valor para texto.

### Exemplo

```python
idade = str(25)
```

Resultado

```python
"25"
```

Tipo retornado

```python
<class 'str'>
```

### Quando utilizar

- Exibir mensagens
- Concatenar textos
- Gerar relatórios
- Salvar dados em arquivos

---

# bool()

Converte um valor para verdadeiro ou falso.

## Valores que retornam False

```python
bool(0)
```

↓

```python
False
```

```python
bool(0.0)
```

↓

```python
False
```

```python
bool("")
```

↓

```python
False
```

---

## Valores que retornam True

```python
bool(100)
```

↓

```python
True
```

```python
bool(-5)
```

↓

```python
True
```

```python
bool(3.14)
```

↓

```python
True
```

```python
bool("Python")
```

↓

```python
True
```

```python
bool("False")
```

↓

```python
True
```

> Atenção:
>
> `"False"` é um texto.
>
> Não é o mesmo que `False`.

---

# Resumo

| Conversão | Exemplo | Resultado |
|-----------|----------|-----------|
| int() | int("200") | 200 |
| float() | float("200") | 200.0 |
| str() | str(200) | "200" |
| bool() | bool(0) | False |
| bool() | bool(100) | True |
| bool() | bool("") | False |
| bool() | bool("Python") | True |

---

# Observações importantes

- `int()` transforma textos numéricos em inteiros.
- `float()` transforma valores em números decimais.
- `str()` transforma qualquer valor em texto.
- `bool()` verifica se um valor é considerado verdadeiro ou falso pelo Python.
- Strings vazias retornam `False`.
- Strings com qualquer conteúdo retornam `True`.
- Qualquer número diferente de zero retorna `True`.

---

# O que aprendi nesta aula

✓ O Python permite converter tipos de dados usando funções nativas.

✓ Nem toda conversão altera a variável original. É necessário armazenar o resultado da conversão.

Exemplo:

```python
idade = "25"

idade = int(idade)
```

✓ O `type()` permite verificar o tipo atual de uma variável.

✓ O `bool()` não verifica o significado de uma palavra, apenas se o valor é considerado vazio ou não.

Exemplo:

```python
bool("False")
```

Resultado:

```python
True
```

porque `"False"` é apenas uma string não vazia.