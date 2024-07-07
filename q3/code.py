print("\nSeja bem vindo, Calvin Teixeira\n")

servicos = [{ "identificador": "DIG", "descricao": "Digitalização ", "valor": 1.10  }, { "identificador": "ICO", "descricao": "Impressão Colorida ", "valor": 1 }, { "identificador": "IPB", "descricao": "Impressão Preto e Branco", "valor": 0.40 }, { "identificador": "FOT", "descricao": "Fotocópia ", "valor": 0.20 }]

servicosExtras = [{ "identificador": 1, "descricao": "Encadernação simples", "valor": 15  }, { "identificador": 2, "descricao": "Encadernação de capa dura ", "valor": 40 }, { "identificador": 0, "descricao": "Nenhum serviço extra", "valor": 0 }]

def geraTextoServicos():
    textoServicos = '''
    ---------------------------------
    Conheça a nossa lista de serviços
    ---------------------------------
    \n'''
    for servico in servicos:
        textoServicos += f'''
{servico["identificador"]} - {servico["descricao"]}  
Valor: R$ {servico["valor"]:.2f}/página
-------------------------------------------
        '''
        
    return textoServicos

def geraTextoServicosExtras():
    textoServicosExtras = '''\n\n
    ---------------
    Serviços extras
    ---------------
    \n'''
    for servicoExtra in servicosExtras:
        textoServicosExtras += f'''
{servicoExtra["identificador"]} - {servicoExtra["descricao"]}  
Valor: R$ {servicoExtra["valor"]:.2f}/página
-------------------------------------------
        '''
        
    return textoServicosExtras

def checkServicoEscolhido(identificadorServicoEscolhido):
    valido = any(servico["identificador"] == identificadorServicoEscolhido for servico in servicos)
    return valido

def checkServicoExtraEscolhido(identificadorServicoExtraEscolhido):
    valido = any(servicoExtra["identificador"] == identificadorServicoExtraEscolhido for servicoExtra in servicosExtras)
    return valido
    
def calculaDesconto(numPaginas, identificadorServicoEscolhido):
    valorServicoEscolhido = next((servico["valor"] for servico in servicos if servico["identificador"] == identificadorServicoEscolhido), None)
    paginasComDesconto = 0
    
    if numPaginas < 20:
        paginasComDesconto = numPaginas * (1 - 0)
    elif numPaginas >= 20 and numPaginas < 200:
        paginasComDesconto = numPaginas * (1 - 0.15)
    elif numPaginas >= 200 and numPaginas < 2000:
        paginasComDesconto = numPaginas * (1 - 0.2)
    elif numPaginas >= 2000 and numPaginas < 20000:
        paginasComDesconto = numPaginas * (1 - 0.25)
    else:
        return False, None
        
    return valorServicoEscolhido, paginasComDesconto

def retornaValorServicoExtra(siglaServicoExtraEscolhido):
    return next((servicoExtra["valor"] for servicoExtra in servicosExtras if servicoExtra["identificador"] == siglaServicoExtraEscolhido), None)

def escolhaServico():
    while True:
        servicoEscolhido = input('Qual serviço você deseja utilizar? (DIG, ICO, IPB, FOT)\n\n')
        if not checkServicoEscolhido(servicoEscolhido):
            print('\nServiço inválido, por favor tente novamente\n\n')
        else:            
            valorServico, paginasComDesconto = numPagina(servicoEscolhido)           
            return valorServico, paginasComDesconto                     

def servicoExtra():
    print(geraTextoServicosExtras())
    while True:
        try:
            servicoExtraEscolhido = input('\nQual serviço extra você deseja? (1/2/0)\n')
            if servicoExtraEscolhido in [1,2,0]:
                if servicoExtraEscolhido in [1,2]:
                    return retornaValorServicoExtra(servicoExtraEscolhido)            
                else:
                    break        
            else:
                print('A opção escolhida é inválida\n')
                continue
        except:
            print('Entrada inválida. Por favor, insira um número inteiro\n')
            continue
            
def numPagina(identificadorServicoEscolhido):
    while True:
        try:
            numPaginasEscolhidas = int(input('\nInforme um valor válido entre 1 e 20.000, por favor\n'))
            valorServico, paginasComDesconto = calculaDesconto(numPaginasEscolhidas, identificadorServicoEscolhido)
            if paginasComDesconto == numPaginasEscolhidas:
                print('\nAceitamos no máximo 20.000 páginas em uma única vez\n')
            else:                
                return valorServico, paginasComDesconto                             
        except ValueError:
            print('Entrada inválida. Por favor, insira um número inteiro\n')            

print(geraTextoServicos())
valorServico, paginasComDesconto = escolhaServico()
valorServicoExtra = servicoExtra()

total = (valorServico * paginasComDesconto) + valorServicoExtra