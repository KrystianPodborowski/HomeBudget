

from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .forms import FormWithCaptcha, CategoryForm, TransactionForm,  LoginForm, RegisterForm #LoginForm, RegisterForm od Adamsa
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from .models import Transaction, Category
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def budzet(request):
    return render(request, 'Budżet.html')

def przychody_dochody(request):
    return render(request, 'strona_przychody_dochody.html')

def home(request):
    context = {
        "captcha": FormWithCaptcha,
    }
    return render(request,"home.html",context)

"""
def konto_formularz(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        username = user.login
        email = user.email

        subject = 'Potwierdzenie Rejestracji Budżet domowy '
        message = f'Witaj {username},\n\nDziękujemy za rejestrację w naszym serwisie.\n\nPozdrawiamy,\nZespół serwisu \n Budżet domowy'
        from_email = 'apka.budzet2023@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        form = AccountForm()

    context = {
        'form': form
    }
    return render(request, "strona_konto.html", context)
"""

def kategorie_formularz(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save(commit = True)
        form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, "strona_kategorie.html",context)


def transakcje_formularz(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save(commit = True)
        form = TransactionForm()

    context = {
        'form': form,
    }
    return render(request, "strona_transakcje.html",context)

def strona_opcja(request):
    return render(request,"strona_opcja.html")



"""
def rejestracja_form(request):
    form = register_form(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        username = user.login
        email = user.email

        subject = 'Potwierdzenie rejestracji'
        message = f'Witaj {username},\n\nDziękujemy za rejestrację w naszym serwisie.\n\nPozdrawiamy,\nZespół serwisu'
        from_email = 'apka.budzet2023@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        form = register_form()

    context = {
        'form': form
    }
    return render(request, "strona_rejestracja.html", context)
"""

#Kod Adamsa poniżej

"""
def homepage(request):
	return render(request=request, template_name='home.html')
"""

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect("login_result", login_success=True) # replace 'home' with your desired URL name
            else:
                form.add_error(None, "Incorrect username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'title': 'Login', 'header': 'Log in to your account'})

def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            username = user.username
            email = user.email
            subject = 'Potwierdzenie Rejestracji Budżet domowy '
            message = f'Witaj {username},\n\nDziękujemy za rejestrację w naszym serwisie.\n\nPozdrawiamy,\nZespół serwisu \n Budżet domowy'
            from_email = 'apka.budzet2023@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("registration_result", registration_success=True)
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_result(request, login_success):
    login_success = True if login_success.lower() == 'true' else False
    return render(request=request, template_name="login_result.html", context={"login_succes": login_success})


def registration_result(request, registration_success):
    registration_success = True if registration_success.lower() == 'true' else False
    return render(request=request, template_name="registration_result.html", context={"registration_success": registration_success})

def statystyki(request):
    transactions = Transaction.objects.order_by('-date_of_transaction')
    return render(request, 'statystyki.html', {'transactions': transactions})

def wykresy(request):
    # wydatki
    labels_wydatki = []
    data_wydatki = []

    queryset_wydatki = Transaction.objects.filter(expense_or_proceeds='EXP')
    for wydatek in queryset_wydatki:
        labels_wydatki.append(wydatek.transaction)
        data_wydatki.append(wydatek.amount)
    # dochody
    labels_dochody = []
    data_dochody = []

    queryset_dochody = Transaction.objects.filter(expense_or_proceeds='PRO')
    for dochod in queryset_dochody:
        labels_dochody.append(dochod.transaction)
        data_dochody.append(dochod.amount)

    #proceeds_sum = Transaction.objects.filter(expense_or_proceeds='PRO').aggregate(Sum('amount'))
    #expenses_sum = Transaction.objects.filter(expense_or_proceeds='EXP').aggregate(Sum('amount'))
    #data = [proceeds_sum, expenses_sum]

    return render(request, 'wykresy.html', {'labels_wydatki': labels_wydatki, 'data_wydatki': data_wydatki,
                                            'labels_dochody': labels_dochody, 'data_dochody': data_dochody})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

def transaction_remove(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('statystyki')

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_list(request):
    categorys = Category.objects.all()
    return render(request, 'category_list.html', {'categorys': categorys})

def category_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')
