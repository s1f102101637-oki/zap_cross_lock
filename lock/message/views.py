from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message_page(request):
  return render(request, 'message/index.html', {})



PROFILE_DATA = {
    'airi': {
        'name': 'Airi',
        'image_url': 'images/airi.jpg',
        'description': 'Airiの説明文をここに書きます。',
    },
    'ayaka': {
        'name': 'Ayaka',
        'image_url': 'images/ayaka.jpg',
        'description': '説明文をここに書きます。',
    },
    'hayato': {
        'name': 'Hayato',
        'image_url': 'images/hayato.jpg',
        'description': '説明文をここに書きます。',
    },   
    'hinako': {
        'name': 'Hinako',
        'image_url': 'images/hinako.jpg',
        'description': '説明文をここに書きます。',
    },
    'kanon': {
        'name': 'Kanon',
        'image_url': 'images/kanon.jpg',
        'description': '説明文をここに書きます。',
    },
    'kei': {
        'name': 'Kei',
        'image_url': 'images/kei.jpg',
        'description': '説明文をここに書きます。',
    },
    'mio': {
        'name': 'Mio',
        'image_url': 'images/mio.jpg',
        'description': '説明文をここに書きます。',
    },
    'nana': {
        'name': 'Nana',
        'image_url': 'images/nana.jpg',
        'description': '説明文をここに書きます。',
    },
    'raimu': {
        'name': 'Raimu',
        'image_url': 'images/raimu.jpg',
        'description': '説明文をここに書きます。',
    },
    'riko': {
        'name': 'Riko',
        'image_url': 'images/riko.jpg',
        'description': '説明文をここに書きます。',
    },
    'rin': {
        'name': 'Rin',
        'image_url': 'images/rin.jpg',
        'description': '説明文をここに書きます。',
    },
    'sugi': {
        'name': 'Sugi',
        'image_url': 'images/sugi.jpg',
        'description': '説明文をここに書きます。',
    },
    'taiga': {
        'name': 'Taiga',
        'image_url': 'images/taiga.jpg',
        'description': '説明文をここに書きます。',
    },
    'takako': {
        'name': 'Takako',
        'image_url': 'images/takako.jpg',
        'description': '説明文をここに書きます。',
    },
    'yasu': {
        'name': 'Yasu',
        'image_url': 'images/Yasu.jpg',
        'description': '説明文をここに書きます。',
    },
    'zenji': {
        'name': 'Zenji',
        'image_url': 'images/zenji.jpg',
        'description': '説明文をここに書きます。',
    },
}

user_to_image = {
    'airi': 'airi.jpg',
    'ayaka': 'ayaka.jpg',
    'hayato': 'hayato.jpg',
    'hinako': 'hinako.jpg',
    'kanon': 'kanon.jpg',
    'kei': 'kei.jpg',
    'mio': 'mio.jpg',
    'nana': 'nana.jpg',
    'raimu': 'raimu.jpg',
    'riko': 'riko.jpg',
    'rin': 'rin.jpg',
    'sugi': 'sugi.jpg',
    'taiga': 'taiga.jpg',
    'takako': 'takako.jpg',
    'yasu': 'yasu.jpg',
    'zenji': 'zenji.jpg',
}

def profile(request, name):
    # user_to_image マッピングを使用する代わりに、PROFILE_DATA から情報を取得します。
    # デフォルトのプロフィールを設定する場合は、適宜デフォルト値を追加してください。
    profile_info = PROFILE_DATA.get(name, {
        'name': 'デフォルトユーザー',
        'image_url': 'images/default.jpg',
        'description': 'デフォルトの説明文です。',
    })
    return render(request, 'profile.html', {'profile': profile_info})