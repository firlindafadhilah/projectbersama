from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tentang/', views.tentang, name='tentang'),  
    path('pendahuluan/', views.pendahuluan, name='pendahuluan'),
    path('notasi/', views.notasi, name='notasi'),
    path('kosong/', views.kosong, name='kosong'),
    path('bagian/', views.bagian, name='bagian'),
    path('hubungan/', views.hubungan, name='hubungan'),
    path('operasi/', views.operasi, name='operasi'),
    path('diagram/', views.diagram, name='diagram'),
    path('kubus/', views.kubus, name='kubus'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    path('kubus/', views.kubus, name='kubus'),
    path('prisma/', views.prisma, name='prisma'),
    path('limas/', views.limas, name='limas'),
    path('balok/', views.balok, name='balok'),
    path('substitusi/', views.substitusi, name='substitusi'),
    path('eliminasi/', views.eliminasi, name='eliminasi'),
    path('grafik/', views.grafik, name='grafik'),
    path('perbedaan/', views.perbedaan, name='perbedaan'),
    path('gabungan/', views.gabungan, name='gabungan'),
    
]