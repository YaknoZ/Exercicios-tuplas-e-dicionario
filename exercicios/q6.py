# Escreva uma função que conta a quantidade de vogais em um texto e
# armazena tal quantidade em um dicionário, onde a chave é a vogal
# considerada.

def contador_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = {vogais: 0 for vogais in vogais}

    for char in texto:
        if char in vogais:
            contador[char] += 1

    return contador

texto = "Rapaz ele ta sem zap"
resultado = contador_vogais(texto)
for vogal, count in resultado.items():
    print(f"{vogal}: {count}")