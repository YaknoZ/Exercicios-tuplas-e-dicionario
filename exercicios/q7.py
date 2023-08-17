# Escreva um programa que lê duas notas de vários alunos e armazena tais
# notas em um dicionário, onde a chave é o nome do aluno. A entrada de
# dados deve terminar quando for lida uma string vazia como nome.
# Escreva uma função que retorna a média do aluno, dado seu nome.


def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def main():
    alunos_notas = {}

    while True:
        nome = input("Digite o nome do aluno (ou deixe em branco para sair): ")
        if nome == "":
            break

        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        alunos_notas[nome] = [nota1, nota2]

    while True:
        nome_busca = input("Digite o nome do aluno para calcular a média (ou deixe em branco para sair): ")
        if nome_busca == "":
            break

        if nome_busca in alunos_notas:
            notas_do_aluno = alunos_notas[nome_busca]
            media = calcular_media(notas_do_aluno)
            print(f"A média do aluno {nome_busca} é: {media:.2f}")
        else:
            print("Aluno não encontrado.")

if __name__ == "__main__":
    main()
