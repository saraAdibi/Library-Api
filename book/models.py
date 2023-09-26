from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()


class Library(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    count = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/', null=True, default='')
    priority = models.IntegerField(default=1)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='Library')

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'Library'
