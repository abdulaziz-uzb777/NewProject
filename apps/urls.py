from django.urls import path

from apps.admin import PlanetAdmin
from apps.views import index_view

urlpatterns = [
    path('',index_view),

]