from django.shortcuts import render
from .models import MoviesInfo, Review
from .utils import average_rating


# Create your views here.

def movies_list(request):
    movies = MoviesInfo.objects.all()
    movie_list =[]
    for Movie in movies:
        reviews = Movie.review_set.all()
        if reviews:
            Movie_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            Movie_rating = None
            number_of_reviews = 0

        movie_list.append({'Movie':Movie, 'Movie_rating':Movie_rating, 'number_of_reviews':number_of_reviews})

    context = {'movie_list': movie_list,}
    return render(request, 'movieslist/movieslist.html', context)
