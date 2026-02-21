from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    # Fields
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING
    )

    #dunder methods or double underscor methods or magic methods in python
    def __str__(self):
        return f"{self.title} - {self.author}"

    # Redirect after create/update
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
