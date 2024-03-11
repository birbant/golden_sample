from django.shortcuts import render, redirect, get_object_or_404
from .forms import SamplesAdder
from .models import Samples
from .decorators import custom_login_required
from django.core.paginator import Paginator


def homepage(request):
    return render(request, 'samp/homepage.html')


def samples(request):

    queryDataAll = Samples.objects.all()
    paginator = Paginator(queryDataAll, 5)  # 5 próbek na stronę

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    approved = Samples.objects.filter(status='Approved').count()
    not_approved = Samples.objects.filter(status='Not approved').count()

    context = {
        'AllSamples': queryDataAll,
        'approved': approved,
        'not_approved': not_approved,
        'page_obj': page_obj
    }

    return render(request, 'samp/samples.html', context)


@custom_login_required
def sample_add(request):
    form = SamplesAdder()

    if request.method == 'POST':
        form = SamplesAdder(request.POST)

        if form.is_valid():
            form.save()
            return redirect('samples')

    context = {"SamplesAdder": form}

    return render(request, 'samp/sample-add.html', context)


@custom_login_required
def sample_update(request, part_number):

    sample = get_object_or_404(Samples, part_number=part_number)
    form = SamplesAdder(instance=sample)

    if request.method == 'POST':

        form = SamplesAdder(request.POST, instance=sample)

        if form.is_valid():
            form.save()
            # messages.success(request, 'Sample updated successfully!')
            return redirect('samples')
        else:
            form = SamplesAdder(instance=sample)

    context = {"SampleUpdate": form}

    return render(request, 'samp/sample-update.html', context)


@custom_login_required
def sample_delete(request, part_number):

    sample = get_object_or_404(Samples, part_number=part_number)

    if request.method == 'POST':
        sample.delete()

        return redirect('samples')
    context = {"part_number": part_number,
               "part_name": sample.part_name}
    return render(request, 'samp/sample-delete.html', context)
