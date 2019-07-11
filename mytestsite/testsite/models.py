from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.

class Filter(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a Filter (e.g. Bill, News, Opinion e.t.c)')

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}"
class Article(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=300)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    article= models.TextField(max_length= 1000, help_text= 'Write out your article here')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    filter = models.ManyToManyField(Filter, help_text='Select a filter for this article')

    publish_date = models.DateField(null=True, blank=True)


    def __str__(self):
        """String for representing the Model object."""
        return f"{self.id} - {self.title}"

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Comment(models.Model):
       author = models.CharField(max_length= 50)
       posted_on = models.DateTimeField(auto_now_add=True)
       body = models.TextField()
       article = models.ForeignKey('Article', on_delete=models.CASCADE )


       def __str__(self):
           return f'{self.body}, {self.author}, {self.posted_on}'

class Bills(models.Model):
    sponsor = models.CharField(max_length= 100)
    congress = models.CharField(max_length= 20)
    name = models.CharField(max_length= 200)
    latest_action = models.CharField(max_length=100)
    bill= models.TextField()
    introduced= models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.sponsor},{self.name},{self.introduced}' 
