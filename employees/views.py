from django.shortcuts import render, redirect, get_object_or_404
from .models import Employees
from .forms import EmployeeAdder
from samples.decorators import custom_login_required
from django.core.paginator import Paginator


def employees(request):
    queryDataAll = Employees.objects.all()
    paginator = Paginator(queryDataAll, 5)  # 5 próbek na stronę

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'AllEmployees': queryDataAll,
        'page_obj': page_obj
    }
    return render(request, 'empl/employees.html', context)


@custom_login_required
def employee_add(request):

    form = EmployeeAdder()

    if request.method == 'POST':
        form = EmployeeAdder(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {"EmployeeAdder": form}

    return render(request, 'empl/employee-add.html', context)


@custom_login_required
def employee_update(request, employee_id):

    employee = get_object_or_404(Employees, employee_id=employee_id)
    form = EmployeeAdder(instance=employee)

    if request.method == 'POST':

        form = EmployeeAdder(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
            form = EmployeeAdder(instance=employee)

    context = {"EmployeeUpdate": form}

    return render(request, 'empl/employee-update.html', context)


@custom_login_required
def employee_delete(request, employee_id):

    employee = get_object_or_404(Employees, employee_id=employee_id)

    if request.method == 'POST':
        employee.delete()

        return redirect('employees')
    context = {"first_name": employee.first_name,
               "last_name": employee.last_name}
    return render(request, 'empl/employee-delete.html', context)
