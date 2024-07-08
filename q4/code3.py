print("\nSeja bem vindo, Calvin Teixeira\n")

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    nome = input("\nDigite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

def consultar_livro():
    while True:
        opcao = input("Escolha uma opção: 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu: ")
        if opcao == '1':
            for livro in lista_livro:
                print(livro)
        elif opcao == '2':
            id_consulta = int(input("Digite o id do livro: "))
            livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_consulta), None)
            if livro_encontrado:
                print(livro_encontrado)
            else:
                print("Livro não encontrado.")
        elif opcao == '3':
            autor_consulta = input("Digite o autor do livro: ")
            livros_autor = [livro for livro in lista_livro if livro['autor'] == autor_consulta]
            for livro in livros_autor:
                print(livro)
        elif opcao == '4':
            break
        else:
            print("Opção inválida")

def remover_livro():
    while True:
        id_remover = int(input("Digite o id do livro a ser removido: "))
        livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_remover), None)
        if livro_encontrado:
            lista_livro.remove(livro_encontrado)
            print("Livro removido com sucesso.")
            break
        else:
            print("Id inválido")

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
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida\n\n")

id_global += 1
cadastrar_livro(id_global)
id_global += 1
cadastrar_livro(id_global)
id_global += 1
cadastrar_livro(id_global)

print("\nConsulta de todos os livros:")
consultar_livro()

print("\nConsulta de um livro por ID:")
consultar_livro()

print("\nConsulta de livros por autor:")
consultar_livro()

print("\nRemoção de um livro e consulta de todos os livros:")
remover_livro()
consultar_livro()