import threading
import os

print("\nSeja bem vindo, Calvin Teixeira\n")

listaLivros = []
idGlobal = 0

def cadastrarLivro(novoId):
    nomeLivro = input('\nInforme o nome do livro: ')
    autorLivro = input('\nInforme o autor do livro: ')
    editoraLivro = input('\nInforme a editora do livro: ')

    dadosNovoLivro = {
        "id": novoId,
        "nome": nomeLivro,
        "autor": autorLivro,
        "editora": editoraLivro
    }

    listaLivros.append(dadosNovoLivro)

    print('\nLivro cadastrado com sucesso!\n')

    while True:
        try:
            acaoUsuario = int(input('''
------------------------------
Escolha como deseja continuar
------------------------------

1 - Cadastrar novo livro
2 - Retornar ao menu principal
'''))

            if acaoUsuario in [1, 2]:
                if acaoUsuario == 1:
                    novoId = listaLivrosAutoIncrementId()
                    cadastrarLivro(novoId)
                    break
                elif acaoUsuario == 2:
                    limparConsole()                    
                    break
            else:
                print('\nPor favor, escolha uma opção disponível\n')
        except ValueError:
            print('Por favor, informe um valor númerico válido para a opção')

    if acaoUsuario == 1:
        cadastrarLivro(listaLivrosAutoIncrementId)



def menuConsultas():
    while True:
        try:
            print('''
    \n
---------------------------------
Que tipo de consulta você deseja?
---------------------------------

Escolha a opção que desejar
1 - Consultar todos
2 - Consultar por Id
3 - Constultar por autor
4 - Retornar ao menu
    \n
    ''')
            acaoUsuario = int(
                input('\nQual opção você deseja? (1, 2, 3 ou 4)\n'))

            if acaoUsuario in [1, 2, 3, 4]:
                if acaoUsuario == 1:
                    print(getAllLivros())
                elif acaoUsuario == 2:
                    idInformado = input('\nInforme o id que deseja buscar\n')
                    print(getLivroById(idInformado))
                elif acaoUsuario == 3:
                    autorInformado = input(
                        '\nInforme o nome do autor que deseja buscar\n')
                    print(getLivroByAutor(autorInformado))
                elif acaoUsuario == 4:
                    limparConsole()
                    initMenu()
            else:
                print('\nPor favor, escolha uma opção disponível\n')
        except ValueError:
            print('Por favor, informe um valor númerico válido para a opção')


def getAllLivros():
    textoLivros = '''
---------------------------
Lista de livros cadastrados
---------------------------
    '''

    for livro in listaLivros:
        textoLivros += f'''
-----------
Id: {livro["id"]}
Nome: {livro["nome"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
-----------
'''
    return textoLivros


def getLivroById(idInformado):
    livro = next(
        (livro for livro in listaLivros if livro["id"] == idInformado), None)

    if livro:
        return f'''
-----------
Id: {livro["id"]}
Nome: {livro["nome"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
-----------
'''
    else:
        return '\nNenhum livro encontrado\n'


def getLivroByAutor(autorInformado):
    nomeAutor = autorInformado.lower()
    livrosEncontrados = [
        livro for livro in listaLivros if nomeAutor in livro["autor"].lower()]
    textoLivros = ''''''

    if len(livrosEncontrados) > 0:
        for livro in livrosEncontrados:
            textoLivros += f'''
-----------
Id: {livro["id"]}
Nome: {livro["nome"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
-----------
            '''
    else:
        return '\nNenhum livro encontrado\n'


def removerLivroById(idInformado):
    livro = next(
        (livro for livro in listaLivros if livro["id"] == idInformado), None)

    if livro:
        list(filter(lambda livro: livro["id"] != idInformado, listaLivros))
        return {
            "error": False,
            "message":  '\nLivro removido com sucesso\n'
        }
    else:
        return {
            "error": True,
            "message": '\nId inválido\n'
        }


def encerrarApp():
    print('Obrigado por usar nossa plataforma!')
    limparConsole()
    exit()


# Configura a função que fecha o app para ter um time out de execução, isso melhora a experiência do usuário, para que ao selecionar a opção e encerrar o sistema, isso não aconteça de forma imediata.
timer = threading.Timer(2, encerrarApp)


def limparConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def listaLivrosAutoIncrementId():
    return len(listaLivros) + 1

print('''
\n   
--------------
Menu de opções
--------------
    
1 - Cadastrar Livro
2 - Consultar Livro
3 - Remover Livro
4 - Encerrar programa
    \n
    ''')

while True:
        try:
            acaoUsuario = int(
                input('\nQual opção você deseja? (1, 2, 3 ou 4)\n'))
            if acaoUsuario in [1, 2, 3, 4]:
                if acaoUsuario == 1:
                    novoId = listaLivrosAutoIncrementId()
                    cadastrarLivro(novoId)
                    break
                elif acaoUsuario == 2:
                    menuConsultas()
                    break
                elif acaoUsuario == 3:
                    while True:
                        idInformado = int(
                            input('\nInforme o id do livro que deseja remover\n'))
                        result = removerLivroById(idInformado)
                        if result["error"]:
                            print(result["message"])
                            print('''
\n   
--------------
Menu de opções
--------------
    
1 - Remover outro livro
2 - Retornar ao menu principal
\n
    ''')
                            while True:
                                try:
                                    acaoUsuario = int(
                                        input('\nQual opção você deseja? (1, 2)\n'))
                                    if acaoUsuario in [1, 2]:
                                        if acaoUsuario == 1:
                                            break
                                        else:
                                            limparConsole()
                                            initMenu()
                                            break
                                    else:
                                        print('\nOpção inválida\n')
                                except ValueError:
                                    print(
                                        'Por favor, informe um valor númerico válido para a opção')
                        else:
                            print(result["message"])
                            print('''
\n   
--------------
Menu de opções
--------------
    
1 - Remover outro livro
2 - Retornar ao menu principal
\n
    ''')
                            while True:
                                try:
                                    acaoUsuario = int(
                                        input('\nQual opção você deseja? (1, 2)\n'))
                                    if acaoUsuario in [1, 2]:
                                        if acaoUsuario == 1:
                                            break
                                        else:
                                            limparConsole()
                                            initMenu()
                                            break
                                    else:
                                        print('\nOpção inválida\n')
                                except ValueError:
                                    print(
                                        'Por favor, informe um valor númerico válido para a opção')
                            break
                elif acaoUsuario == 4:
                    print('Encerrando aplicação...')
                    timer.start()
                    timer.join()
                    encerrarApp()
            else:
                print('\nPor favor, escolha uma opção disponível\n')
        except ValueError:
            print('Por favor, informe um valor númerico válido para a opção')