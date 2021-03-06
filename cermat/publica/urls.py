from django.urls import path
from . import views

app_name = 'publica'

urlpatterns =[
    # post views
    path('', views.post_list, name='lista_publica'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='publica_detalhe'),
    path('criar_publica/', views.CreatePublica.as_view(), name='criar_publica'),
    path('editar_publica/<slug>/', views.UpdatePublica.as_view(), name='editar_publica'),
    path('deletar_publica/<publica_id>/', views.delete_publica, name='deletar_publica'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('prod_cient/', views.prod_cient, name='prod_cient'),
    path('proj/<int:year>/<int:month>/<int:day>/<slug:project_slug>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('ger_pesq/', views.manage_researcher, name='ger_pesq'),
    path('deletar_pesq/<researcher_id>/', views.delete_researcher, name='deletar_pesq'),
    path('atualizar_pesq/<researcher_id>/', views.update_researcher, name='atualizar_pesq'),

]
