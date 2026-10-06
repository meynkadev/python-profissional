# Resumo do Módulo — Dicionários em Python

## Objetivo

Aprender a trabalhar profissionalmente com **dicionários (`dict`) em Python**, entendendo como criar, acessar, modificar, percorrer e remover dados organizados em pares de **chave e valor**.

---

## Aula 1 — Fundamentos de Dicionários

### Aprendi

- Criar dicionários com pares `chave: valor`.
- Acessar valores usando `dict["key"]`.
- Alterar valores de chaves existentes.
- Adicionar novas chaves e valores.
- Entender `KeyError` ao acessar uma chave inexistente com `[]`.
- Usar `get()` para acessar valores sem gerar `KeyError`.
- Usar `get(key, default)` para fornecer um valor padrão.
- Verificar a existência de chaves com `in` e `not in`.
- Percorrer dicionários com `for`.
- Entender que a iteração direta sobre um dicionário percorre suas chaves.
- Conhecer `keys()`, `values()` e `items()`.
- Remover elementos com `pop()`, `popitem()` e `del`.
- Esvaziar um dicionário com `clear()`.

### Conceito importante

Um dicionário organiza dados no formato:

```python
{
    "key": "value"
}
```

A chave identifica o dado e o valor é a informação associada a ela.

---

## Aula 2 — Métodos de Dicionários

### Aprendi

- Usar `update()` para atualizar chaves existentes e adicionar novas chaves.
- Usar `setdefault()` para adicionar uma chave somente quando ela ainda não existe.
- Entender a diferença entre `update()` e `setdefault()`.
- Usar `copy()` para criar uma cópia independente do dicionário.
- Diferenciar uma cópia de uma simples referência:
  - `backup = user` → mesma referência.
  - `backup = user.copy()` → novo dicionário.
- Usar `dict.fromkeys()` para criar um dicionário a partir de várias chaves com um valor inicial.
- Usar `pop()` para remover uma chave e obter o valor removido.
- Usar o valor padrão de `pop()` para evitar `KeyError`.
- Usar `popitem()` para remover e retornar o último par inserido.
- Usar `clear()` para remover todos os pares sem excluir o dicionário.
- Diferenciar `clear()` de `del`.
- Usar `keys()` para percorrer somente as chaves.
- Usar `values()` para percorrer somente os valores.
- Usar `items()` para percorrer chave e valor simultaneamente.
- Aplicar desempacotamento com `items()`:

```python
for key, value in user.items():
    print(key, value)
```

### Conceito importante

Os principais métodos podem ser lembrados pela finalidade:

| Método | Finalidade |
|---|---|
| `update()` | Atualizar/adicionar dados |
| `setdefault()` | Adicionar somente se a chave não existir |
| `copy()` | Criar uma cópia |
| `fromkeys()` | Criar dicionário a partir de chaves |
| `get()` | Acessar com segurança |
| `pop()` | Remover uma chave e retornar seu valor |
| `popitem()` | Remover e retornar o último par |
| `clear()` | Esvaziar o dicionário |
| `keys()` | Obter chaves |
| `values()` | Obter valores |
| `items()` | Obter pares chave/valor |

---

## Competências consolidadas no módulo

Ao finalizar o módulo, consigo:

- Modelar informações usando dicionários.
- Acessar e modificar dados por meio de chaves.
- Tratar chaves inexistentes com `get()`.
- Adicionar e atualizar informações de diferentes maneiras.
- Remover dados e aproveitar o valor retornado pelos métodos.
- Criar cópias de dicionários.
- Percorrer chaves, valores e pares chave/valor.
- Usar desempacotamento ao trabalhar com `items()`.
- Escolher métodos de `dict` de acordo com o problema.

## Próximo passo

Avançar para a próxima aula do curso, mantendo o foco em **entendimento, raciocínio e aplicação prática**, sem retornar a conteúdos já dominados.
