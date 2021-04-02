from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(request.user)
    # print(args, kwargs)
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": 'This is about us',
        'my_list':[123,4568,312, 'Abc']
    }
    return render(request, 'about.html', my_context)