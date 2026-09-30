# Aula 2 — Métodos de Dicionários

## Objetivo

Aprender os principais métodos para atualizar, consultar, copiar, criar, remover e percorrer dicionários em Python.

## Métodos estudados

### `update()`

Atualiza valores de chaves existentes e também adiciona novas chaves.

```python
product.update({
    "price": 180,
    "brand": "Logitech"
})
```

- Chave existente → valor é atualizado.
- Chave inexistente → chave é adicionada.

### `setdefault()`

Adiciona uma chave somente se ela ainda não existir.

```python
user.setdefault("city", "Porto Alegre")
```

- Chave inexistente → cria a chave com o valor informado.
- Chave existente → mantém o valor atual.
- Retorna o valor associado à chave.

**Regra mental:** `setdefault()` = “coloque esse valor se ainda não existir”.

### `copy()`

Cria uma cópia independente do dicionário.

```python
backup = user.copy()
```

Alterações posteriores em `user` não alteram `backup` nesse caso.

> `backup = user` não cria uma cópia; as duas variáveis apontam para o mesmo dicionário.

### `fromkeys()`

Cria um dicionário a partir de uma sequência de chaves, usando o mesmo valor inicial.

```python
fields = ["name", "email", "phone"]
contact = dict.fromkeys(fields, "")
```

Resultado:

```python
{
    "name": "",
    "email": "",
    "phone": ""
}
```

### `pop()`

Remove uma chave e retorna o valor removido.

```python
removed = product.pop("price")
```

É possível fornecer um valor padrão para evitar `KeyError`:

```python
removed = product.pop("phone", "Not informed")
```

### `popitem()`

Remove e retorna o último par chave-valor inserido no dicionário.

```python
key, value = product.popitem()
```

O resultado é um par, como:

```python
("stock", 10)
```

### `clear()`

Remove todos os pares chave-valor, mas mantém o dicionário existente.

```python
user.clear()
```

Depois:

```python
{}
```

Diferença:

```python
user.clear()
```

→ dicionário continua existindo, mas vazio.

```python
del user
```

→ a variável `user` deixa de existir.

### `keys()`

Fornece as chaves do dicionário.

```python
for key in user.keys():
    print(key)
```

Também é possível iterar diretamente:

```python
for key in user:
    print(key)
```

### `values()`

Fornece os valores do dicionário.

```python
for value in user.values():
    print(value)
```

### `items()`

Fornece pares `(chave, valor)`.

```python
for key, value in user.items():
    print(key, value)
```

Nesse caso ocorre **desempacotamento** do par em duas variáveis.

Também é possível receber o par inteiro:

```python
for item in user.items():
    print(item)
```

## Regra mental

| Método | Função principal |
|---|---|
| `update()` | Atualizar/adicionar pares |
| `setdefault()` | Adicionar somente se a chave não existir |
| `copy()` | Criar uma cópia do dicionário |
| `fromkeys()` | Criar dicionário a partir de chaves |
| `pop()` | Remover uma chave e retornar seu valor |
| `popitem()` | Remover e retornar o último par |
| `clear()` | Esvaziar o dicionário |
| `keys()` | Obter as chaves |
| `values()` | Obter os valores |
| `items()` | Obter chave e valor |

## Conceitos consolidados

- Distinguir atualização de adição condicional.
- Diferenciar cópia de referência.
- Entender métodos que removem elementos e retornam valores.
- Percorrer chaves, valores ou pares chave-valor.
- Usar desempacotamento com `items()`.
