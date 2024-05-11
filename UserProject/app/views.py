from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def usermodel(request):
    EUMO=UserModel()
    d={'EUMO':EUMO}
    if request.method == 'POST':
        UFDO=UserModel(request.POST)
        if UFDO.is_valid():
            pw=UFDO.cleaned_data.get('password')
            MUFO=UFDO.save(commit=False)
            MUFO.set_password(pw)
            MUFO.save()
            
    return render(request ,'usermodel.html',d)