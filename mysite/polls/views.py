from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def myview(request):
#     return render(request, 'myapp/index.html', {
#         'foo': 'bar',
#     }, content_type='application/xhtml+xml')