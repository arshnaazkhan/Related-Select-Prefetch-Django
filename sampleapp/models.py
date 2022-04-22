from django.db import models

# Create your models here.
class Director(models.Model):  
    director_name = models.CharField(max_length=20)  
  
    def __str__(self):  
        return self.director_name  
      
class Movie(models.Model):  
    movie_title = models.CharField(max_length=150)  
    release_year = models.IntegerField()  
    director_name = models.ForeignKey(Director, on_delete = models.CASCADE, max_length=100)  
      
    def __str__(self):  
        return self.movie_title  