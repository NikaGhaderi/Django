from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
        # f"/blog/{self.id}/"