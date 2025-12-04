def adicionar_livro(carrinho):
    while True:
        livro = input("Digite o nome do livro para adicionar ao carrinho ou 'sair': ")

        if livro.lower() == 'sair':
            break

        carrinho.append(livro)
        print(f'📘 Livro "{livro}" adicionado ao carrinho com sucesso!')

    print("\nLista de livros escolhidos:")
    for item in carrinho:
        print(f"- {item}")

carrinho = []
adicionar_livro(carrinho)
