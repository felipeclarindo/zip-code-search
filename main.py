from functions import *

# cep = input("Digite o seu cep: ")

cep = "60762665"

busca = searchCode(cep)

if 'Cep' in busca:
    print("----------------------------")
    print("------ Informações Cep -----")
    print("----------------------------")

    for dado in busca:
        print(f"{dado}: {busca[dado]}")