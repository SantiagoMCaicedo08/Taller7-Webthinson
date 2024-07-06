from django.shortcuts import render, get_object_or_404, redirect
from .models import Tipodocumento, Persona
from .forms import PersonaForm, TipodocumentoForm
from rest_framework import generics
from .serializers import TipodocumentoSerializer

class TipodocumentoListCreate(generics.ListCreateAPIView):
    queryset = Tipodocumento.objects.all()
    serializer_class = TipodocumentoSerializer

def index(request):
    personas = Persona.objects.all()
    return render(request, 'main_app/index.html', {'personas': personas})

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()
    return render(request, 'main_app/persona_form.html', {'form': form})

def persona_detail(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'main_app/persona_detail.html', {'persona': persona})

def tipodocumento_create(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    if persona.tipodocumento:
        return redirect('persona_detail', pk=persona_id)
    if request.method == 'POST':
        form = TipodocumentoForm(request.POST)
        if form.is_valid():
            tipodocumento = form.save()
            persona.tipodocumento = tipodocumento
            persona.save()
            return redirect('persona_detail', pk=persona_id)
    else:
        form = TipodocumentoForm()
    return render(request, 'main_app/tipodocumento_form.html', {'form': form, 'persona_id': persona_id})

def tipodocumento_update(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    tipodocumento = persona.tipodocumento
    if not tipodocumento:
        return redirect('tipodocumento_create', persona_id=persona_id)
    if request.method == 'POST':
        form = TipodocumentoForm(request.POST, instance=tipodocumento)
        if form.is_valid():
            form.save()
            return redirect('persona_detail', pk=persona_id)
    else:
        form = TipodocumentoForm(instance=tipodocumento)
    return render(request, 'main_app/tipodocumento_form.html', {'form': form, 'persona_id': persona_id})

def tipodocumento_delete(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    tipodocumento = persona.tipodocumento
    if request.method == 'POST':
        tipodocumento.delete()
        persona.tipodocumento = None
        persona.save()
        return redirect('persona_detail', pk=persona_id)
    return render(request, 'main_app/tipodocumento_confirm_delete.html', {'tipodocumento': tipodocumento, 'persona_id': persona_id})
