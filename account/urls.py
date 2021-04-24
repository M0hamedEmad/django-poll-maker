from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='account/change_password.html', success_url=reverse_lazy('login')), name='change_password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/reset_password.html'), name='reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='reset_password_d0ne'),
    path('reset_password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='reset_password_confirm'),
    path('reset_password/confirm/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='rpassword_reset_complete'),
]