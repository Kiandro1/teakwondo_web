from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from users.models import Practicing
from users.forms import PracticingForm

def practicing_list(request):
    practicing = Practicing.objects.filter(is_active = True)
    context = {
        'practicing':practicing,
    }
    return render(request, 'users/practicing_list.html', context=context)

def practicing_create(request):
    if request.method == 'GET':
        context = {
            'form': PracticingForm()
        }

        return render(request, 'users/practicing_create.html', context=context)

    elif request.method == 'POST':
        form = PracticingForm(request.POST)
        if form.is_valid():
            Practicing.objects.create(
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                phone_number = form.cleaned_data['phone_number'],
                email = form.cleaned_data['email'],
            )
            context = {
                'message': 'Alumno/a creado'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PracticingForm()
            }
        return render(request, 'users/practicing_list.html', context=context)


def practicing_update(request, pk):
    practicing = Practicing.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': PracticingForm(
                initial={
                    'name':practicing.name,
                    'address':practicing.address,
                    'phone_number':practicing.phone_number,
                    'email':practicing.email,
                }
            )
        }

        return render(request, 'users/practicing_update.html', context=context)

    elif request.method == 'POST':
        form = PracticingForm(request.POST)
        if form.is_valid():
            practicing.name = form.cleaned_data['name']
            practicing.address = form.cleaned_data['address']
            practicing.phone_number = form.cleaned_data['phone_number']
            practicing.email = form.cleaned_data['email']           
            practicing.save()
            
            context = {
                'message': 'Alumno/a actualizado'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PracticingForm()
            }
        return render(request, 'users/practicing_update.html', context=context)


class PracticingDeleteView(DeleteView):
    model = Practicing
    template_name = 'users/practicing_delete.html'
    success_url = '/users/practicing-list/'


# Create your views here.
