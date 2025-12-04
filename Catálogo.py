def exibir_catalogo(produtos):
    print("\n Catálogo de produtos disponíveis")
    print("--------------------------------")
    for produto in produtos:
        print(f'ID: {produto["id"]}')
        print(f'Título: {produto["titulo"]}')
        print(f'Autor: {produto["autor"]}')
        print(f'Descrição: {produto["descricao"]}')
        print(f'Preço: {produto["preco"]}')
        print("--------------------------------")

itens = [
    {"id": 1, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "descricao": "Livro do Frodo", "preco": 49.90},
    {"id": 2, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "descricao": "Livro de Ciúme, dúvida, obsessão", "preco": 39.90},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "descricao": "Livro sobre vigilância, opressão, totalitarismo", "preco": 59.90},
    {"id": 4, "titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "descricao": "Livro de guerra, palavras, resistência", "preco": 44.90},
    {"id": 5, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "descricao": "Livro de amizade, sensibilidade, imaginação", "preco": 29.90}
]

exibir_catalogo(itens)
