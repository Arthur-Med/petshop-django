from django.contrib import admin
from django.urls import path
from pets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                 # A raiz do site (/) abre a Home
    path('painel/', views.painel_pets, name='painel'), # O site (/painel/) abre a Tabela
    path('cadastrar/', views.cadastrar_pet, name='cadastrar_pet'), # Rota de cadastro de animal
    path('cliente/novo/', views.cadastrar_cliente, name='cadastrar_cliente'), # Rota de cadastro de cliente 

]