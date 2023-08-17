# Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:
# nome, idade, telefone,endereço. Também usando d, imprima todos os
# itens do dicionário no formato chave : valor, ordenado pela chave

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
tel = input("Digite o seu telefone: ")
end = input("Digite seu endereço: ")

d = {'Nome': nome, 'Idade': idade, 'Telefone': tel, 'Endereço': end}

sorted(d)

for chave, valor in d.items():
    print(f"{chave}: {valor}")