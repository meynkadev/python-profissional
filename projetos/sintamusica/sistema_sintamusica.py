# ===================================
# Projeto: Sistema Sinta Música!
#
# Desenvolvedor: Meynkâ Griebeler
# 
# Objetivo:
# Sistema de gerencimaneto de alunos deenvolvido durante
# os estudos de Python.
#
# Versão: 1.0
# ===================================

# Estrutura principal responsável pelo armazenamento dos alunos cadastrados
alunos = []

# While vai permitir que sempre volte ao menu após a execução,
# premitindo que o programa continue rodando, exceção opção 0
# que contém o Break, que encerra o While
while True:

    print("=" * 42)
    print("         SISTEMA SINTA MÚSICA!")
    print("=" * 42)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sobre")
    print("0 - Sair")

# .strip() vai retirar os espaços antes e depois da string,
# garantindo que a entrada do usuário seja igual a opção indica no menu
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print()
        print("======== CADASTRO ========")
        print()
        # Criação das variáveis para armazenar dados dos alunos
        nome = input("Nome: ")
        instrumento = input("Instrumento: ")
        idade = input("Idade: ")
        aluno = f"{nome} | {instrumento} | {idade} anos" # Cria uma string contendo todas as informações do aluno
        alunos.append(aluno) # # Adiciona o novo aluno ao final da lista
        print()
        print(f"O aluno {nome} foi cadastrado!") # Exibe confirmação

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "2":
        print()
        print("======== ALUNOS CADASTRADOS ========")
        print()
        contador = 1 # criação da variável que irá enumerar a lista
        for aluno in alunos: # fr irá percorrer a lista de alunos cadastrados
            print(f"{contador} - {aluno}") #exibe a númeração do aluno atual do ciclo e as informações dele
            contador += 1 # cada ciclo a enumeração muda
        print()

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":
        print()
        print("======== BUSCA DE ALUNOS ========")
        print()
        # Solicita o nome que será pesquisado
        aluno_busca = input("Digite o nome do aluno que deseja encontrar: ").strip()
        # Começa como False e será alterada para True caso
        # algum aluno corresponda à pesquisa.   
        encontrou = False
        # Percorre toda a lista de alunos cadastrados
        for aluno in alunos:
            # Verifica se o texto digitado pelo usuário está presente
            # nos dados do aluno, sem diferenciar maiúsculas de minúsculas
            if aluno_busca.lower() in aluno.lower():
                print("O aluno(a) foi encontrado")
                print(aluno)
                # Atualiza a variável de controle para impedir que a mensagem
                # "Aluno não encontrado" seja exibida ao final da busca.
                encontrou = True

        # Se nenhum aluno foi encontrado durante o laço
        if not encontrou:
             print("aluno não encontrado!")

        print()
        input("\nPressione ENTER para voltar ao menu...")

    
    elif opcao == "4":
        print()
        print("=" * 42)
        print("Sistema Sinta Música")
        print("Versão 1.0")
        print()
        print("Desenvolvido por:")
        print("Meynkâ do Nascimento Griebeler")
        print()
        print("Projeto desenvolvido durante")
        print("a Formação Python Fundamentals.")
        print("=" * 42)

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "0":
        print("\nObrigado por utilizar o sistema.")
        print("Até logo!")
        break # Break interrompe imediatamente o While


    