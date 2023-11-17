from django.shortcuts import render
from .models import MenuItem


def some_view(request):
    return render(request, 'your_template.html')


def main_menu_view(request):
    return render(request, 'menu_page.html')
