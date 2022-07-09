from urllib.robotparser import RobotFileParser
from django.db import models



class Actor(models.Model):
    # movies
    # roles
    pass

    
class Movie(models.Model):
    actors = models.ManyToManyField(Actor, through='Role', related_name='movies')
    # roles
    pass


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    
