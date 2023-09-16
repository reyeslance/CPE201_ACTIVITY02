from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Jesse Lance Reyes',
        'title': 'Introduction Page',
        'content': 'Hello,thank you for visiting my web portfolio! I am Lance, a dedicated Web Developer with a creative flair and a strong desire to bring digital experiences to life. This portfolio provides an inside look at my world of design, development, and innovation.',
    }

]
def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'portfo/home.html', context)

def about (request):
    return render(request, 'portfo/about.html')

def contact (request):
    return render(request, 'portfo/contact.html')