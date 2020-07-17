from django.shortcuts import render
import os

# Create your views here.
def upload(request):
    if request.method == "POST":
        ruc = request.POST.get('ruc')
        cedula = request.POST.get('user')
        pword = request.POST.get('pword')
        pword = str(pword)
        twofaoption = request.POST.get('2fa')
        fechain = request.POST.get('ini')
        fechafin = request.POST.get('fin')
        twofa = request.POST.get('twofa')
        print(ruc)
        print(twofa)
    return render(request, 'consolidacion/consolidacion.html')
