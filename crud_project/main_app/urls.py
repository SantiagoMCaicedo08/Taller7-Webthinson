from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persona/new/', views.persona_create, name='persona_create'),
    path('persona/<int:pk>/', views.persona_detail, name='persona_detail'),
    path('persona/<int:persona_id>/tipodocumento/new/', views.tipodocumento_create, name='tipodocumento_create'),
    path('persona/<int:persona_id>/tipodocumento/edit/', views.tipodocumento_update, name='tipodocumento_update'),
    path('persona/<int:persona_id>/tipodocumento/delete/', views.tipodocumento_delete, name='tipodocumento_delete'),
    path('api/tipodocumento/', views.TipodocumentoListCreate.as_view(), name='tipodocumento_list_create'),  # Asegúrate de usar el nombre correcto de la clase
]

