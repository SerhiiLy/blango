from django.db import models


class Post(models.Model):
  slug = models.SlugField(unique=True)
  


