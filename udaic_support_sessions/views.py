from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

# Create your views here.

def asesoramientos_home(request):
        title = _('UdAIC')
        page_title = _('UdAIC Support')
        context = {
            'title': title,
            'page_title': page_title
        }
        return render(request, 'udaic_support_sessions/home.html', context)
