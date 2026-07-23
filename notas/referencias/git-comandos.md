# Git - Guia de Consulta Rápida

Este documento reúne os principais comandos do Git utilizados durante os estudos.

---

# Conceitos importantes

## Repositório (Repository)

Projeto controlado pelo Git.

Pode existir:

- Local (no computador)
- Remoto (GitHub)

---

## Commit

É um "checkpoint" do projeto.

Cada commit registra um conjunto de alterações.

---

## Branch

É uma linha de desenvolvimento.

A principal normalmente chama-se:

```
main
```

---

## Origin

É o nome padrão do repositório remoto.

Exemplo:

```
origin
```

---

# Fluxo básico do Git

```
Arquivos

↓

git add

↓

Staging Area

↓

git commit

↓

Repositório Local

↓

git push

↓

GitHub
```

---

# Inicializar um repositório

```bash
git init
```

Cria um repositório Git na pasta atual.

---

# Verificar o status

```bash
git status
```

Mostra:

- arquivos modificados;
- arquivos novos;
- arquivos preparados;
- branch atual.

É um dos comandos mais utilizados.

---

# Adicionar arquivos

Adicionar um arquivo:

```bash
git add arquivo.py
```

Adicionar tudo:

```bash
git add .
```

---

# Criar um commit

```bash
git commit -m "mensagem"
```

Exemplo:

```bash
git commit -m "Adiciona aula sobre operadores lógicos"
```

A mensagem deve explicar claramente a alteração.

---

# Enviar para o GitHub

```bash
git push
```

Envia os commits locais para o repositório remoto.

---

# Baixar alterações

```bash
git pull
```

Atualiza o projeto local com as alterações do GitHub.

---

# Clonar um projeto

```bash
git clone URL_DO_REPOSITORIO
```

Exemplo:

```bash
git clone https://github.com/usuario/projeto.git
```

---

# Ver histórico

```bash
git log
```

Histórico completo.

Versão resumida:

```bash
git log --oneline
```

---

# Ver o repositório remoto

```bash
git remote -v
```

Mostra o endereço do GitHub.

---

# Adicionar repositório remoto

```bash
git remote add origin URL
```

Exemplo:

```bash
git remote add origin https://github.com/meynkadev/python-profissional.git
```

---

# Alterar URL do repositório remoto

```bash
git remote set-url origin NOVA_URL
```

---

# Ver branch atual

```bash
git branch
```

---

# Criar uma branch

```bash
git branch nome-da-branch
```

---

# Trocar de branch

```bash
git checkout nome-da-branch
```

ou (mais moderno)

```bash
git switch nome-da-branch
```

---

# Criar e trocar de branch

```bash
git checkout -b nova-branch
```

ou

```bash
git switch -c nova-branch
```

---

# Fazer merge

```bash
git merge nome-da-branch
```

Une uma branch à branch atual.

---

# Remover uma branch

```bash
git branch -d nome-da-branch
```

---

# Restaurar alterações

Descartar alterações em um arquivo:

```bash
git restore arquivo.py
```

Descartar tudo:

```bash
git restore .
```

---

# Tirar um arquivo da Staging Area

```bash
git restore --staged arquivo.py
```

---

# Remover um repositório Git

```bash
rm -rf .git
```

No Windows (PowerShell):

```powershell
Remove-Item -Recurse -Force .git
```

Remove apenas o controle de versão.

Os arquivos do projeto permanecem.

---

# Arquivo .gitignore

Serve para informar ao Git quais arquivos ou pastas NÃO devem ser versionados.

Exemplo:

```
.venv/
__pycache__/
.vscode/
*.pyc
```

---

# Sequência mais utilizada no dia a dia

```bash
git status

git add .

git commit -m "Descrição"

git push
```

---

# Fluxo para baixar alterações

```bash
git pull
```

---

# Fluxo para iniciar um projeto

```bash
git init

git remote add origin URL

git add .

git commit -m "Primeiro commit"

git push -u origin main
```

---

# Convenções de mensagens de commit

## feat

Nova funcionalidade.

```
feat: adiciona sistema de login
```

---

## fix

Correção.

```
fix: corrige cálculo de média
```

---

## docs

Documentação.

```
docs: atualiza README
```

---

## refactor

Melhoria interna do código.

```
refactor: reorganiza estrutura do projeto
```

---

## chore

Manutenção.

```
chore: organiza estrutura das pastas
```

---

# Resumo

Fluxo mais comum:

```
git status

git add .

git commit -m "Mensagem"

git push
```

Fluxo para atualizar:

```
git pull
```

Consultar histórico:

```
git log --oneline
```

Consultar status:

```
git status
```