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

    if opcao == "4":
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

    else:
        print("\nOpção ainda não implementada.")

        input("\nPressione ENTER para voltar ao menu...")

    