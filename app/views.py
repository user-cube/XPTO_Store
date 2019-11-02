from datetime import datetime
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import SignUpForm
from app.models import Items, Profile


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
            profiler = Profile(nome=request.POST['first_name'],
                               user=request.POST['username'],
                               picture='app/static/img/default.jpg',
                               morada=request.POST['morada'],
                               zipcode=request.POST['zipcode'],
                               pais=request.POST['pais'])
            profiler.save()
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


def getProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        tparams = {
            'database': Profile.objects.filter(user=request.user)
        }
        return render(request, 'profile.html', tparams)


def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        tparams = {
            'database': Profile.objects.filter(user=request.user),
            'user': request.user
        }
        return render(request, 'editProfile.html', tparams)


def updateProfile(request):
    if request.method == 'POST':
        if str(request.POST['user']) == str(request.user):
            profiler = Profile.objects.get(user=request.user)
            if 'nome' in request.POST:
                profiler.nome = request.POST['nome']
                profiler.save()
            if 'morada' in request.POST:
                profiler.morada = request.POST['zipcode']
                profiler.save()
            if 'zipcode' in request.POST:
                profiler.zipcode = request.POST['zipcode']
                profiler.save()
            if 'pais' in request.POST:
                profiler.pais = request.POST['pais']
                profiler.save()
            if 'picture' in request.FILES:
                profiler.picture = request.FILES['picture']
                profiler.save()

            tparams = {
                'database': Profile.objects.filter(user=request.user),
                'user': request.user
            }
            return redirect('profileedit')
