from django.shortcuts import render

# Create your views here.
def upload(request):
    if request.method == "POST":
        ruc = request.POST.get('ruc')
        cedula = request.POST.get('user')
        pword = request.POST.get('pword')
        twofa = request.POST.get('2fa')
        fechain = request.POST.get('ini')
        fechafin = request.POST.get('fin')
    return render(request, 'consolidacion/consolidacion.html')
