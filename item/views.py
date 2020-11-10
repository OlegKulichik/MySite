from django.shortcuts import render
from .models import Item
from django.views.generic import DetailView

def item_page(request):
    auto = Item.objects.all()
    return render(request, template_name = "item.html", context= {'auto':auto})

class AutoDatail(DetailView):
    model = Item
    template_name = 'details_view.html'
    context_object_name = 'article'