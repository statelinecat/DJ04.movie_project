from dbm import error

from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm

# Create your views here.
def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'title': 'Фильмы', 'films': films})

def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = FilmsForm()
    return render(request, 'films/add_film.html', {'title': 'Добавление нового фильма', 'form': form, 'errors': error})

