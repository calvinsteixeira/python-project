print("Seja bem vindo, Calvin Teixeira\n")

lanches = [{ "sigla": "CP", "descricao": "Cupuaçu", "tamanhos": [{ "sigla": "P", "valor": 9 }, { "sigla": "M", "valor": 14 }, { "sigla": "G", "valor": 18 }]}, { "sigla": "AC", "descricao": "Açaí", "tamanhos": [{ "sigla": "P", "valor": 11 }, { "sigla": "M", "valor": 16 }, { "sigla": "G", "valor": 20 }]}]

totalPedido = 0

def geraTextoCardapio():
    cardapio = ''
    for lanche in lanches:
        cardapio += f'''
{lanche["sigla"]} - {lanche["descricao"]}
Tamanhos: {", ".join([f'{t["sigla"]} (R$ {t["valor"]})' for t in lanche["tamanhos"]])}
        '''
    
    return cardapio
def checkSaborEscolhido(sabor):
    valido = any(lanche["sigla"] == sabor for lanche in lanches)
    return valido
def checkTamanhoEscolhido(sabor, tamanho):
    for lanche in lanches:
        if lanche['sigla'] == sabor:
            return any(t['sigla'] == tamanho for t in lanche["tamanhos"])
    return False
def getLanche(siglaSaborEscolhido, siglaTamanhoEscolhido):
    for lanche in lanches:
        if lanche["sigla"] == siglaSaborEscolhido:
            for tamanho in lanche["tamanhos"]:
                if tamanho["sigla"] == siglaTamanhoEscolhido:
                    return lanche["descricao"], tamanho["sigla"], tamanho["valor"] 

print('Segue abaixo a lista dos nossos sabores e tamanhos disponíveis\n') 
print(geraTextoCardapio())

while True:
    saborEscolhido = input('Digite a sigla referente ao sabor que você deseja\n')
    if not checkSaborEscolhido(saborEscolhido):
        print('\nSabor inválido. Tente novamente\n')
        continue
    else:
        while True:
            tamanhoEscolhido = input('Digite a sigla referente ao tamanho que você deseja\n')
            if not checkTamanhoEscolhido(saborEscolhido, tamanhoEscolhido):
                print('\nTamanho inválido. Tente novamente\n')                  
            else:
                descricaoLancheEscolhido, tamanho, valor = getLanche(saborEscolhido, tamanhoEscolhido)
                print(f'Você pediu um {descricaoLancheEscolhido} no tamanho {tamanho}: R$ {valor:.2f}\n')
                totalPedido += valor
                break    
    
    while True:
        acao = input('\nDeseja continuar comprando? (S/N)\n')         
        if acao != 'S' and acao != 'N':
            print('\nOpção inválida, você deseja continuar comprando? (S/N)?\n')     
            continue
        else:
            break       
        
    if acao == 'N':        
        print(f'\nO valor total do seu pedido é de R$ {totalPedido:.2f}. Obrigado por usar nosso serviço!\n')
        break
                 
    
    
    
