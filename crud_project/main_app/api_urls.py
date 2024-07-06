from django.urls import path
from .views import TipodocumentoListCreate

urlpatterns = [
    path('tipodocumento/', TipodocumentoListCreate.as_view(), name='tipodocumento_list_create'),
]
