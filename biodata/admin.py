from django.contrib import admin
from .models import AnggotaKelompok, GlobalTheme

@admin.register(AnggotaKelompok)
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'npm', 'prodi', 'role', 'urutan']
    list_editable = ['urutan']
    ordering = ['urutan']

@admin.register(GlobalTheme)
class GlobalThemeAdmin(admin.ModelAdmin):
    list_display = ['primary_color', 'font_family', 'updated_by', 'updated_at']
