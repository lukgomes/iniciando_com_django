from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar, name="cadastrar"),
    path('excluir/<int:id>', views.excluir, name="excluir"),
    path('visualizar/', views.visualizar)
]
