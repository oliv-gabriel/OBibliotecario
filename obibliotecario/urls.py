from django.urls import path
from obibliotecario.views import *

urlpatterns =[
    path('',index,name='home'),
    path('livros/',livros,name='livros')
]