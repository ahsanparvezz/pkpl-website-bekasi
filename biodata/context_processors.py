from .models import GlobalTheme

def theme_context(request):
    """Inject theme ke semua template"""
    theme = GlobalTheme.get_instance()
    return {
        'global_theme': theme,
    }
