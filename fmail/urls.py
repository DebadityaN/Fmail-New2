from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    MailListView,
    MailDetailView,
    MailCreateView,
    MailDeleteView,
    UserMailListView,
    SentMailListView
)

urlpatterns = [
    path('', login_required(MailListView.as_view(), login_url='login'), name='fmail-home'),
    path('user/<str:username>/', UserMailListView.as_view(), name='user-mails'),
    path('mail/<int:pk>/', MailDetailView.as_view(), name='mail-detail'),
    path('mail/new/', MailCreateView.as_view(), name='mail-create'),
    path('mail/<int:pk>/delete/', MailDeleteView.as_view(), name='mail-delete'),
    path('sent', login_required(SentMailListView.as_view(), login_url='login'), name='fmail-sent'),
    path('register', views.register, name='fmail-register'),
    path('profile', views.profile, name='fmail-profile'),
]