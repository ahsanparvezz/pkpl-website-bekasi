from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/update-theme/', views.update_theme, name='update_theme'),
    path('api/theme/', views.get_theme, name='get_theme'),
]
