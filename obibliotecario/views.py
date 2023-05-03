
from django.shortcuts import render, redirect
import requests

def index(request):
    
    return render(request, 'obibliotecario/index.html' )


def pesquisa(request):
    genero = request.POST.get('genero')
    autor = request.POST.get('autor')
    ano = request.POST.get('ano')

    API_KEY = 'AIzaSyDGOeC_b875-tGdokQz09EEutLD1TEy6sY'

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

    livros = response.json()
    return livros




def livros(request):
    livros_api = pesquisa(request)
    livros = []
    for item in livros_api.get('items', []):
        volume_info = item.get('volumeInfo', {})
        livro = {
            'titulo': volume_info.get('title', ''),
            'autor': ', '.join(volume_info.get('authors', [])),
            'descricao': volume_info.get('description', ''),
        }
        imagem_links = volume_info.get('imageLinks', {})
        if 'thumbnail' in imagem_links:
            livro['imagem'] = imagem_links['thumbnail']
        else:
            livro['imagem'] = None
        livros.append(livro)

    return render(request, 'obibliotecario/livros.html', {'livros': livros})

