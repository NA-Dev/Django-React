from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

catchall = TemplateView.as_view(template_name='index.html')
