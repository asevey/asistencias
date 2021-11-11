from django.urls import path

from .views import banco_create, lista_banco, persona_create, persona_lista




app_name = 'persona'
urlpatterns = [
    # programa views
    
    path('cuentabancaria/', banco_create, name='banco_create'),
    path('crearPersona/',persona_create,name='persona_create'),
    path('listar/',persona_lista,name='lista_persona'),
    path('lista/<int:pk>',lista_banco,name='lista_banco'),
]