from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import News



# Malumotlarni chiqarishni birinchi usuli
class IndexPageView(ListView):
	model = News
	template_name = 'index.html'
