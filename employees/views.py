from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse

# Home page with buttons
def home(request):
    return render(request, 'employees/home.html')

# View all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# Add a new employee
def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        salary = request.POST['salary']
        email = request.POST['email']
        Employee.objects.create(name=name, position=position, salary=salary, email=email)
        return redirect('employee_list')
    return render(request, 'employees/add_employee.html')

# Remove an employee
def remove_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
    except Employee.DoesNotExist:
        pass
    return redirect('employee_list')

# Search for an employee by name
def search_employee(request):
    if request.method == 'POST':
        query = request.POST['search']
        employees = Employee.objects.filter(name__icontains=query)
        return render(request, 'employees/search_employee.html', {'employees': employees})
    return render(request, 'employees/search_employee.html')
