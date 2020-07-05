from django.shortcuts import render, get_object_or_404
from .models import Blogs
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger, InvalidPage
# Create your views here.

def blogs(request, blog_id):
    ob1 = get_object_or_404(Blogs , pk=blog_id)
    template = 'html/details.html'
    context = {
        'key1':ob1,
    }
    return render(request ,template,context)


def home(request):
    blog = Blogs.objects.all()
    paginator = Paginator(blog, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        items = paginator.get_page(page)
    except(EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)



    templates= 'home.html'
    context = {
        'itmes':items,
    }

    return render(request, templates , context)