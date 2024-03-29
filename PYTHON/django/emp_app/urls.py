'ARCHIVO DE RUTAS DE NUESTRA APP, DESPUES TENES QUE IMPORTARLAS EN EL APIGATEWAY'
#https://platzi.com/clases/2694-django/45264-nuestro-primer-proyecto-premios-platzi-app-2/
from django.urls import path,include
from . import views #IMPORTA TODAS LAS VISTAS
from django.contrib import admin

#primer param = url
#segundo param = archivo
#tercer param = nombre
urlpatterns = [
    # path('',views.IndexView.as_view(),name="index"), #INDEX VIEW GENERIC VIEW
    path('',views.index,name="index"), #INDEX
    path('all_emp',views.all_emp,name="all_emp"),
    path('add_emp',views.add_emp,name="add_emp"),
    path('remove_emp',views.remove_emp,name="remove_emp"),
    path('remove_emp/<int:emp_id>',views.remove_emp,name="remove_emp"), #PASA POR URL UN INT remove_emp/1
    path('filter_emp',views.filter_emp,name="filter_emp"),
]
# http://127.0.0.1:8000/admin