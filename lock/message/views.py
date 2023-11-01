from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message_page(request):
  return render(request, 'message/index.html', {})