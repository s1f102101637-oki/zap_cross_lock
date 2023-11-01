from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message_page(request):
  return render(request, 'message/index.html', {})

def profile_view(request, name):
    # 何らかの処理（例：データベースからプロフィール情報を取得）
    return render(request, 'profile_template.html', {'name': name})