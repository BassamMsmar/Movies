from django.contrib import admin
from .models import MoviesInfo, Contributor, Review, Publisher, MovieContributor

# Register your models here.
admin.site.register(MoviesInfo)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Review)
admin.site.register(MovieContributor)