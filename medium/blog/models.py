from django.db import models

# Create your models here.



class User(models.Model):
    # posts
    # comments
    pass


class Post(models.Model):
    # user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    # comments
    pass


class Comment(models.Model):
    # user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    # post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    pass

