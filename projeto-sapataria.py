import random

estoque = []
vendas = 0


while True:

    print("\n===== LOJA DE TÊNIS =====")
    print("1 - Cadastrar tênis")
    print("2 - Mostrar estoque")
    print("3 - Comprar tênis por marca")
    print("4 - Ver total de vendas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do tênis: ")
        marca = input("Marca: ")
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        tenis = {
            "nome": nome,
            "marca": marca,
            "preco": preco,
            "quantidade": quantidade
        }

        estoque.append(tenis)

        print("Tênis cadastrado com sucesso!")

    elif opcao == "2":

        if len(estoque) == 0:
            print("Estoque vazio.")

        else:
            print("\n===== ESTOQUE =====")

            for tenis in estoque:
                print(f"\nTênis: {tenis['nome']}")
                print(f"Marca: {tenis['marca']}")
                print(f"Preço: R$ {tenis['preco']:.2f}")
                print(f"Quantidade: {tenis['quantidade']}")

    elif opcao == "3":

        marca = input("Digite a marca (Nike, Adidas...): ")

        lista_marca = []

        for tenis in estoque:

            if tenis["marca"].lower() == marca.lower():

                if tenis["quantidade"] > 0:
                    lista_marca.append(tenis)

        if len(lista_marca) == 0:

            print("Nenhum tênis dessa marca disponível.")

        else:

            tenis_escolhido = random.choice(lista_marca)

            print("\n===== TÊNIS ENCONTRADO =====")
            print(f"Nome: {tenis_escolhido['nome']}")
            print(f"Marca: {tenis_escolhido['marca']}")
            print(f"Preço: R$ {tenis_escolhido['preco']:.2f}")
            print(f"Quantidade: {tenis_escolhido['quantidade']}")

            comprar = input("Deseja comprar? (s/n): ")

            if comprar.lower() == "s":

                quantidade = int(input("Quantidade: "))

                if quantidade <= tenis_escolhido["quantidade"]:

                    total = quantidade * tenis_escolhido["preco"]

                    tenis_escolhido["quantidade"] -= quantidade

                    vendas += total

                    print("Compra realizada com sucesso!")
                    print(f"Total: R$ {total:.2f}")

                else:
                    print("Estoque insuficiente.")

    elif opcao == "4":

        print(f"\nTotal vendido: R$ {vendas:.2f}")

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")