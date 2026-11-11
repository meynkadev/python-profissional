# Python — Módulo 10
## Programação Orientada a Objetos: Classes, Objetos, Atributos e Métodos

**Objetivo:** compreender os fundamentos da POO e aprender a organizar dados e comportamentos em classes e objetos.

---

## 1. O que é Programação Orientada a Objetos?

A Programação Orientada a Objetos (POO) é um paradigma que organiza o código em torno de objetos. Um objeto reúne:
- **Dados**, que descrevem suas características.
- **Comportamentos**, que representam as ações que pode executar.

Em um sistema de loja, por exemplo, um produto pode ter nome, preço e estoque, além de comportamentos como exibir informações e atualizar o estoque.

## 2. O que é uma classe?

Uma **classe** é um modelo que define a estrutura e os comportamentos que seus objetos poderão ter.

```python
class Produto:
    pass
```

- `class` declara uma classe.
- `Produto` é o nome da classe.
- `pass` indica que ainda não há instruções no corpo da classe.

Por convenção, nomes de classes utilizam `PascalCase`: `Produto`, `ContaBancaria`, `CadastroCliente`.

## 3. O que é um objeto?

Um **objeto** é uma instância de uma classe.

```python
class Produto:
    pass

produto1 = Produto()
produto2 = Produto()
```

`Produto` é a classe. `produto1` e `produto2` são referências a instâncias distintas dessa classe.

A classe é o modelo; cada objeto é uma instância concreta criada a partir dele.

## 4. O que são atributos?

Atributos são informações associadas a um objeto.

```python
class Produto:
    pass

produto1 = Produto()
produto1.nome = "Teclado"
produto1.preco = 150
produto1.estoque = 10

print(produto1.nome)
print(produto1.preco)
print(produto1.estoque)
```

Nesse exemplo, `nome`, `preco` e `estoque` são atributos de `produto1`.

Cada objeto pode guardar valores próprios:

```python
produto2 = Produto()
produto2.nome = "Mouse"

print(produto1.nome)  # Teclado
print(produto2.nome)  # Mouse
```

Embora sejam da mesma classe, os objetos são instâncias distintas e possuem seus próprios valores.

## 5. O que são métodos?

Métodos são funções definidas dentro de uma classe. Representam comportamentos que os objetos podem executar.

```python
class Produto:
    def exibir_informacoes(self):
        print("Exibindo informações do produto.")

produto1 = Produto()
produto1.exibir_informacoes()
```

| Elemento | Representa | Exemplo |
|---|---|---|
| Atributo | Informação do objeto | `produto.nome` |
| Método | Ação ou comportamento | `produto.exibir_informacoes()` |

**Para lembrar:** atributos descrevem o objeto; métodos definem o que ele pode fazer.

## 6. Entendendo o `self`

`self` é o parâmetro que representa a própria instância que está executando o método. Ele permite acessar os atributos e outros métodos daquele objeto.

```python
class Produto:
    def exibir_nome(self):
        print(self.nome)

produto1 = Produto()
produto1.nome = "Teclado"
produto1.exibir_nome()
```

`self.nome` significa: acesse o atributo `nome` da instância atual.

O mesmo método funciona com objetos diferentes:

```python
produto1 = Produto()
produto1.nome = "Teclado"

produto2 = Produto()
produto2.nome = "Mouse"

produto1.exibir_nome()  # Teclado
produto2.exibir_nome()  # Mouse
```

Quando chamamos `produto1.exibir_nome()`, o Python passa a instância `produto1` como primeiro argumento do método. Quando chamamos pelo `produto2`, passa `produto2`.

**Importante:** `self` não é uma palavra reservada, mas é a convenção adotada pela comunidade Python. Utilize esse nome para manter o código claro e alinhado ao padrão da linguagem.

## 7. Métodos que modificam atributos

Um método também pode alterar os dados do objeto.

```python
class Produto:
    def aumentar_estoque(self, quantidade):
        self.estoque += quantidade

produto1 = Produto()
produto1.estoque = 10

produto1.aumentar_estoque(5)
print(produto1.estoque)  # 15
```

O método recebe uma quantidade e atualiza o atributo `estoque` da instância que chamou o método.

## 8. Exemplo integrado: produto de uma loja

```python
class Produto:
    def exibir_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco}")
        print(f"Estoque: {self.estoque}")

    def aumentar_estoque(self, quantidade):
        self.estoque += quantidade

produto1 = Produto()
produto1.nome = "Teclado"
produto1.preco = 150
produto1.estoque = 10

produto1.exibir_informacoes()
produto1.aumentar_estoque(5)

print("\nDepois da atualização:")
produto1.exibir_informacoes()
```

O exemplo reúne os conceitos:
- `Produto` é a classe.
- `produto1` é uma instância.
- `nome`, `preco` e `estoque` são atributos.
- `exibir_informacoes()` e `aumentar_estoque()` são métodos.
- `self` permite que os métodos acessem os dados do objeto que os chamou.

## 9. Como os conceitos se relacionam?

| Conceito | Significado |
|---|---|
| Classe | Modelo que define estrutura e comportamentos |
| Objeto | Instância criada a partir de uma classe |
| Atributo | Informação armazenada no objeto |
| Método | Função definida na classe que representa um comportamento |
| `self` | Referência à instância que está utilizando o método |

### Uma comparação para memorizar

Imagine uma classe como a planta de construção de um instrumento musical:
- A **classe** descreve o modelo.
- Cada **objeto** é um instrumento concreto construído a partir dele.
- Os **atributos** descrevem características, como modelo e afinação.
- Os **métodos** representam ações que podem ser realizadas com ele.
- O **`self`** permite que cada ação trabalhe com o instrumento específico que está sendo utilizado.

## 10. Boas práticas iniciais

1. Dê nomes claros e significativos às classes, atributos e métodos.
2. Utilize `PascalCase` para classes, como `ContaBancaria`.
3. Utilize `snake_case` para atributos e métodos, como `saldo_atual` e `depositar`.
4. Mantenha juntos os dados e comportamentos que pertencem ao mesmo conceito.
5. Evite criar classes sem uma responsabilidade clara.
6. Prefira inicializar atributos de maneira organizada com `__init__()`, em vez de espalhar atribuições pelo programa.

## 11. Resumo para consulta

- **POO:** paradigma que organiza o programa em objetos que reúnem dados e comportamentos.
- **Classe:** modelo que define a estrutura e os comportamentos dos objetos.
- **Objeto:** instância concreta de uma classe.
- **Atributo:** informação pertencente a um objeto.
- **Método:** função definida dentro de uma classe.
- **`self`:** referência à instância que está executando o método.

**Ideia principal:** uma classe organiza os dados e as ações relacionadas a determinado conceito. Cada objeto criado a partir dela possui sua própria identidade e seus próprios valores.

## 12. Prática recomendada

Crie classes que representem situações simples:

1. **Aluno:** atributos `nome` e `nota`; método para exibir as informações.
2. **ContaBancaria:** atributos `titular` e `saldo`; métodos para depositar e consultar o saldo.
3. **Produto:** atributos `nome`, `preco` e `estoque`; métodos para exibir informações e aumentar o estoque.

Ao praticar, identifique em cada exemplo:
- Qual é a classe?
- Quais objetos foram criados?
- Quais são os atributos?
- Quais são os métodos?
- O que `self` representa em cada chamada?
