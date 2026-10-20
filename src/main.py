from animal import Animal, Elefante, Leao, Macaco
from tratador import Tratador
from recinto import Recinto
from administrador import Administrador
from arquivos import salvar_atividade, ler_atividades

admin = Administrador()

leao = Leao("Simba")
macaco = Macaco("Caco")
elefante = Elefante("Dumbo")
girafa = Animal("Melman", "Girafa", "Folhas")

tratador = Tratador("João")

recinto = Recinto("Selva")

animais = [leao, macaco, elefante, girafa]

while True:

    print("\n===== ZOOLÓGICO =====")
    print("1 - Alimentar animal")
    print("2 - Tratar animal")
    print("3 - Limpar recinto")
    print("4 - Banho de sol")
    print("5 - Relatório")
    print("6 - Ler arquivo")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        print("\nEscolha o animal:")

        for i, animal in enumerate(animais):
            print(f"{i+1} - {animal.nome} ({animal.especie})")

        try:
            escolha = int(input("Animal: "))
            
            if escolha < 1 or escolha > len(animais):
                print("Animal inválido!")
                continue

            animal_escolhido = animais[escolha - 1]

        except ValueError:
            print("Digite apenas números.")
            continue

        atividade = tratador.alimentar_animal(animal_escolhido)

        print(atividade)
        admin.registrar(tratador.nome, atividade)
        salvar_atividade(atividade)

    elif opcao == "2":
        print("\nEscolha o animal:")

        for i, animal in enumerate(animais):
            print(f"{i+1} - {animal.nome} ({animal.especie})")

        try:
            escolha = int(input("Animal: "))
                 
            if escolha < 1 or escolha > len(animais):
                print("Animal inválido!")
                continue
       
            animal_escolhido = animais[escolha - 1]
       
        except ValueError:
            print("Digite apenas números.")
            continue
        
        atividade = tratador.tratar_animal(animal_escolhido)

        print(atividade)
        admin.registrar(tratador.nome, atividade)
        salvar_atividade(atividade)

    elif opcao == "3":
        atividade = tratador.limpar_recinto(recinto)

        print(atividade)
        admin.registrar(tratador.nome, atividade)
        salvar_atividade(atividade)

    elif opcao == "4":
        print("\nEscolha o animal:")
        
        for i, animal in enumerate(animais):
            print(f"{i+1} - {animal.nome} ({animal.especie})")
        
        try:
            escolha = int(input("Animal: "))
            
            if escolha < 1 or escolha > len(animais):
                print("Animal inválido!")
                continue

            animal_escolhido = animais[escolha - 1]

        except ValueError:
            print("Digite apenas números.")
            continue
        atividade = tratador.banho_sol(animal_escolhido)

        print(atividade)
        admin.registrar(tratador.nome, atividade)
        salvar_atividade(atividade)

    elif opcao == "5":

        admin.exibir_relatorio()

    elif opcao == "6":

        ler_atividades()

    elif opcao == "0":

        print("Encerrando...")
        break

    else:
        print("Opção inválida")
