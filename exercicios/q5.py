# Considere um sistema onde os dados são armazenados em dicionários.
# Nesse sistema existe um dicionario principal e o dicionário de backup.
# Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
# dados na tela e apaga o seu conteúdo. Crie um programa que insira dados
# em um dicionário, realizando o backup a cada dado e excluindo os dados
# do dicionário principal quando ele atingir tamanho 5.

def main():
    principal = {}  
    backup = {}  
    contador = 1 

    while True:
        data = input("Insira os nomes dos funcionários ")
        principal[f"Nome {contador}"] = data  
        backup[f"Nome {contador}"] = data  

        print("Nome inserido e backup realizado.")

        if len(principal) >= 5:
            print("Dicionário principal atingiu tamanho 5. Nomes:")
            for nome, value in principal.items():
                print(f"{nome}: {value}")
            principal.clear() 
            print("Dicionário principal limpo.")

        contador += 1

if __name__ == "__main__":
    main()