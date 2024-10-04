#from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def segundo_template(request):
    
    fecha_actual = datetime.now()
    datos = {
        'fecha_actual': fecha_actual,
        'numeros': list(range(1, 11))    
    }

    return render(request, 'segundo_template.html', datos)