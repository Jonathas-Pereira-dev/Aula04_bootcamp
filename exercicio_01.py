# Armazenar informações de um livro
# incluindo título, autor e ano de publicação. Imprima cada informação,

from typing import Dict, Any

livro_01: dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Analista",
    "Ano": 2005
}

livro_02: dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "Analista",
    "Ano": 2007
}

lista_de_livros = []
lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)

#lista_de_elementos: list = livro.items()
#for elemento in lista_de_elementos:
#    print(elemento)