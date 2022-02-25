from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.title
        
    # to reverse to post detail after creating new post using reverse so it's not hard coded
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])