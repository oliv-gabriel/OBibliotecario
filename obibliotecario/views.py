from django.shortcuts import render
import json
import requests


def index(request):

    API_KEY = 'AIzaSyDGOeC_b875-tGdokQz09EEutLD1TEy6sY'

    genero = input('Digite o gênero do livro que deseja buscar: ')
    autor = input('Digite o nome do autor que deseja buscar: ')
    ano = input('Digite o ano de publicação que deseja buscar: ')

    parametros = {
        'q': '',
        'printType': 'books',
        'key': API_KEY
    }

    if genero:
        parametros['q'] += f'subject:{genero}'
    if autor:
        if parametros['q']:
            parametros['q'] += '+'
        parametros['q'] += f'inauthor:{autor}'
    if ano:
        if parametros['q']:
            parametros['q'] += '+'
        parametros['q'] += f'published:{ano}'

    url = 'https://www.googleapis.com/books/v1/volumes'
    response = requests.get(url, params=parametros)

    # AQUI
    dados = response.json()
    dados = 'dados'

    if 'items' in dados:
        for item in dados['items']:
            print(item)
            titulo= item['volumeInfo'].get('title', 'Título desconhecido')
            autores= item['volumeInfo'].get('authors', ['Autor desconhecido'])
            print(f'- {titulo}, por {", ".join(autores)}')
    else:
        print('Nenhum resultado encontrado.')

    return render(request, 'obibliotecario/index.html', )


def livros(request,):
    dados = 'dadosads'
    
    return render(request, 'obibliotecario/livros.html', {'dados': dados})
