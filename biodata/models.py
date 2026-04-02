from django.db import models
from django.contrib.auth.models import User


class AnggotaKelompok(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20, unique=True)
    prodi = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto_anggota/', blank=True, null=True)
    angkatan = models.CharField(max_length=10, blank=True)
    role = models.CharField(max_length=50, blank=True, default='Anggota')
    motto = models.TextField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['urutan', 'nama']
        verbose_name = 'Anggota Kelompok'
        verbose_name_plural = 'Anggota Kelompok'

    def __str__(self):
        return f"{self.nama} ({self.npm})"


class ThemeSettings(models.Model):
    """Pengaturan tema per user yang sudah login sebagai anggota kelompok"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='theme')
    
    # Warna
    primary_color = models.CharField(max_length=7, default='#6366f1')
    secondary_color = models.CharField(max_length=7, default='#8b5cf6')
    accent_color = models.CharField(max_length=7, default='#06b6d4')
    bg_color = models.CharField(max_length=7, default='#0f0f1a')
    text_color = models.CharField(max_length=7, default='#e2e8f0')
    card_bg = models.CharField(max_length=7, default='#1e1e35')
    
    # Font
    FONT_CHOICES = [
        ('Space_Grotesk', 'Space Grotesk'),
        ('Outfit', 'Outfit'),
        ('Sora', 'Sora'),
        ('DM_Sans', 'DM Sans'),
        ('Nunito', 'Nunito'),
        ('Raleway', 'Raleway'),
        ('Josefin_Sans', 'Josefin Sans'),
        ('Quicksand', 'Quicksand'),
    ]
    font_family = models.CharField(max_length=50, choices=FONT_CHOICES, default='Space_Grotesk')
    
    # Layout
    LAYOUT_CHOICES = [
        ('grid', 'Grid'),
        ('masonry', 'Masonry'),
        ('list', 'List'),
    ]
    card_layout = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default='grid')
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Theme milik {self.user.username}"
    
    @classmethod
    def get_global(cls):
        """Ambil theme global (dari admin/database langsung)"""
        return None


class GlobalTheme(models.Model):
    """Tema global yang berlaku untuk semua pengunjung"""
    primary_color = models.CharField(max_length=7, default='#6366f1')
    secondary_color = models.CharField(max_length=7, default='#8b5cf6')
    accent_color = models.CharField(max_length=7, default='#06b6d4')
    bg_color = models.CharField(max_length=7, default='#0f0f1a')
    text_color = models.CharField(max_length=7, default='#e2e8f0')
    card_bg = models.CharField(max_length=7, default='#1e1e35')
    font_family = models.CharField(max_length=50, default='Space_Grotesk')
    card_layout = models.CharField(max_length=20, default='grid')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Global Theme'

    def __str__(self):
        return "Global Theme Settings"

    @classmethod
    def get_instance(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
