# Documentação — Sistema Sinta Música

## 1. Visão geral

O **Sistema Sinta Música** é um projeto desenvolvido em Python para simular um sistema simples de gerenciamento de alunos de uma escola de música.

O projeto foi desenvolvido como uma aplicação prática dos conhecimentos adquiridos nos quatro primeiros módulos da formação em Python.

A aplicação funciona por meio do terminal e possui um menu interativo que permite ao usuário cadastrar, listar e buscar alunos.

---

## 2. Objetivo

O principal objetivo do projeto é transformar os conhecimentos estudados em uma aplicação prática.

Durante o desenvolvimento foram aplicados conceitos fundamentais de Python, além de lógica de programação, construção de algoritmos, organização do código e resolução de problemas.

O projeto também representa um marco na evolução dos estudos, pois reúne em uma única aplicação diversos conceitos que foram aprendidos separadamente durante o curso.

---

## 3. Escopo da versão 1.0

### Funcionalidades implementadas

* Cadastro de alunos
* Listagem de alunos cadastrados
* Busca de alunos por nome
* Numeração dos alunos na listagem
* Exibição das informações do sistema
* Menu interativo
* Encerramento do programa

### Funcionalidades fora do escopo atual

A versão 1.0 não possui:

* Banco de dados
* Persistência de dados em arquivos
* Sistema de login
* Edição de alunos
* Exclusão de alunos
* Interface gráfica

Essas limitações são intencionais, pois o projeto foi desenvolvido de acordo com os conhecimentos disponíveis até o módulo 4 da formação.

---

## 4. Funcionamento do sistema

O sistema possui um menu principal que permanece em execução enquanto o usuário não escolher a opção de encerramento.

### Fluxo principal

```text
Início
  ↓
Menu principal
  ↓
Usuário escolhe uma opção
  ↓
Executa a funcionalidade
  ↓
Retorna ao menu
  ↓
Usuário escolhe novamente
  ↓
Opção 0
  ↓
Encerramento
```

A estrutura de repetição `while` é responsável por manter o menu funcionando continuamente.

As estruturas condicionais `if` e `elif` determinam qual funcionalidade será executada de acordo com a opção escolhida.

---

## 5. Funcionalidades

### 5.1 Cadastro de aluno

A opção de cadastro solicita informações básicas do aluno:

* Nome
* Instrumento
* Idade

As informações são organizadas em uma string utilizando **f-string** e adicionadas à lista de alunos com o método `.append()`.

Exemplo:

```text
Nome | Instrumento | Idade
```

---

### 5.2 Listagem de alunos

A opção de listagem percorre todos os alunos cadastrados utilizando a estrutura de repetição `for`.

Cada aluno é apresentado com uma numeração sequencial.

Exemplo:

```text
1 - João | Teclado | 25 anos
2 - Maria | Piano | 16 anos
3 - Pedro | Violão | 12 anos
```

A numeração é controlada por uma variável contador, que é incrementada a cada repetição.

---

### 5.3 Busca de aluno

A busca solicita ao usuário o nome do aluno que deseja encontrar.

O programa percorre a lista e verifica se o nome informado está presente nos dados de cada aluno.

A comparação utiliza `.lower()` para evitar que diferenças entre letras maiúsculas e minúsculas impeçam a localização do aluno.

Uma variável booleana chamada `encontrou` é utilizada como controle da busca.

Ela começa como `False` e passa para `True` quando um aluno correspondente é encontrado.

Ao final da busca, caso nenhum aluno tenha sido encontrado, o sistema apresenta uma mensagem informando o usuário.

---

### 5.4 Sobre

A opção **Sobre** apresenta informações básicas do projeto, como nome, versão e autor.

---

### 5.5 Encerramento

A opção `0` encerra o programa.

A instrução `break` interrompe o laço principal e permite que a execução do programa seja finalizada.

---

## 6. Estrutura dos dados

Nesta versão, os alunos são armazenados em uma lista Python.

Os dados permanecem apenas na memória durante a execução do programa.

Cada aluno é representado por uma string contendo suas principais informações.

Exemplo:

```python
alunos = [
    "João | Teclado | 25 anos",
    "Maria | Piano | 16 anos"
]
```

Essa estrutura foi escolhida por ser adequada aos conhecimentos disponíveis durante o desenvolvimento da versão 1.0.

---

## 7. Tecnologias e conceitos utilizados

### Tecnologias

* Python 3
* Visual Studio Code
* Git
* GitHub
* Terminal

### Conceitos de Python

* Variáveis
* Tipos de dados
* Entrada e saída de dados
* Strings
* F-strings
* Operadores de comparação
* Operadores de associação
* Estruturas condicionais
* Estruturas de repetição
* Listas
* Método `.append()`
* Métodos `.strip()` e `.lower()`
* Variáveis booleanas
* Contadores
* Indentação e blocos de código

---

## 8. Como executar

Com o Python instalado, abra o terminal na pasta do projeto e execute:

```bash
python sistema_sintamusica.py
```

Em ambientes nos quais o comando `python` não estiver configurado, pode ser necessário utilizar:

```bash
python3 sistema_sintamusica.py
```

Após a execução, o menu principal será apresentado no terminal.

---

## 9. Armazenamento dos dados

A versão 1.0 utiliza armazenamento exclusivamente em memória.

Isso significa que os alunos cadastrados permanecem disponíveis enquanto o programa está em execução.

Ao encerrar o programa, os dados são perdidos.

Essa é uma limitação conhecida da versão atual e está relacionada ao estágio da formação em Python em que o projeto foi desenvolvido.

---

## 10. Organização do projeto

Estrutura atual:

```text
sintamusica/
├── imagens/
├── DOCUMENTACAO.md
├── README.md
└── sistema_sintamusica.py
```

O arquivo Python contém a implementação do sistema.

O `README.md` apresenta o projeto de forma resumida.

O `DOCUMENTACAO.md` apresenta informações técnicas e detalhadas sobre seu funcionamento.

---

## 11. Aprendizados

O desenvolvimento do Sistema Sinta Música permitiu aplicar, em um único projeto, conhecimentos que foram estudados inicialmente de forma isolada.

Entre os principais aprendizados estão:

* Transformar um problema em etapas de programação;
* Planejar o fluxo de uma aplicação;
* Utilizar estruturas condicionais para tomada de decisões;
* Utilizar estruturas de repetição para automatizar tarefas;
* Percorrer e manipular listas;
* Pesquisar informações dentro de uma coleção de dados;
* Utilizar variáveis de controle para representar estados da aplicação;
* Organizar o código de forma legível;
* Utilizar comentários para documentar a lógica;
* Desenvolver uma aplicação incrementalmente;
* Praticar versionamento com Git e GitHub.

O projeto também ajudou a consolidar a diferença entre aprender uma sintaxe e utilizar essa sintaxe para resolver um problema real.

---

## 12. Limitações atuais

A versão atual é propositalmente simples.

Os principais pontos que podem ser melhorados futuramente são:

* Persistência dos dados;
* Estruturas de dados mais adequadas;
* Separação do código em funções;
* Validação mais completa das entradas;
* Edição de informações;
* Banco de dados;
* Interface gráfica.

Essas melhorias poderão ser consideradas conforme novos conceitos forem estudados na formação.

---

## 13. Evolução futura

O projeto poderá evoluir gradualmente junto com os estudos de Python.

A ideia não é adicionar funcionalidades apenas para aumentar o tamanho do código, mas utilizar novos conhecimentos para melhorar a arquitetura, a organização e a qualidade do sistema.

Dessa forma, o projeto poderá servir como um registro prático da evolução técnica ao longo da formação.

---

## 14. Status

**Versão 1.0 — Concluída**

Projeto desenvolvido após a conclusão dos quatro primeiros módulos da formação em Python.

A versão atual cumpre seu objetivo principal: consolidar os fundamentos de Python por meio de uma aplicação prática e funcional.

---

## 15. Autor

**Meynkâ do Nascimento Griebel**

Projeto desenvolvido como parte dos estudos de Python.
