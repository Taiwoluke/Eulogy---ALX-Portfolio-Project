from django.shortcuts import render, redirect
from .models import Memory
from . import forms

def memory_log(request):
    memories = Memory.objects.all().order_by('-date')
    return render(request, 'memory_log/memory_log.html',{ 'memories' : memories })

def memory_page(request, slug):
    memory = Memory.objects.get(slug=slug)
    return render(request, 'memory_log/memory_pager.html',{ 'memory' : memory })

def log_memory(request):
    if request.method == 'POST':
        form = forms.CreateMemory(request.POST, request.FILES)
        newmemory = form.save(commit=False)
        newmemory.save()
        return redirect('memorials:memories')
    else:
        form = forms.CreateMemory()
    return render(request, 'memory_log/log_memory.html', { 'form': form})
