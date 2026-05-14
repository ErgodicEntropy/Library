from django.db import models


class Home(models.Model):
    # Django ORM:
    # class -> database table

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        max_length=500
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title