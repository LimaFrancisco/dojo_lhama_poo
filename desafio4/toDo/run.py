from model import Livro, Biblioteca

livro1 = Livro('O Hobbit', 'Tolkien', 1937, 1)
livro2 = Livro('A Sociedade do Anel', 'Tolkien', 1954, 2)
livro3 = Livro('As Duas Torres', 'Tolkien', 1954, 3)
livro4 = Livro('O Retorno do Rei', 'Tolkien', 1955, 4)
livro5 = Livro('A Sociedade do Anel', 'Tolkien', 1954, 5)
livro6 = Livro('O Silmarillion', 'Tolkien', 1977, 6)

biblioteca = Biblioteca()

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)
biblioteca.cadastrar_livro(livro4)
biblioteca.cadastrar_livro(livro5)
biblioteca.cadastrar_livro(livro6)

print(biblioteca.listar_livros())
