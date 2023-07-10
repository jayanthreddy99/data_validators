from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def sf(request):
    SFO = StudentForms()
    d = {'SFO':SFO}
    if request.method == 'POST':
        SFD = StudentForms(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('invalid Data')
    return render(request,'sf.html',d)