from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flinch/', views.flinch_index, name='index'),
    path('flinch/<int:flinch_id>/', views.flinch_detail, name='detail'),
]
