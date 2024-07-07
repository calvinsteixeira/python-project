import math

print("Seja bem vindo, Calvin Teixeira\n")

def calculaValorComDesconto(valorOriginal):
    desconto = 0 # Em caso de futuras promoções, essa variável pode servir como uma configuração de desconto base a ser cálculado junto com as regras a seguir.
    observacao = ""
 
    # A estrutura de incrementação foi adotada para que o parâmetro de configuração base de desconto (no início da função) funcione adequadamente. 
    if valorOriginal < 2500:
        desconto = desconto + 0
        observacao = "Nenhum desconto aplicado, o desconto é  apenas em compras maiores que R$ 2.500"
    elif valorOriginal >= 2500 and valorOriginal < 6000:
        desconto = desconto + 0.04
        observacao = "Desconto aplicado para compras entre R$ 2.500 e R$ 6.000"
    elif valorOriginal >= 6000 and valorOriginal < 10000:
        desconto = desconto + 0.07
        observacao = "Desconto aplicado para compras entre R$ 6.500 e R$ 10.000"
    else:
        desconto = desconto + 0.11
        observacao = "Desconto aplicado para compras acima de R$ 10.000"

    valorDesconto = valorOriginal * desconto    
    porcentagemDesconto = retornaPorcentagem(desconto)

    return {
        "valorFinalComDesconto": valorOriginal - valorDesconto,
        "valorDescontado": valorDesconto,
        "descontoEmPorcentagem": porcentagemDesconto,
        "descricaoDesconto": observacao
    }   

def retornaPorcentagem(valor):
    fracaoDecimal, fracaoInteira = math.modf(valor)
    return int(fracaoDecimal * 100)

valorProduto = int(input("Informe o valor unitário do produto comprado: "))
quantidadeProduto = int(input("Informe a quantidade do produto comprado: "))

valorTotalSemDesconto = valorProduto * quantidadeProduto
resultado = calculaValorComDesconto(valorTotalSemDesconto)

print(f'O valor total da sua compra sem descontos é de: R$ {valorTotalSemDesconto}')
print(f'Observações sobre descontos: {resultado["descricaoDesconto"]}!')
print(f'Você recebeu um desconto de {resultado["descontoEmPorcentagem"]}% que representa R$ {resultado["valorDescontado"]}, portanto, o valor final à pagar é de R$ {resultado["valorFinalComDesconto"]}')