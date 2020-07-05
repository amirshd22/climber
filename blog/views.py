from django.shortcuts import render , get_object_or_404
from .models import Blogs 
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger, InvalidPage
import random


def bl(request, blog_id):
    ob1 = get_object_or_404(Blogs , pk=blog_id)
    template = 'details.html'
    context = {
        'key1':ob1,
    }
    return render(request ,template,context)

def homepage(request):
    deli = Blogs.objects.all()
    paginator = Paginator(deli, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        items = paginator.get_page(page)
    except(EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)


    template = "home.html"
    context = {
       
        'items':items,
    }

    return render(request, template , context)
