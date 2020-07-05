
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('about/', views.about , name='about'),
    path('rent/', views.rent , name='rent'),
    path('sell/', views.sell , name='sell'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
