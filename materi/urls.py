from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.profile, name='about'),  
    path('pendahuluan/', views.pendahuluan, name='pendahuluan'),
    path('notasi/', views.notasi, name='notasi'),
    path('kosong/', views.kosong, name='kosong'),
    path('bagian/', views.bagian, name='bagian'),
    path('hubungan/', views.hubungan, name='hubungan'),
    path('operasi/', views.operasi, name='operasi'),
    path('diagram/', views.diagram, name='diagram'),
    path('kubus/', views.kubus, name='kubus'),
    path('profile/', views.profile, name='profile'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    
]