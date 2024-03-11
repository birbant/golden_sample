from django.shortcuts import render, redirect
from .models import SampleOperation
from .forms import SampleOperationAdder
from samples.decorators import custom_login_required
from django.core.paginator import Paginator


@custom_login_required
def sample_management(request):
    queryDataAll = SampleOperation.objects.all()
    paginator = Paginator(queryDataAll, 5)  # 5 próbek na stronę

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'Sample_management': queryDataAll,
               'page_obj': page_obj}
    return render(request, 'samp_mana/management.html', context)


@custom_login_required
def sample_manage_add(request):
    if request.method == 'POST':
        form = SampleOperationAdder(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management')
    else:
        form = SampleOperationAdder()
    context = {"SampleOperationAdder": form}
    return render(request, 'samp_mana/sample-mana-add.html', context)
