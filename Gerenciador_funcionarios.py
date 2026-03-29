# ================================
# SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS
# ================================

# Exibe mensagem inicial ao iniciar o programa
print("Bem-vindo ao sistema de gerenciamento de funcionários")

# Exibe o nome do desenvolvedor
print("Desenvolvido por: Rhaldney Furtado")


# ================================
# VARIÁVEIS GLOBAIS
# ================================

# Lista que irá armazenar todos os funcionários cadastrados
lista_funcionarios = []

# Variável que armazena o ID inicial dos funcionários
# Esse valor será incrementado automaticamente a cada cadastro
id_global = 5134109


# ================================
# FUNÇÃO: CADASTRAR FUNCIONÁRIO
# ================================

def cadastrar_funcionario(id):
    # Exibe título da seção
    print("\n--- Cadastro de Funcionário ---")

    # Solicita o nome do funcionário
    nome = input("Digite o nome do funcionário: ")

    # Solicita o setor do funcionário
    setor = input("Digite o setor do funcionário: ")

    # Estrutura de repetição para garantir entrada válida do salário
    while True:
        try:
            # Solicita o salário e converte para número decimal (float)
            salario = float(input("Digite o salário do funcionário: "))
            break  # Sai do loop se o valor for válido
        except ValueError:
            # Caso o usuário digite algo inválido (ex: texto)
            print("Digite um valor numérico válido!")

    # Cria um dicionário com os dados do funcionário
    funcionario = {
        "id": id,           # ID único do funcionário
        "nome": nome,       # Nome do funcionário
        "setor": setor,     # Setor do funcionário
        "salario": salario  # Salário do funcionário
    }

    # Adiciona o dicionário na lista de funcionários
    lista_funcionarios.append(funcionario)

    # Mensagem de sucesso
    print("Funcionário cadastrado com sucesso!")


# ================================
# FUNÇÃO: CONSULTAR FUNCIONÁRIOS
# ================================

def consultar_funcionarios():
    # Loop infinito até o usuário decidir sair
    while True:
        # Exibe menu de consulta
        print("\n--- Consultar Funcionários ---")
        print("1 - Consultar Todos")
        print("2 - Consultar por ID")
        print("3 - Consultar por Setor")
        print("4 - Retornar ao menu")

        # Recebe a opção do usuário
        opcao = input("Escolha uma opção: ")

        # ================================
        # OPÇÃO 1: CONSULTAR TODOS
        # ================================
        if opcao == "1":
            # Verifica se a lista está vazia
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                # Percorre a lista e exibe cada funcionário
                for func in lista_funcionarios:
                    exibir_funcionario(func)

        # ================================
        # OPÇÃO 2: CONSULTAR POR ID
        # ================================
        elif opcao == "2":
            try:
                # Solicita o ID e converte para inteiro
                id_consulta = int(input("Digite o ID do funcionário: "))
            except ValueError:
                # Caso o usuário digite algo inválido
                print("ID inválido!")
                continue  # Volta ao início do loop

            # Variável de controle para verificar se encontrou
            encontrado = False

            # Percorre a lista buscando o ID informado
            for func in lista_funcionarios:
                if func["id"] == id_consulta:
                    exibir_funcionario(func)
                    encontrado = True

            # Caso não encontre o funcionário
            if not encontrado:
                print("Funcionário não encontrado")

        # ================================
        # OPÇÃO 3: CONSULTAR POR SETOR
        # ================================
        elif opcao == "3":
            # Solicita o nome do setor
            setor_consulta = input("Digite o setor: ")

            # Lista de funcionários encontrados no setor informado
            encontrados = [
                func for func in lista_funcionarios
                if func["setor"].lower() == setor_consulta.lower()
            ]

            # Verifica se encontrou algum funcionário
            if encontrados:
                for func in encontrados:
                    exibir_funcionario(func)
            else:
                print("Nenhum funcionário encontrado nesse setor")

        # ================================
        # OPÇÃO 4: RETORNAR AO MENU
        # ================================
        elif opcao == "4":
            return  # Sai da função e volta ao menu principal

        # ================================
        # OPÇÃO INVÁLIDA
        # ================================
        else:
            print("Opção inválida")


# ================================
# FUNÇÃO: REMOVER FUNCIONÁRIO
# ================================

def remover_funcionario():
    # Loop para garantir entrada válida
    while True:
        try:
            # Solicita o ID do funcionário a ser removido
            id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        except ValueError:
            # Caso o valor não seja numérico
            print("Digite um ID válido!")
            continue

        # Percorre a lista buscando o funcionário
        for func in lista_funcionarios:
            if func["id"] == id_remover:
                # Remove o funcionário da lista
                lista_funcionarios.remove(func)

                # Mensagem de sucesso
                print("Funcionário removido com sucesso!")
                return  # Sai da função

        # Caso o ID não seja encontrado
        print("ID não encontrado.")


# ================================
# FUNÇÃO AUXILIAR: EXIBIR FUNCIONÁRIO
# ================================

def exibir_funcionario(func):
    # Exibe dados do funcionário de forma organizada
    print("\n------------------------")
    print(f"ID: {func['id']}")
    print(f"Nome: {func['nome']}")
    print(f"Setor: {func['setor']}")
    print(f"Salário: R$ {func['salario']:.2f}")
    print("------------------------")


# ================================
# MENU PRINCIPAL
# ================================

# Loop principal do sistema
while True:
    # Exibe opções do menu
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Remover Funcionário")
    print("4 - Encerrar Programa")

    # Recebe a escolha do usuário
    opcao_menu = input("Escolha uma opção: ")

    # ================================
    # OPÇÃO 1: CADASTRAR
    # ================================
    if opcao_menu == "1":
        cadastrar_funcionario(id_global)

        # Incrementa o ID automaticamente para o próximo cadastro
        id_global += 1

    # ================================
    # OPÇÃO 2: CONSULTAR
    # ================================
    elif opcao_menu == "2":
        consultar_funcionarios()

    # ================================
    # OPÇÃO 3: REMOVER
    # ================================
    elif opcao_menu == "3":
        remover_funcionario()

    # ================================
    # OPÇÃO 4: SAIR
    # ================================
    elif opcao_menu == "4":
        print("Programa encerrado.")
        break  # Encerra o loop e o programa

    # ================================
    # OPÇÃO INVÁLIDA
    # ================================
    else:
        print("Opção inválida")