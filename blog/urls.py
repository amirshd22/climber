
from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepage  , name='home' ),
    path('<int:blog_id>/', views.bl , name='blogs')
]