from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.author.username + " " + self.created_at.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])