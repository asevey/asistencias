from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import Persona,CuentaBancaria

from .forms import BancoForm,PersonaForm

# Create your views here.

def banco_create(request):
    nuevo_banco = None
    if request.method == 'POST':
        banco_form = BancoForm(request.POST)
        if banco_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_banco = banco_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente la cuenta bancaria {}'.format(nuevo_banco))
            return redirect(reverse('persona:lista_banco', args={nuevo_banco.id}))
    else:
        banco_form = BancoForm()

    return render(request, 'persona/banco_form.html',
                  {'form': banco_form})


def persona_create(request):
    nueva_persona = None
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_persona = persona_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nueva_persona))
            return redirect(reverse('persona:lista_persona'))
    else:
        persona_form = PersonaForm()

    return render(request, 'persona/persona_form.html',
                  {'form': persona_form})


def persona_lista(request):
    personas = Persona.objects.all()
    return render(request, 'persona/listarPersonas.html',
                  {'personas': personas})


def lista_banco(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    cuenta=get_object_or_404(CuentaBancaria, pk=pk)
    return render(request,'persona/listaBanco.html',
                  {'persona': persona,'cuenta':cuenta})