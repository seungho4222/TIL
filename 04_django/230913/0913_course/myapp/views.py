from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'loginPage.html')


def login(request):
    context = {
        'id': request.GET.get('id'),
        'pw': request.GET.get('pw'),
    }
    return render(request, 'loginResult.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


def age(request, age):
    context = {
        'age': age
    }
    return render(request, 'age.html', context)