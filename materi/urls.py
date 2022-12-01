from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.profile, name='about'),  
    path('pendahuluan/', views.pendahuluan, name='pendahuluan'),
    path('notasi/', views.notasi, name='notasi'),
    path('kubus/', views.kubus, name='kubus'),
    path('limas/', views.limas, name='limas'),
    path('prisma/', views.prisma, name='prisma'),
    path('profile/', views.profile, name='profile'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    
]