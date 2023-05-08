# https://ccbv.co.uk/ --VISTAS GENERICAS https://platzi.com/clases/2694-django/45284-implementando-generic-views-en-la-aplicacion/
'CREA LAS VISTAS'
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect #ESTO PERMITE GENERAR UN RESPUESTA HTTP
from .models import Employee,Role,Department
from django.db.models import Q
from django.views import generic
from django.urls.base import reverse

app_name='emp_app'
# https://platzi.com/clases/2694-django/45278-elevando-el-error-404/
def index(request):
    emps = Employee.objects.all() #BUSCA TODOS LOS ELEMENTOS
    emps_filter = get_object_or_404(Employee, name='Juan Cruz') #FILTRA Y SI NO ESTA, 404

    context = {  #ARRAY DE CAMPOS
        'emps':emps,
        'emps_filter':emps_filter
    }

    response = self.client.get(reverse('emp_app:index')) #trae el response
    question= get_object_or_404(Question, pk=question_id) #OBTIENE el resultado de consulta sino 404

    #param 1:request, param 2:vista, param 3:contexto
    return HttpResponse('HELLO WORLD') #respuesta HTTP
    return HttpResponseRedirect(reverse("polls:results",args=(question.id, ))) #USAR PARA FORMULARIOS
    return render(request,'index.html',context) #IMPRIME LA VISTA INDEX.HTML

#siempre que se pueda usar generic views
#GENERIC VIEW  https://platzi.com/clases/2694-django/45284-implementando-generic-views-en-la-aplicacion/
class IndexView(generic.Listview):
    template_name = 'vista'
    context_object_name= 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()
    
# FORMULARIO
def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Exception! Operation failed')
    
# FORMULARIO PLATZI https://platzi.com/clases/2694-django/45281-creando-la-vista-vote/
def form_platzi(request, question_id):
    question= get_object_or_404(Question, pk=question_id) #OBTIENE LA PREGUNTA
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist): #SI EL FORMULARIO ESTA INCOMLETO
        return render(request, "polls/detail.html", { #REDIRECCIONA CON MENSAJE DE ERROR
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:                                   #SI EL FORMULARIO ESTA COMPLETO
        selected_choice.votes += 1 #SE SUMA UN VOTO
        selected_choice.save() #SE GUARDA EN LA BD
        return HttpResponseRedirect(reverse("polls:results",args=(question.id, )))