from django.shortcuts import render

posts = [
    {
        'author':'emma zhang',
        'title': 'nightingale',
        'content': 'first novel',
        'date_posted': 'September 17, 2020'
    },
    {
        'author':'alice yang',
        'title': 'tomorrow',
        'content': 'tomorrow is a good day',
        'date_posted': 'September 15, 2020'
    }

]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})