from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import Mahasiswa

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def pendahuluan(request):
    template = loader.get_template('pendahuluan.html')
    return HttpResponse(template.render())
def notasi(request):
    template = loader.get_template('notasi.html')
    return HttpResponse(template.render())
def kubus(request):
    template = loader.get_template('kubus.html')
    return HttpResponse(template.render())
def limas(request):
    template = loader.get_template('limas.html')
    return HttpResponse(template.render())
def prisma(request):
    template = loader.get_template('prisma.html')
    return HttpResponse(template.render())
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())
def mahasiswa(request):
    template = loader.get_template('mahasiswa.html')
    return HttpResponse(template.render())