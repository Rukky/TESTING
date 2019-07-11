from django.contrib import admin
from .models import Article, Filter, Author, Comment, Bills
# Register your models here.

admin.site.register(Article)
admin.site.register(Filter)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Bills)
