from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Pages principales
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_page, name='upload_page'),

    # Authentification et gestion des utilisateurs
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),

    # Gestion du mot de passe (Django Auth)
    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='auth/forgot_password.html'), name='forgot_password'),
    path('forgot_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/forgot_password_done.html'), name='forgot_password_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),

    # Autres pages
    path('next_page/', views.next_page, name='next_page'),
    path('send_test_mail/', views.send_test_mail, name='send_test_mail'),
    path("patch_selection/", views.patch_selection, name="patch_selection")
]

# Gestion des fichiers médias en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
