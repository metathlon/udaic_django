
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from udaic_blog.views import blog_home
from udaic_profile.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('udaic_support_sessions/', include('udaic_support_sessions.urls', namespace='udaic_support_sessions')),
    path('', blog_home, name='home'),
    path('udaic_blog/',  include('udaic_blog.urls', namespace='udaic_blog')),
    path('udaic_profile/',  include('udaic_profile.urls', namespace='udaic_profile')),
    path('register/', register, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)