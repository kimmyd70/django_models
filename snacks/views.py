from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class SnackListView(ListView):
    template_name = 'snack_list.html'
