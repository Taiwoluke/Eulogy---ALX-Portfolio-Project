from django.db import models

class Memory(models.Model):
    profile = models.ImageField(default='eulogy_fallback.png', blank=True)
    name = models.CharField(max_length=50)
    lifeline = models.CharField(max_length=150)
    story = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.slug
