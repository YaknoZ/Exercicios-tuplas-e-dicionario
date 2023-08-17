# Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
# Escreva um programa que leia todos os tempos em segundos e os guarde
# em um dicionário, onde a chave é o nome do corredor. Ao final diga de
# quem foi a melhor volta da prova e em que volta; e ainda a classificação
# final em ordem (1o o campeão). O campeão é o que tem a menor média
# de tempos.


def calcular_media(tempo_voltas):
    return sum(tempo_voltas) / len(tempo_voltas)

def main():
    corridores_tempos = {}

    for i in range(6):
        nome_corredor = input(f"Digite o nome do corredor {i + 1}: ")
        tempos_voltas = []

        for volta in range(1, 11):
            tempo = float(input(f"Digite o tempo da volta {volta} em segundos: "))
            tempos_voltas.append(tempo)

        corridores_tempos[nome_corredor] = tempos_voltas

    melhor_volta = float('inf')
    nome_melhor_volta = ""
    volta_melhor_volta = 0

    classificacao = []

    for nome, tempos_voltas in corridores_tempos.items():
        media = calcular_media(tempos_voltas)
        classificacao.append((nome, media))

        if min(tempos_voltas) < melhor_volta:
            melhor_volta = min(tempos_voltas)
            nome_melhor_volta = nome
            volta_melhor_volta = tempos_voltas.index(melhor_volta) + 1

    classificacao.sort(key=lambda x: x[1])

    print("\nMelhor volta:")
    print(f"Corredor: {nome_melhor_volta}")
    print(f"Volta: {volta_melhor_volta}")
    print(f"Tempo: {melhor_volta:.2f} segundos\n")

    print("Classificação final:")
    for i, (nome, media) in enumerate(classificacao, start=1):
        print(f"{i}º lugar: {nome} - Média de tempos: {media:.2f} segundos")

if __name__ == "__main__":
    main()
