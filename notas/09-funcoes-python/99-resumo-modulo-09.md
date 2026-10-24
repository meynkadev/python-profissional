📘 Resumo — Módulo 9: Funções
🎯 Objetivo
Aprender a criar e utilizar funções para organizar, reutilizar e estruturar o código Python, entendendo parâmetros, argumentos, retornos, escopo e recursos que tornam as funções mais flexíveis.
---
📚 Aulas
Aula 1 — Fundamentos de Funções
Aprendi:
criação de funções com `def`;
chamada de funções;
parâmetros e argumentos;
múltiplos parâmetros;
diferença entre `print()` e `return`;
armazenamento do valor retornado em uma variável;
retorno de strings;
`return` encerrando imediatamente a execução da função;
rastreamento do fluxo de execução em funções com condicionais.
💡 Conceito importante
`return` não apenas exibe um valor: ele devolve um resultado para quem chamou a função e encerra sua execução naquele ponto.
---
Aula 2 — Argumentos, Flexibilidade e Escopo
Aprendi:
argumentos nomeados;
`*args` para quantidade variável de argumentos posicionais;
`**kwargs` para quantidade variável de argumentos nomeados;
diferença entre `*args` (tupla) e `**kwargs` (dicionário);
parâmetros somente posicionais com `/`;
parâmetros somente nomeados com `*`;
funções como objetos de primeira classe;
armazenamento de funções em variáveis;
passagem de funções como argumentos;
escopo local;
escopo global;
aplicação desses conceitos na organização de código.
💡 Conceito importante
Em Python, funções também são objetos: podem ser armazenadas, passadas como argumentos e utilizadas para criar código mais flexível e reutilizável.
---
🧠 Visão Geral do Módulo
```text
                         FUNÇÕES
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
       CRIAÇÃO           RETORNO          ARGUMENTOS
          │                 │                 │
        def()           return          ┌─────┴─────┐
                                        │           │
                                   Posicionais   Nomeados
                                        │           │
                                      *args      **kwargs

                            │
                            ▼
                  PARÂMETROS ESPECIAIS
                            │
                       ┌────┴────┐
                       │         │
                       /         *
                       │         │
                Só posição   Só nome

                            │
                            ▼
                 FUNÇÕES COMO OBJETOS
                            │
                            ▼
                   Função como valor
                            │
                            ▼
                  Função como argumento

                            │
                            ▼
                         ESCOPO
                       ┌────┴────┐
                       │         │
                     Local     Global
```
---
💡 Principal aprendizado do módulo
> **Funções permitem dividir um programa em partes menores e reutilizáveis.** Além de executar tarefas, elas podem receber dados, processá-los, retornar resultados e até ser utilizadas como valores dentro de outras funções.
---
🔑 Conceitos para lembrar
Conceito	Ideia principal
`def`	Define uma função
`()`	Chama/executa uma função
Parâmetro	Variável definida na função
Argumento	Valor enviado para a função
`return`	Devolve um valor e encerra a função
Argumento nomeado	Informa explicitamente o parâmetro
`*args`	Recebe vários argumentos posicionais
`**kwargs`	Recebe vários argumentos nomeados
`/`	Define parâmetros somente posicionais
`*`	Define parâmetros somente nomeados
Primeira classe	Funções podem ser tratadas como valores
Escopo local	Contexto interno da função
Escopo global	Contexto externo/global
---
🎯 O que devo conseguir fazer depois deste módulo?
Ao finalizar o módulo, devo ser capaz de:
criar funções com responsabilidades específicas;
definir parâmetros;
passar argumentos posicionais e nomeados;
utilizar `return` corretamente;
rastrear o fluxo de execução de uma função;
trabalhar com `*args` e `**kwargs`;
controlar a forma de passagem de parâmetros;
compreender funções como objetos de primeira classe;
passar funções para outras funções;
distinguir escopo local e global;
começar a organizar programas maiores utilizando funções.
---
🚀 Princípio profissional
```text
Código organizado
       ↓
Funções com responsabilidades claras
       ↓
Reutilização
       ↓
Menos repetição
       ↓
Mais facilidade para testar e manter
```
> 🧠 **Entendimento > memorização**
>
> **Raciocínio > copiar código**
>
> **Prática > teoria isolada**
>
> **Aplicação > decorar sintaxe**