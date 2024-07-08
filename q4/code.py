import os

print("\nSeja bem vindo, Calvin Teixeira\n")

lista_livro = []
id_global = 0


def cadastrar_livro(id):
    nome = input("\nDigite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)
    print('\nLivro cadastrado com sucesso!\n')

def consultar_livro():
    while True:
        print("\n1. Consultar Todos \n2. Consultar por Id \n3. Consultar por Autor \n4. Retornar ao menu:\n")
        opcao = input("\nDigite a opção desejada: ")
        if opcao == '1':
            if len(lista_livro) == 0:
                print('\nNenhum livro para listar, tente outra opção')
            for livro in lista_livro:
                print(f'''
---------------------------------
ID: {livro['id']}
NOME: {livro['nome']}
AUTOR: {livro['autor']}
EDITORA: {livro['editora']}
---------------------------------
''')
        elif opcao == '2':
            id_consulta = int(input("Digite o id do livro: "))
            livro_encontrado = next(
                (livro for livro in lista_livro if livro['id'] == id_consulta), None)
            if livro_encontrado:
                print(f'''
---------------------------------
ID: {livro_encontrado['id']}
NOME: {livro_encontrado['nome']}
AUTOR: {livro_encontrado['autor']}
EDITORA: {livro_encontrado['editora']}
---------------------------------
''')
            else:
                print("Livro não encontrado.")
        elif opcao == '3':
            autor_consulta = input("Digite o autor do livro: ")
            livros_autor = [
                livro for livro in lista_livro if livro['autor'] == autor_consulta]
            for livro in livros_autor:
                print(f'''
---------------------------------
ID: {livro['id']}
NOME: {livro['nome']}
AUTOR: {livro['autor']}
EDITORA: {livro['editora']}
---------------------------------
''')
        elif opcao == '4':
            limpa_console()
            break
        else:
            limpa_console()
            print("\nOpção inválida, tente novamente\n\n")

def remover_livro():
    while True:
        id_remover = int(input("\nDigite o id do livro a ser removido: "))
        livro_encontrado = next(
            (livro for livro in lista_livro if livro['id'] == id_remover), None)
        if livro_encontrado:
            lista_livro.remove(livro_encontrado)
            limpa_console()
            print("\nLivro removido com sucesso.")
            break
        else:
            print("\nId inválido, tente novamente")

def limpa_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux, macOS)
        os.system('clear')

while True:
    print("\n1. Cadastrar Livro \n2. Consultar Livro \n3. Remover Livro \n4. Encerrar Programa:\n")
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        limpa_console()
        print("Programa encerrado.")
        exit()        
    else:
        limpa_console()
        print("\nOpção inválida, tente novamente\n\n")