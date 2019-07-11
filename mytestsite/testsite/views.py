from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail
from .forms import ContactForm, CommentForm
from .models import Article, Author, Comment

# Create your views here.

def contact(request):
    form = ContactForm(request.POST)
    # if this is a POST request we need to process the form data
    if form.is_valid():
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        number = range(form.cleaned_data['number'])

        recipients = ['Ibrahimruqayya@gmail.com']


        send_mail(name, message, sender,number, recipients)
        return render(request, 'testsite/Success.html')



def home(request):
    form = ContactForm

    return render(request, 'testsite/index.html', {'form': form})

def about(request):

    return render(request, 'testsite/About.html')

def opinions(request):

    context = {
        "article": Article.objects.all().order_by('publish_date')
    }

    return render(request, 'testsite/Blog.html', context)

def projects(request):

    return render(request, 'testsite/Projects.html')

def hadejia(request):

    return render(request, 'testsite/Hadejia.html')

def articles(request, article_id):
    try:
        article = Article.objects.get(pk= article_id)
        form = CommentForm()
        if request.method == 'POST':
           form = CommentForm(request.POST)
           if form.is_valid():
               comment = Comment(
                  author=form.cleaned_data["author"],
                  body=form.cleaned_data["body"],
                  article=article
               )
               comment.save()
        comments = Comment.objects.filter(article=article)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    context =  {
         'article':article,
         'comments':comments,
         'form':form,
    }

    return render(request, 'testsite/Articles.html', context)
