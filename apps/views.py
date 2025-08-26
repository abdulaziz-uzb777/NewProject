from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.models import Planet


def index_view(request):
    return render(request, 'index.html')

class ViewPage(ListView):
    template_name = 'index.html'
    context_object_name = 'planet'
    queryset = Planet.objects.all()


# Create your views here.
