from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'films/index.html', {'title': 'Фильмы'})

def add_film(request):
    return render(request, 'films/add_film.html', {'title': 'Добавление нового фильма'})
