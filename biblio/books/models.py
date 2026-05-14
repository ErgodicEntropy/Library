from django.db import models


class Book(models.Model):

    GENRE_CHOICES = [
        ("fiction", "Fiction"),
        ("nonfiction", "Non-Fiction"),
        ("science", "Science"),
        ("history", "History"),
        ("fantasy", "Fantasy"),
        ("biography", "Biography"),
    ]

    title = models.CharField(
        max_length=200
    )

    author = models.CharField(
        max_length=150
    )

    description = models.TextField(
        max_length=1000,
        blank=True
    )

    isbn = models.CharField(
        max_length=13,
        unique=True
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        default="fiction"
    )

    published_date = models.DateField(
        null=True,
        blank=True
    )

    available = models.BooleanField(
        default=True
    )

    cover_image = models.ImageField(
        upload_to="books/covers/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} - {self.author}"



    