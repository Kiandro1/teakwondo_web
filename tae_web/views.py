from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',context={})

def history(request):
    return render(request, 'historia.html', context= {})
def list_hours(request):
    days = { 'lunes':'Lunes menores de 17:00 hs a 19:00 hs, mayores de 19:00 hs a 21:00 hss',
            'martes': 'Martes de 18:00 hs a 20:00 hs entrenamiento de competición', 
            'miercoles': 'Miércoles: menores de 17:30 hs a 19:30 hs, mayores de 19:30 hs a 21:30 hs ', 
            'jueves': 'Jueves: práctica de formas 19:00 hs a 21:00 hs',
            'viernes': 'Viernes: Menores de 17:00 hs a 19:00 hs, mayores de 19:00 hs a 21:00 hs', 
            'sabado': 'Sabados: cinturones negros de 10:00 hs a 12:00 hs'        
    }
    return render(request, 'list-hours.html', context= {'days':days})