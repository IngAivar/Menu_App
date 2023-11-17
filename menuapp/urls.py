from django.urls import path, include
from .views import some_view, main_menu_view

urlpatterns = [
    path('some-view/', some_view, name='some-view'),
    path('main_menu/', main_menu_view, name='main-menu-view'),
]
