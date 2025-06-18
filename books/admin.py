from django.contrib import admin
from .models import Book, Reviews


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    search_fields = ('title', 'author')
    list_filter = ('published_year',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('book', 'mark')
    search_fields = ('author',)
    list_filter = ('mark',)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Book, BookAdmin)
