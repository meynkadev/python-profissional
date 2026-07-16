# Resumo do Módulo 01 – Conhecendo Python

## Objetivo do módulo

Neste módulo foram apresentados os conceitos fundamentais da linguagem Python, incluindo tipos de dados, variáveis, conversão de tipos e entrada de dados pelo teclado. Esses conceitos formam a base para todos os programas que serão desenvolvidos nos próximos módulos.

---

# Tipos de Dados

O Python possui diversos tipos de dados. Os principais estudados foram:

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| int | Números inteiros | 10 |
| float | Números decimais | 3.14 |
| str | Texto | "Python" |
| bool | Valores lógicos | True / False |

### Funções úteis

```python
type()
dir()
help()
```

- `type()` identifica o tipo de uma variável.
- `dir()` lista os atributos e métodos disponíveis para um objeto.
- `help()` exibe a documentação de uma função, método ou objeto.

---

# Variáveis

Uma variável é um nome utilizado para armazenar uma referência a um valor na memória.

Exemplo:

```python
nome = "Meynkâ"
idade = 27
```

O valor associado a uma variável pode ser alterado durante a execução do programa.

```python
nome = "Carlos"
```

As variáveis não armazenam necessariamente uma cópia do valor, mas uma referência para um objeto.

---

# Constantes

O Python não possui constantes verdadeiras.

Por convenção, utiliza-se letras maiúsculas para indicar que um valor não deve ser alterado.

Exemplo:

```python
PI = 3.14159
IDADE_MINIMA = 18
```

Essa convenção serve apenas para orientar outros desenvolvedores.

---

# Conversão de Tipos (Casting)

A conversão de tipos permite transformar um valor de um tipo para outro.

Principais funções:

```python
int()
float()
str()
bool()
```

Exemplos:

```python
int("10")
float("10")
str(10)
bool(10)
```

### Regras importantes

| Expressão | Resultado |
|-----------|-----------|
| bool(0) | False |
| bool(0.0) | False |
| bool("") | False |
| bool(100) | True |
| bool(-5) | True |
| bool("Python") | True |
| bool("False") | True |

Uma conversão só altera a variável quando seu resultado é armazenado.

Exemplo:

```python
idade = int("25")
```

---

# Entrada de Dados

A função `input()` permite receber informações digitadas pelo usuário.

Exemplo:

```python
nome = input("Digite seu nome: ")
```

O programa interrompe sua execução até que o usuário pressione **Enter**.

### Regra mais importante

O `input()` sempre retorna uma **string**, independentemente do conteúdo digitado.

Exemplo:

```python
idade = input("Digite sua idade: ")
```

Mesmo digitando:

```
25
```

O tipo será:

```python
<class 'str'>
```

Quando necessário, deve-se converter o valor:

```python
idade = int(input("Digite sua idade: "))
```

---

# Operadores em Strings

## Concatenação

```python
"Olá " + "Mundo"
```

Resultado:

```
Olá Mundo
```

## Repetição

```python
"Python " * 3
```

Resultado:

```
Python Python Python
```

O comportamento dos operadores depende do tipo dos dados utilizados.

---

# Boas práticas aprendidas

- Utilizar nomes claros para variáveis.
- Converter dados para o tipo adequado antes de utilizá-los.
- Não confiar automaticamente nos dados digitados pelo usuário.
- Organizar os arquivos do projeto por módulos e aulas.
- Documentar o aprendizado utilizando arquivos Markdown.
- Fazer commits frequentes e bem descritos utilizando Git.

---

# Estrutura do projeto

```
python-profissional/

├── aulas/
├── notas/
├── desafios/
├── exercicios/
├── projetos/
├── README.md
```

Cada aula possui:

- Um arquivo `.py` contendo os exemplos e exercícios.
- Um arquivo `.md` contendo a documentação e as anotações.

---

# O que aprendi neste módulo

Ao concluir este módulo, sou capaz de:

- Identificar os principais tipos de dados do Python.
- Declarar e modificar variáveis.
- Entender a convenção de constantes.
- Converter valores entre diferentes tipos.
- Utilizar a função `input()` para receber dados do usuário.
- Compreender que `input()` sempre retorna uma string.
- Utilizar corretamente os operadores `+` e `*` em strings.
- Organizar meus estudos utilizando documentação em Markdown.
- Versionar meu projeto utilizando Git e GitHub.

---

# Próximo passo

No próximo módulo serão introduzidos novos conceitos que permitirão criar programas cada vez mais interativos e inteligentes. Os fundamentos aprendidos neste módulo serão utilizados continuamente durante todo o estudo da linguagem Python.