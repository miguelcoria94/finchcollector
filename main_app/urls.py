from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flinch/', views.flinch_index, name='index'),
    path('flinch/<int:flinch_id>/', views.flinch_detail, name='detail'),
    path('flinch/create/', views.FlinchCreate.as_view(), name='flinch_create'),
    path('flinch/<int:pk>/edit/', views.FlinchUpdate.as_view(), name='flinch_edit'),
    path('flinch/<int:pk>/delete/', views.FlinchDelete.as_view(), name='flinch_delete'),
    path('flinch/<int:flinch_id>/add_feeding/', views.add_feeding, name='add_feeding')
]
