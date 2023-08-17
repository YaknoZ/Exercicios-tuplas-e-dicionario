# Crie um programa que cadastre informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um dicionário. Depois remova todas as
# pessoas menores de 18 anos do dicionário e coloque em outro dicionário.


pessoas = {}
pessoas_de_menor = {}
while True:
    print("Menu:")
    print("1. Cadastrar nova chave")
    print("2. Exibir chaves cadastradas")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        cpf = input("Digite seu CPF: ")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            pessoas_de_menor[cpf] = {'nome': nome, 'idade': int(idade)}
            print("Usuário menor de 18 anos cadastrado.")
        else:
            pessoas[cpf] = {{'nome': nome, 'idade': idade}}
            print("Usuário cadastrado")

    elif escolha == "2":
        print("Usuários de maior: ")
        for cpf, registro in pessoas.items():
            print("CPF:", cpf)
            print("Nome:", registro['nome'])
            print("Idade:", registro['idade'], "\n")
        print("Usuários de menor: ")
        for cpf, registro in pessoas.items():
            print("CPF:", cpf)
            print("Nome:", registro['nome'])
            print("Idade:", registro['idade'], "\n")
        
        
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.\n")
