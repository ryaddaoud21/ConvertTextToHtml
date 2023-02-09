from django.shortcuts import render
from .forms import *



def home(request):
    form=EditorForm()
    context = {'form':form}
    return render(request,'HTML/home.html',context)