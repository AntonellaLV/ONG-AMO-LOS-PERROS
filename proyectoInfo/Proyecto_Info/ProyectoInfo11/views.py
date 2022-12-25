from django.shortcuts import render

def home(request):
    template_name = 'index.html'
    ctx ={}
    return render(request, template_name, ctx)
