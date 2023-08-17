# Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
# chave (cpf), nome, idade, telefone. O programa deve ler um número
# indeterminado de dados, criar a agenda e imprimir todos os itens do
# dicionário no formato chave: nome-idadefone.

agenda = {}
while True:
    print("Menu:")
    print("1. Cadastrar nova chave")
    print("2. Exibir chaves cadastradas")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        cpf = input("Digite seu CPF: ")
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        telefone = input("Digite seu telefone: ")
        agenda[cpf] = {'nome': nome, 'idade': idade, 'telefone': telefone}
        print("Usuário cadastrado.")

    elif escolha == "2":
        for cpf, registro in agenda.items():
            print("CPF:", cpf)
            print("Nome:", registro['nome'])
            print("Idade:", registro['idade'])
            print("Telefone:", registro['telefone'], "\n")
        
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.\n")





# cpf = input("Digite seu CPF: ")
# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# telefone = input("Digite seu telefone: ")



# agenda = {'cpf':cpf, 'nome':nome, 'idade':idade, 'telefone':telefone}
# sorted(agenda)