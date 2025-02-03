from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import UploadedFile
import os
from django.conf import settings
from django.http import HttpResponse

ALLOWED_EXTENSIONS = [ "zip","rar","7z","tar.gz","gz"]
# Create your views here.
def index (request):
    return render(request, 'home/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None: 
            auth_login(request, user)
            return redirect('dashboard') #redirect to dashboard page
        else:
            messages.error(request, 'Incorrect email or password')
            
    return render(request, 'home/login.html')

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

def user_logout(request):
    logout(request)
    return render(request, 'home/user_logout.html')


def register(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validation des données
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'home/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'home/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'home/register.html')

        # Création de l'utilisateur
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=firstname,
            last_name=lastname,
        )
        user.save()

        # Message de succès et redirection
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')  # Redirige vers la page de connexion

    return render(request, 'home/register.html')
def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name='registration/password_reset_email.html'
            )
            return render(request, 'home/forgot_password_done.html')
    else:
        form = PasswordResetForm()
    return render(request, 'home/forgot_password.html', {'form': form})

# Vue pour demander la réinitialisation du mot de passe
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'home/forgot_password.html'
    email_template_name = 'home/password_reset_email.html'
    success_url = reverse_lazy('forgot_password_done')

# Vue pour afficher la confirmation d'envoi du lien
class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'home/forgot_password_done.html'

# Vue pour confirmer la réinitialisation via le lien
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'home/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

# Vue pour afficher la confirmation de réinitialisation réussie
class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'home/password_reset_complete.html'

class CustomPasswordResetView(PasswordResetView):
    template_name = 'home/forgot_password.html'  # Formulaire de demande de réinitialisation
    email_template_name = 'home/password_reset_email.html'  # Email envoyé à l'utilisateur
    subject_template_name = 'home/password_reset_subject.txt'  # Sujet de l'email
    success_url = reverse_lazy('forgot_password_done')  # Redirection après succès

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'home/password_reset_confirm.html'  # Template pour la réinitialisation
    success_url = reverse_lazy('password_reset_complete')  # Redirection après succès
    
def upload_page(request):
    return render(request, 'home/upload_page.html')

def upload_page(request):
    if request.method == "POST":
        # Récupération des fichiers
        normal_files = request.FILES.getlist('normal_files')  # Fichiers normaux
        anomalous_files = request.FILES.getlist('anomalous_files')  # Fichiers anormaux

        # Validation : vérifier que les fichiers ont été téléchargés
        if not normal_files or not anomalous_files:
            error_message = "Veuillez télécharger des fichiers normaux et anormaux avant de continuer."
            return render(request, 'home/upload_page.html', {'error': error_message})
        
        for file in normal_files:
            if not is_valid_extension(file.name):
                error_message = f"Le fichier {file.name} n'est pas une extension autorisée (acceptées: {', '.join(ALLOWED_EXTENSIONS)})."
                return render(request, 'home/upload_page.html', {'error': error_message})
            file_path = save_file_to_directory(file, 'normal')
            UploadedFile.objects.create(
                file=file_path, 
                file_type='normal'
            )
        for file in anomalous_files:
            if not is_valid_extension(file.name):
                error_message = f"Le fichier {file.name} n'est pas une extension autorisée (acceptées: {', '.join(ALLOWED_EXTENSIONS)})."
                return render(request, 'home/upload_page.html', {'error': error_message})
            file_path = save_file_to_directory(file, 'anomalous')
            UploadedFile.objects.create(
                file=file_path, 
                file_type='anomalous'
            )
        # Redirigez vers la page suivante si tout va bien
        return redirect('next_page')

    return render(request, 'home/upload_page.html')

def save_file_to_directory(file, file_type):
    sub_dir = os.path.join(settings.MEDIA_ROOT, file_type)
    os.makedirs(sub_dir, exist_ok=True)
    
    file_path = os.path.join(sub_dir, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return f'{file_type}/{file.name}'
 
def is_valid_extension(filename):
    ext= filename.split('.')[-1].lower()
    return ext in ALLOWED_EXTENSIONS
def next_page(request):
    return render(request, 'home/next_page.html')

def send_test_mail(request):
    subject = 'Test email'
    message = 'This is a test email.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['your_email@example.com']
    try:
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse('Email sent successfully')
    except Exception as e:
        return HttpResponse(f'Error sending email: {str(e)}')