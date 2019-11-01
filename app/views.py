from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import SignUpForm
from app.models import Items

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'database': Items.objects.all()
    }
    return render(request, 'index.html', tparams)

def contact(request):
    tparams = {
        'title': 'Find Us',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About Us',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def successregister(request):
    return render(request, 'successregister.html')

def getItem(request):
    if request.method == 'GET':
        titulo = request.GET['titulo']
        tparams = {
            'database': Items.objects.filter(id=titulo)
        }
        return render(request, 'infoItem.html', tparams)
    else:
        return redirect('home')

def search(request):
    if request.method == 'GET':
        pesquisa = request.GET['search']
        tparams = {
            'database': Items.objects.filter(titulo__contains=pesquisa)
        }
        return render(request, 'search.html', tparams)
    else:
        return redirect('home')