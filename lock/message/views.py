from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message_page(request):
  return render(request, 'message/index.html', {})

def profile_view(request, name):
    # ここでプロフィールのデータを取得する
    # 例: profile = get_object_or_404(ProfileModel, name=name)
    context = {'profile': profile}
    return render(request, 'profile.html', context)