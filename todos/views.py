from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
#from django.core import serializers

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def task_all(request):
    if request.method == 'POST':
        # Creamos
        tk = Task() #Instancio de la clase Task
        tk.title = request.POST.get('title') # capturamos el valor que envia el formulario titlee desde el frontend
        tk.save() # guardo la tarea en la base de datos
        return JsonResponse({"id": tk.id, "title": tk.title, "completed": tk.completed})
    else:
        t = Task.objects.all()
    # tt = serializers.serialize('json', t)
        tobjects = []
        for x in t:
            tobjects.append({
                'id': x.id,
                'title': x.title,
                'completed': x.completed
            })
        return JsonResponse(tobjects, safe=False)

def task_toggle(request, task_id):
    tk = Task.objects.get(id =task_id) # capturo el objeto
    tk.completed = not tk.completed # cambio el estado de la tarea de F V y de V F
    tk.save() # guardo la tarea en la base de datos
    return JsonResponse({"id": tk.id, "title": tk.title, "completed": tk.completed}) 

def task_edit(request, task_id):
    tk = Task.objects.get(id =task_id) # capturo el objeto task
    titulo= request.POST.get('title') # capturamos el valor que envia el formulario
    tk.title = titulo # cambiamos el valor de la tarea
    tk.save() # guardo la tarea en la base de datos
    return JsonResponse({"id": tk.id, "title": tk.title, "completed": tk.completed})




    