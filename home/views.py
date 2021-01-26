from django.shortcuts import render
from .forms import GeeksForm 
from django.shortcuts import redirect

def home_page(request):
    return render(request, template_name="home.html", context={})


def home_view(request): 
    form = GeeksForm(request.POST) 
    print(form)
    if request.POST: 
        temp = request.POST
        print(temp)
    return render(request, "home.html",context ={'form':form}) 
