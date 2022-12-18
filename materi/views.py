from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import Mahasiswa

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def tentang(request):
    template = loader.get_template('tentang.html')
    return HttpResponse(template.render())
def pendahuluan(request):
    template = loader.get_template('pendahuluan.html')
    return HttpResponse(template.render())
def notasi(request):
    template = loader.get_template('notasi.html')
    return HttpResponse(template.render())
def kosong(request):
    template = loader.get_template('kosong.html')
    return HttpResponse(template.render())
def bagian(request):
    template = loader.get_template('bagian.html')
    return HttpResponse(template.render())
def hubungan(request):
    template = loader.get_template('hubungan.html')
    return HttpResponse(template.render())
def operasi(request):
    template = loader.get_template('operasi.html')
    return HttpResponse(template.render())
def diagram(request):
    template = loader.get_template('diagram.html')
    return HttpResponse(template.render())
def kubus(request):
    template = loader.get_template('kubus.html')
    return HttpResponse(template.render())
def mahasiswa(request):
    template = loader.get_template('mahasiswa.html')
    return HttpResponse(template.render())
def kubus(request):
    template = loader.get_template('kubus.html')
    return HttpResponse(template.render())
def prisma(request):
    template = loader.get_template('prisma.html')
    return HttpResponse(template.render())
def limas(request):
    template = loader.get_template('limas.html')
    return HttpResponse(template.render())
def balok(request):
    template = loader.get_template('balok.html')
    return HttpResponse(template.render())
def perbedaan(request):
    template = loader.get_template('perbedaan.html')
    return HttpResponse(template.render())
def grafik(request):
    template = loader.get_template('grafik.html')
    return HttpResponse(template.render())
def eliminasi(request):
    template = loader.get_template('eliminasi.html')
    return HttpResponse(template.render())
def substitusi(request):
    template = loader.get_template('substitusi.html')
    return HttpResponse(template.render())
def gabungan(request):
    template = loader.get_template('gabungan.html')
    return HttpResponse(template.render())