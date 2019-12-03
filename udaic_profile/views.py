from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from .forms import UdaicUserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UdaicUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = UdaicUserCreationForm()
    title = _('UdAIC Registration')
    title_page = _('UdAIC User Registration')
    return render(request, 'udaic_profile/register.html', {'form': form,
                                                          'title': title,
                                                          'title_page': title_page})
