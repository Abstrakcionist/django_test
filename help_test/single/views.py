from django.shortcuts import render
from .forms import InputsForm
from .word import document_builder


def index(request):
    # создание массива с информацией из формы
    user_information = []
    error = ''
    if request.method == 'POST':
        form = InputsForm(request.POST)
        if form.is_valid():
            # сохранение в базу данных
            form.save()

            # добавление данных из полей в массив
            user_information.append(form.cleaned_data.get('username'))
            user_information.append(form.cleaned_data.get('date_of_birth'))
            user_information.append(form.cleaned_data.get('info'))

            # запуск функции по созданию ворд документа
            document_builder(user_information)
        else:
            error = 'Что то не так'

    form = InputsForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'single/index.html', data)
