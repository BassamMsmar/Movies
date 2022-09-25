import email
from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(max_length=200, help_text="The name of thePublisher. ")
    website = models.URLField(help_text=" The publisher's website. ")
    email = models.EmailField(help_text=" The publisher's email address. ")

    def __str__(self):
        return self.name


class Contributor(models.Model):
    first_name = models.CharField(max_length=200, help_text="The contributor first name. ")
    last_name = models.CharField(max_length=200, help_text="The contributor last name. ")
    email = models.EmailField(help_text=" The contact email for the contributor. ")
    


class MoviesInfo(models.Model):
    name = models.CharField(max_length=200, help_text="The name of the Movie. ")
    date = models.DateField(verbose_name="Date of The Movie was released. ")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, through="MovieContributor")
    

    def __str__(self):
        return self.name


class MovieContributor(models.Model):
    class ContributorRole(models.TextChoices):
        ACTOR = "ACTOR", "Actor"
        DIRECTOR = "DIRECTOR", "Director"
    movie = models.ForeignKey(MoviesInfo, on_delete=models.CASCADE)
    contributors = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the Movie. ", choices= ContributorRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="The Review text. ")
    rating = models.IntegerField(help_text="The rating the review has given. ")
    date_created = models.DateTimeField(auto_now_add=True, help_text="the date and time review was created. ")
    movie = models.ForeignKey(MoviesInfo, on_delete=models.CASCADE, help_text="the movies that this review is for. ", blank=False, null=False )
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, blank=False,null=False )






