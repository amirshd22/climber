from django.shortcuts import render




def about(request):
    templates = 'about.html'
    context= {}
    return render(request, templates, context )



def sell(request):
    templates = 'sell.html'
    context= {}
    return render(request, templates, context )



def rent(request):
    templates = 'rent.html'
    context= {}
    return render(request, templates, context )