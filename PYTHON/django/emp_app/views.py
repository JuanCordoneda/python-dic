'CREA LAS VISTAS'
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse #ESTO PERMITE GENERAR UN RESPUESTA HTTP
from .models import Employee,Role,Department
from django.db.models import Q

# EL INDEX
def index(request):
#    return HttpResponse('HELLO WORLD') #respuesta HTTP
    return render(request,'index.html') #IMPRIME LA VISTA INDEX.HTML

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    
    return render(request,'viewall_emp.html',context    )

def add_emp(request):
    
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
    
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Susccessfully")
        except:
            return HttpResponse("Please enter a valid Emp ID")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = (request.POST['dept'])
        role = (request.POST['role'])
        emps = Employee.objects.all()
        if first_name:
            emps = emps.filter(Q(first_name__icontains = first_name))
        if last_name:
            emps = emps.filter(Q(last_name__icontains = last_name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__contains = role)
            
        context = {
           'emps' : emps 
        }
        return render(request,'viewall_emp.html',context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')
        
    return render(request,'filter_emp.html')
