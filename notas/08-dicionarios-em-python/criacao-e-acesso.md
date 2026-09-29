# Dicionários em Python — Aula 1

## Objetivo da aula

Aprender a criar, acessar, alterar e percorrer dicionários em Python, compreendendo a relação entre **chaves** e **valores**.

\---

## 1\. Criação de dicionários

Dicionários armazenam dados no formato:

```python
chave: valor
```

Exemplo:

```python
person = {
    "name": "Meynka",
    "age": 25,
    "language": "Python"
}
```

\---

## 2\. Acesso aos valores

Os valores são acessados por meio das chaves:

```python
print(person\["name"])
print(person\["language"])
```

\---

## 3\. Alteração e adição de dados

Dicionários são mutáveis.

Alterar um valor existente:

```python
person\["age"] = 26
```

Adicionar uma nova chave:

```python
person\["city"] = "Porto Alegre"
```

\---

## 4\. Acesso com `get()`

Ao utilizar `dict\["key"]`, uma chave inexistente gera `KeyError`.

```python
print(person\["email"])
```

Para realizar um acesso seguro:

```python
print(person.get("email"))
```

Se a chave não existir, `get()` retorna `None`.

Também podemos definir um valor padrão:

```python
print(person.get("email", "Not informed"))
```

\---

## 5\. Verificação de chaves

O operador `in` verifica se uma chave existe:

```python
if "name" in person:
    print("Name exists")
```

Também podemos utilizar `not in`:

```python
if "email" not in person:
    print("Email does not exist")
```

\---

## 6\. Percorrendo um dicionário

Ao utilizar `for` diretamente em um dicionário, percorremos suas chaves:

```python
for key in person:
    print(key)
```

### `keys()`

Retorna as chaves:

```python
for key in person.keys():
    print(key)
```

### `values()`

Retorna os valores:

```python
for value in person.values():
    print(value)
```

### `items()`

Retorna os pares de chave e valor:

```python
for key, value in person.items():
    print(key, value)
```

O `items()` utiliza o conceito de **unpacking**, já estudado anteriormente com tuplas.

\---

## 7\. Remoção de elementos

### `pop()`

Remove uma chave e retorna o valor removido:

```python
removed\_price = product.pop("price")
```

### `popitem()`

Remove e retorna o último par de chave e valor:

```python
removed\_item = product.popitem()
```

### `del`

Remove uma chave específica:

```python
del product\["stock"]
```

### `clear()`

Remove todos os elementos:

```python
product.clear()
```

\---

## Conceitos importantes

* Dicionários armazenam dados em pares **chave → valor**.
* Cada chave deve ser única.
* Dicionários são mutáveis.
* `dict\["key"]` acessa diretamente um valor e gera `KeyError` se a chave não existir.
* `get()` permite acessar uma chave sem gerar `KeyError`.
* `in` e `not in` verificam a existência de chaves.
* `for` percorre as chaves por padrão.
* `keys()` retorna as chaves.
* `values()` retorna os valores.
* `items()` retorna pares de chave e valor.
* `pop()` remove uma chave e devolve seu valor.
* `del` remove uma chave sem devolvê-la.
* `clear()` esvazia o dicionário.

\---

## Conhecimentos adquiridos

Ao concluir esta parte da aula consigo:

* Criar dicionários.
* Acessar valores por meio das chaves.
* Alterar valores existentes.
* Adicionar novas chaves.
* Identificar o comportamento de `KeyError`.
* Utilizar `get()` com e sem valor padrão.
* Verificar a existência de chaves.
* Percorrer chaves, valores e pares de chave/valor.
* Remover elementos de um dicionário.
* Diferenciar `pop()`, `del`, `popitem()` e `clear()`.

\---

## Observação

Os demais **métodos da classe `dict`** serão estudados na próxima aula.

