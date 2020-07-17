from django.shortcuts import render
import os, threading
import subprocess
# import downloadbot
# Create your views here.
def upload(request):

    if request.method == "POST":
        ruc = request.POST.get('ruc')
        cedula = request.POST.get('user')
        pword = request.POST.get('pword')
        pword = str(pword)
        option = request.POST.get('2fa')
        fechain = request.POST.get('ini')
        fechafin = request.POST.get('fin')
        #para que abra el downloadbot
        if ruc != '':
            twofa = request.POST.get('twofa')
            os.system('cd.. & py downloadbot.py %s %s %s %s %s %s' %(ruc, cedula, pword, option, fechain, fechafin))
            # process = subprocess.run(['ls','-lha'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
            # output = process.stdout
            # print(output)
            os.system('ahh')
            if twofa != '':
                os.system('%s'%(twofa))

    return render(request, 'consolidacion/consolidacion.html')
