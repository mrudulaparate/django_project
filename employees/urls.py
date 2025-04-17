from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/remove/<int:id>/', views.remove_employee, name='remove_employee'),
    path('employees/search/', views.search_employee, name='search_employee'),
]
