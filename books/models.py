from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_year = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    youtube_url = models.TextField(null=True, blank=True, help_text="Embed ссылка с YouTube")

    def average_rate(self):
        reviews = self.reviews_set.all()
        if reviews.exists():
            return round(sum(review.mark for review in reviews) / reviews.count(), 1)
        return 'Нет оценок'


    def __str__(self):
        return self.title


class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(validators=[MinValueValidator(1, message='Оценка должна быть от 1 до 5'),
                                           MaxValueValidator(5, message='Оценка должна быть от 1 до 5')])

    def __str__(self):
        return f'{self.author} - {self.book}'