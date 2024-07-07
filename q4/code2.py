import os

print('Seja bem vindo, Calvin!')

listaLivros = []
idGlobal = 0

# FUNÇÕES DE GERENCIMAENTO DOS LIVROS


def cadastrarLivro(novoId):
    print(f'\nId: {novoId}')
    nomeLivro = input('Qual o nome do livro?: ')
    autorLivro = input('Qual o nome do autor do livro?: ')
    editoraLivro = input('Qual o nome da editora do livro?: ')

    dadosLivro = {
        "id": novoId,
        "nome": nomeLivro,
        "autor": autorLivro,
        "editora": editoraLivro
    }

    listaLivros.append(dadosLivro)

    print('\nLivro cadastrado com sucesso!\n\n')


def consultarLivros():

    while True:
        print('''
-----------------
MENU DE CONSULTAS
-----------------

1 - Consultar todos
2 - Consultar por id
3 - Consultar por autor
4 - Retornar ao menu principal
          ''')
        try:
            acaoUsuario = int(input('Qual ação você deseja? (1, 2, 3 ou 4): '))
            if acaoUsuario in [1, 2, 3, 4]:
                if acaoUsuario == 1:
                    limparConsole()
                    listagemLivros = '''
------------------
LISTAGEM DE LIVROS
------------------
'''                 
                    if len(listaLivros) > 0:
                        for livro in listaLivros:
                            listagemLivros += f'''
-----------
Id: {livro["id"]}
Nome: {livro["nome"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
-----------    
'''
                    else:
                        listagemLivros += '\nNenhum livro encontrado\n'         
                    print(listagemLivros)
                    continue
                # elif acaoUsuario == 2:
                # elif acaoUsuario == 3:
                # else:
        except ValueError:
            print('Por favor, informe um valor numérico válido')


# FUNÇÕES UTILITÁRIAS

def limparConsole():
    if os.name == 'nt':  # WINDOWS
        os.system('cls')
    else:  # LINUX
        os.system('clear')


while True:
    print('''
--------------
MENU PRINCIPAL
--------------

1 - Cadastrar livro
2 - Consultar livro
3 - Remover livro
4 - Encerrar programa
          ''')

    try:
        while True:
            acaoUsuario = int(input('Qual ação você deseja? (1, 2, 3 ou 4): '))
            if acaoUsuario in [1, 2, 3, 4]:
                if acaoUsuario == 1:
                    idGlobal = len(listaLivros) + 1
                    cadastrarLivro(idGlobal)
                    break
                elif acaoUsuario == 2:
                    limparConsole()
                    consultarLivros()
                    break
                # elif acaoUsuario == 3:
                # else:

    except ValueError:
        print('Por favor, informe um valor numérico válido')
