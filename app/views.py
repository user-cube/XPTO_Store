from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import SignUpForm, EmailForm
from app.models import Items, Profile, Encomenda
import os
from django.db.models import Count, F, Sum


def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'database': Items.objects.all()
    }
    return render(request, 'index.html', tparams)


def findus(request):
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
    return render(request, 'signUp.html', {'form': form})


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
        tipo = request.GET['pesquisa']
        if tipo == "nome":
            tparams = {
                'database': Items.objects.filter(titulo__contains=pesquisa)
            }
        if tipo == "desc":
            tparams = {
                'database': Items.objects.filter(descricao__contains=pesquisa)
            }
        if tipo == "disp":
            tparams = {
                'database': Items.objects.filter(quantidade__gt=0)
            }
        if tipo == "precoa":
            tparams = {
                'database': Items.objects.all().order_by("preco")
            }
        if tipo == "precod":
            tparams = {
                'database': Items.objects.all().order_by("-preco")
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
            return redirect('profileedit')


def painel(request):
    if request.user.is_authenticated and request.user.is_superuser:
        tparams = {
            'database': Items.objects.all()
        }
        return render(request, 'adminPanel.html', tparams)
    else:
        return redirect('home')


def addProducts(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'addItem.html')
    else:
        return redirect('home')


def processAdd(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            adder = Items(titulo=request.POST['titulo'], short=request.POST['short'],
                          descricao=request.POST['descricao'], preco=request.POST['preco'],
                          picture=request.FILES['picture'], quantidade=request.POST['quantidade'])
            adder.save()
            return redirect('adminpanel')
        else:
            return redirect('home')
    else:
        return redirect('home')


def editProducts(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            tparams = {
                'database': Items.objects.filter(id=request.GET['id'])
            }
            return render(request, 'editItem.html', tparams)
        else:
            return redirect('home')
    else:
        return redirect('home')


def processEdit(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            items = Items.objects.get(id=request.POST['id'])
            items.short = request.POST['short']
            items.titulo = request.POST['titulo']
            items.descricao = request.POST['descricao']
            items.preco = request.POST['preco']
            if 'picture' in request.FILES:
                items.picture = request.FILES['picture']
            items.quantidade = request.POST['quantidade']
            items.save()
            return redirect('/edititem?id=' + request.POST['id'])
        else:
            return redirect('home')
    else:
        return redirect('home')


def removeProducts(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            Items.objects.get(id=request.GET['id']).delete()
            return redirect('adminpanel')
        else:
            return redirect('home')
    else:
        return redirect('home')


def searchAdmin(request):
    if request.method == 'GET':
        pesquisa = request.GET['search']
        tparams = {
            'database': Items.objects.filter(titulo__contains=pesquisa)
        }
        return render(request, 'searchAdmin.html', tparams)
    else:
        return redirect('home')


def addCart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'products' in request.session.keys():
                prods = request.session.__getitem__('products')
                prods.append(request.POST['id'])
                request.session.__setitem__('products', prods)
            else:
                request.session.__setitem__('products', [])
                prods = request.session.__getitem__('products')
                prods.append(request.POST['id'])
                request.session.__setitem__('products', prods)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return redirect('home')
    else:
        return redirect('login')

def removeCart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            index = request.POST['index']
            products = request.session['products']
            products.pop(int(index))
            request.session.__setitem__('products', products)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('login')


def shoppingCart(request):
    if 'products' not in request.session.keys():
        return
    total = 0
    items = []
    for i in request.session['products']:
        prod = Items.objects.get(id=i)
        items.append(prod)
        total += prod.preco

    tparams = {
        'shoppingbag': items,
        'total': total
    }
    return render(request, 'shoppingCart.html', tparams)


def checkout(request):

    if not request.user.is_authenticated:
        return redirect('login')

    for i in request.session['products']:
        adder = Encomenda(user=request.user, produtos=Items.objects.get(id=i))
        adder.preco = Items.objects.get(id=i).preco
        adder.total = adder.preco * adder.quantidade
        adder.save()
        Items.objects.filter(id=i).update(quantidade=F('quantidade') - 1)
        request.session.__setitem__('products', [])

    send_mail(subject='Compra efetuada com sucesso',
              message='A tua compra já se encontra disponível no painel de itens comprados.\nPodes aceder em: https://xpto-store.herokuapp.com/boughtlist/\nGratos pela tua preferência,\nXPTO Store',
              from_email=os.getenv('EMAIL'),
              recipient_list=[request.user.email]
              )
    messages.info(request, "Compra efetuada com sucesso!")
    return redirect('boughtlist')


def bought(request):
    if request.user.is_authenticated:
        tparams = {
            "database": Encomenda.objects.filter(user=request.user).order_by("-id"),
            "year": datetime.now().year
        }
        return render(request, "salesList.html", tparams)
    else:
        return redirect('login'
                        '')
def boughtAdmin(request):
    if request.user.is_superuser and request.user.is_authenticated:
        tparams = {
            "database": Encomenda.objects.all().order_by("-id"),
            "year": datetime.now().year
        }
        return render(request, "salesListAdmin.html", tparams)
    else:
        return redirect('home')

def boughtSearch(request):
    if request.method == "GET" and 'search' in request.GET:
        if request.user.is_authenticated:
            tparams = {
                "database": Encomenda.objects.filter(user=request.user, produtos__titulo__contains=request.GET['search']).order_by("-id"),
                "year": datetime.now().year
            }
            return render(request, "salesList.html", tparams)
        else:
            return redirect('login')
    else:
        return redirect('home')

def boughtSearchAdmin(request):
    if request.method == "GET" and 'search' in request.GET :
        if request.user.is_authenticated and request.user.is_superuser:
            tparams = {
                "database": Encomenda.objects.filter(produtos__titulo__contains=request.GET['search']).order_by("-id"),
                "year": datetime.now().year
            }
            return render(request, "salesList.html", tparams)
        else:
            return redirect('login')
    else:
        return redirect('home')

def buyItem(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            adder = Encomenda(user=request.user, produtos=Items.objects.get(id=request.POST['id']))
            adder.preco = Items.objects.get(id=request.POST['id']).preco
            adder.total = adder.preco * adder.quantidade
            adder.save()

            Items.objects.filter(id=request.POST['id']).update(quantidade=F('quantidade') - 1)

            send_mail(subject='Compra efetuada com sucesso',
                      message='A tua compra já se encontra disponível no painel de itens comprados.\nPodes aceder em: https://xpto-store.herokuapp.com/boughtlist/\nGratos pela tua preferência,\nXPTO Store',
                      from_email=os.getenv('EMAIL'),
                      recipient_list=[request.user.email]
                      )
            messages.info(request, "Compra efetuada com sucesso!")
            return redirect('boughtlist')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('login')

def contact(request):
    return render(request, 'contactUS.html')

def sendEmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            mensagem = form.cleaned_data.get('message')

            if phone != None:
                send_mail(subject='Contacto de ' + name,
                          message= mensagem + "\nEste email foi enviado por: " + email + "\nContacto telefónico: " + str(phone),
                          from_email=os.getenv('EMAIL'),
                          recipient_list=[os.getenv('EMAIL_TO')]
                          )
            else:
                send_mail(subject='Contacto de ' + name,
                          message=mensagem + "\nEste email foi enviado por: " + email,
                          from_email=os.getenv('EMAIL'),
                          recipient_list=[os.getenv('EMAIL_TO')]
                          )

            messages.success(request, 'Email sent')
            return redirect('contact')

def openCharts(request):
    if request.user.is_superuser:
        stock = Items.objects.all()
        lista = [['Items', 'Quantidade']]
        for i in stock:
            lista.append([i.titulo, i.quantidade])
        return render(request, 'charts.html', {'lista':lista})
    else:
        raise PermissionDenied()

def analiseMes(request):
    if request.user.is_superuser:
        x = datetime.now()
        vendas = Encomenda.objects.filter(data__month=x.month, data__year=x.year).values('produtos_id').annotate(num=Count('produtos'))
        lista = [['Item', 'Quantidade']]
        for i in vendas:
            nome = Items.objects.filter(id=i['produtos_id'])
            for u in nome:
                lista.append([u.titulo, i['num']])
        return render(request, 'analiseVendas.html', {'lista':lista})
    else:
        raise PermissionDenied()

def analise(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        dinheiro = Encomenda.objects.filter(user=request.user).aggregate(Sum('total'))
        compras = Encomenda.objects.filter(user=request.user).aggregate(Count('id'))

        vendas = Encomenda.objects.filter(user=request.user).values('produtos_id').annotate(
            num=Count('produtos'))
        lista = [['Item', 'Quantidade']]
        for i in vendas:
            nome = Items.objects.filter(id=i['produtos_id'])
            for u in nome:
                lista.append([u.titulo, i['num']])

        tparams = {
            'database': Profile.objects.filter(user=request.user),
            'dinheiro': dinheiro['total__sum'],
            'compras': compras['id__count'],
            'lista': lista
        }
        return render(request, 'estatistica.html', tparams)
    else:
        if request.user.is_superuser:
            raise PermissionDenied()
        else:
            redirect('login')