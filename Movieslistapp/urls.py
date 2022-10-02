from django.urls import path
from .views import movies_list, publisher_add_edit

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movesadd/', publisher_add_edit, name='publisher_add_edit'),
]
