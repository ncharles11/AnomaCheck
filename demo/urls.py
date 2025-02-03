from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login, name= 'login'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name= 'register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),  # Add this URL to your project's urls.py file.  # This URL will display a form for users to enter their email address.  # When the form is submitted, Django will send a password reset email to the user's email address.  # The email template is located at 'registration/password_reset_email.html'.  # You can customize this template as needed.
    path('forgot_password/', views.PasswordResetView.as_view(), name='forgot_password'),
    path('forgot_password_done/', views.PasswordResetDoneView.as_view(), name='forgot_password_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('forgot_password/', views.CustomPasswordResetView.as_view(), name='forgot_password'),
    path('forgot_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='home/forgot_password_done.html'), name='forgot_password_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('upload_page/', views.upload_page, name='upload_page'),
    path('next_page/', views.next_page, name='next_page'),
    path('send_test_mail/', views.send_test_mail, name='send_test_mail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)