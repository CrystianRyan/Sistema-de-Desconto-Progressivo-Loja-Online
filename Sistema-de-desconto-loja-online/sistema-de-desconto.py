# Sistema de Desconto

# ENTRADA DE DADOS
#Solicita as informações do usuário pelo terminal
produto = input("Digite o produto da compra: ")
# Pede o nome do produto e guarda em formato de texto (string)
valor_compra = float(input("Digite o valor total da compra: R$ "))
# Pede o valor total, converte o texto digitado para número decimal (float)
# e armazena na variável 'valor_compra'

# PROCESSAMENTO
# Define qual porcentagem de desconto será aplicada
# Regra 1: Compras menores que R$ 200,00 recebem 5% de desconto
if valor_compra < 200:
    desconto = 0.05  # 5% em decimal
    print("Você ganhou 5% de desconto!")
 # Regra 2: Compras entre R$ 200,00 e R$ 299,99 recebem 10% de desconto   
elif valor_compra >= 200 and valor_compra < 300:
    desconto = 0.10
    print("Desconto de 10% aplicado!")
 # Regra 3: Qualquer valor igual ou maior que R$ 300,00 recebe 15% de desconto   
else:
    desconto = 0.15
    print("Desconto de 15% aplicado!")

# CÁLCULOS MATEMÁTICOS
#Processa o desconto e o valor final a ser pago
# Multiplica o valor total pela taxa de desconto para saber o valor em reais economizado
valor_desconto = valor_compra * desconto
#Subtrai o valor do desconto do valor original da compra para obter o preço final
valor_final = valor_compra - valor_desconto

# SAÍDA DE DADOS
# Exibe os resultados finais formatados na tela
# Mostra o nome do produto inserido
print(f"Produto: {produto}")
# Mostra quanto foi economizado em reais (.2f força o número a ter 2 casas decimais)
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
# Mostra o total que o cliente precisa pagar no final
print(f"Valor final a pagar: R$ {valor_final:.2f}")
