from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('About', views.about, name='about'),
    path('Projects', views.projects, name='projects'),
    path('Blog', views.opinions, name='opinions'),
    path('Hadejia', views.hadejia, name='hadejia'),
    path('Contact', views.contact, name='contact'),
    path('Blog/<int:article_id>', views.articles, name= 'article'),
    path('Comment', views.articles, name ='article'),
]
