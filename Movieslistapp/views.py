from django.shortcuts import render
from .models import MoviesInfo


# Create your views here.

def movies_list(request):
    move_list = MoviesInfo.objects.all()

    content = {'move_list': move_list}
    return render(request, 'movieslist/movieslist.html', content)
