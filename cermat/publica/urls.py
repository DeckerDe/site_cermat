from django.urls import path
from . import views

app_name = 'publica'

urlpatterns =[
    # post views
    path('', views.post_list, name='lista_publica'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='publica_detalhe'),
    path('criar_publica/', views.CreatePublica.as_view(), name='criar_publica'),
    path('projetos/', views.lista_projetos, name='lista_projetos')
]
