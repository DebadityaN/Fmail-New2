from django.shortcuts import render, redirect, get_object_or_404
from .models import Mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm


class MailListView(ListView):
    model = Mail
    template_name = 'fmail/home.html'
    context_object_name = 'mails'
    ordering = ['-datetime']
    paginate_by = 50


class SentMailListView(ListView):
    model = Mail
    template_name = 'fmail/sent.html'
    context_object_name = 'mails'
    ordering = ['-datetime']
    paginate_by = 50


class UserMailListView(ListView):
    model = Mail
    template_name = 'fmail/user_mails.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'mails'
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Mail.objects.filter(sender=user).order_by('-datetime')


class MailDetailView(DetailView):
    model = Mail


class MailCreateView(CreateView):
    model = Mail
    fields = ['reciever', 'title', 'info']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


class MailDeleteView(DeleteView):
    model = Mail
    success_url = '/'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created successfully, Now you can log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'fmail/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('fmail-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'fmail/profile.html', context=context)
