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
    path('flinch/<int:flinch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('flinch/<int:flinch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('flinch/<int:flinch_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    
]
