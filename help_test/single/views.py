from django.shortcuts import render
from .models import Inputs
from .forms import InputsForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = InputsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'FY'

    form = InputsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'single/index.html', data)
