from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


# Create your views here.
def blog_home(request):
    title = _('UdAIC')
    page_title = _('UdAIC Blog')
    context = {
        'title': title,
        'page_title': page_title
    }
    return render(request, 'udaic_blog/home.html', context)
