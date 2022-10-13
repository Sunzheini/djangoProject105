from django import forms
from django.shortcuts import render
from djangoProject105.web.forms import PersonForm
from djangoProject105.web.models import Person


def index(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )
        else:
            pass
    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'index.html', context)







