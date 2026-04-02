from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
import json

from .models import AnggotaKelompok, GlobalTheme


def is_member(user):
    """Cek apakah user adalah anggota kelompok yang terdaftar"""
    if not user.is_authenticated:
        return False
    allowed = getattr(settings, 'ALLOWED_MEMBER_EMAILS', [])
    return user.email in allowed


def home(request):
    anggota = AnggotaKelompok.objects.all()
    theme = GlobalTheme.get_instance()
    context = {
        'anggota': anggota,
        'theme': theme,
        'is_member': is_member(request.user),
    }
    return render(request, 'biodata/home.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'biodata/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Berhasil logout.')
    return redirect('home')


@require_POST
def update_theme(request):
    """Hanya anggota kelompok yang bisa mengubah tema"""
    if not is_member(request.user):
        return JsonResponse({'success': False, 'error': 'Unauthorized: Hanya anggota kelompok yang dapat mengubah tampilan.'}, status=403)
    
    try:
        data = json.loads(request.body)
        theme = GlobalTheme.get_instance()
        
        allowed_fields = [
            'primary_color', 'secondary_color', 'accent_color',
            'bg_color', 'text_color', 'card_bg', 'font_family', 'card_layout'
        ]
        
        for field in allowed_fields:
            if field in data:
                val = data[field]
                # Validasi hex color
                if field.endswith('_color') or field == 'card_bg' or field == 'bg_color':
                    if not (val.startswith('#') and len(val) in [4, 7]):
                        return JsonResponse({'success': False, 'error': f'Format warna tidak valid: {field}'}, status=400)
                setattr(theme, field, val)
        
        theme.updated_by = request.user
        theme.save()
        
        return JsonResponse({'success': True, 'message': 'Tema berhasil diperbarui!'})
    
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Data tidak valid.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def get_theme(request):
    """Endpoint publik untuk mendapatkan tema saat ini"""
    theme = GlobalTheme.get_instance()
    return JsonResponse({
        'primary_color': theme.primary_color,
        'secondary_color': theme.secondary_color,
        'accent_color': theme.accent_color,
        'bg_color': theme.bg_color,
        'text_color': theme.text_color,
        'card_bg': theme.card_bg,
        'font_family': theme.font_family,
        'card_layout': theme.card_layout,
    })
