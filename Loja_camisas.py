# ================================
# Sistema de Venda de Camisetas
# Autor: Rhaldney Furtado
# ================================

# Exibe mensagem inicial do sistema
print("Bem-Vindos a Shirt's Store do Rhaldney Furtado\n")

# Dicionário com os modelos disponíveis
# Formato: Código: (Nome do modelo, Preço unitário)
modelos = {
    "MCS": ("Manga Curta Simples", 1.89),
    "MLS": ("Manga Longa Simples", 2.10),
    "MCE": ("Manga Curta com Estampa", 2.09),
    "MLE": ("Manga Longa com Estampa", 2.29),
}

# ============================================
# Função: Escolher modelo de camiseta
# ============================================
def escolha_modelo():
    while True:
        print("Entre com o modelo desejado:")

        # Exibe todos os modelos disponíveis
        for codigo, (nome, preco) in modelos.items():
            print(f"{codigo} - {nome} - R$ {preco:.2f}")

        # Recebe entrada do usuário e padroniza para maiúsculo
        modelo = input(">> ").upper()

        # Valida se o modelo existe
        if modelo in modelos:
            return modelo  # Retorna o código escolhido
        else:
            print("Opção inválida. Tente novamente.\n")

# ============================================
# Função: Escolher quantidade de camisetas
# ============================================
def num_camisetas():
    while True:
        try:
            # Solicita a quantidade
            quantidade = int(input("Entre com o número de camisetas: "))

            # Validação: quantidade máxima permitida
            if quantidade > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                print("Por favor, digite um valor menor.\n")
                continue

            # Validação: quantidade mínima
            if quantidade <= 0:
                print("Digite um número válido maior que zero.\n")
                continue

            return quantidade  # Retorna valor válido

        except ValueError:
            # Caso o usuário digite texto ou valor inválido
            print("Entrada inválida. Digite apenas números.\n")

# ============================================
# Função: Escolher tipo de frete
# ============================================
def escolha_frete():
    while True:
        print("\nEscolha o tipo de frete:")
        print("1 - Frete por Sedex – R$ 100,00")
        print("2 - Frete por Transportadora – R$ 200,00")
        print("3 - Frete Grátis (Retirar na loja)")

        opcao = input(">> ")

        # Validação das opções
        if opcao == "1":
            return 100.0, "Frete por Sedex"
        elif opcao == "2":
            return 200.0, "Frete por Transportadora"
        elif opcao == "3":
            return 0.0, "Retirada na loja (Grátis)"
        else:
            print("Opção inválida. Tente novamente.\n")

# ============================================
# Programa Principal
# ============================================

# Escolhas do usuário
modelo = escolha_modelo()
quantidade = num_camisetas()
valor_frete, tipo_frete = escolha_frete()

# Obtém dados do modelo escolhido
nome_modelo, preco_unitario = modelos[modelo]

# Calcula subtotal sem desconto
subtotal = preco_unitario * quantidade

# ============================================
# Aplicação de descontos
# ============================================

desconto = 0  # Valor padrão

if quantidade < 20:
    desconto = 0
elif quantidade < 200:
    desconto = 5
    subtotal *= 0.95
elif quantidade < 2000:
    desconto = 7
    subtotal *= 0.93
else:
    desconto = 12
    subtotal *= 0.88

# Calcula valor total com frete
total = subtotal + valor_frete

# ============================================
# Exibição do resumo do pedido
# ============================================

print("\n======= RESUMO DO PEDIDO =======")
print(f"Modelo: {nome_modelo} (R$ {preco_unitario:.2f})")
print(f"Quantidade: {quantidade}")

# Exibe desconto apenas se houver
if desconto > 0:
    print(f"Desconto aplicado: {desconto}%")

print(f"Frete: {tipo_frete}")
print(f"Total a pagar: R$ {total:.2f}")
print("================================")