from django.shortcuts import render
import myapp.program.downloadbot
import threading
from multiprocessing import Process,Pipe

# import os, threading
# import subprocess
# Create your views here.

flag = True
twofa = None
#2fa pipe
def f(child_conn):
    msg = twofa
    child_conn.send(msg)
    child_conn.close()

#flag Pipe
def g(child_conn):
    msg = flag
    child_conn.send(msg)
    child_conn.close()


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
        if ruc != None:
            twofa = request.POST.get('twofa')

            #input para el downloadbot
            bot = 'py downloadbot.py ' + ruc + ' ' + cedula + ' ' + pword + ' ' + option + ' ' + fechain + ' ' + fechafin
            # proc = subprocess.Popen(bot, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            threading.Thread(target=downloadbot.bot(),args=(cedula,pword,ruc,option, fechain, fechafin))

            # output = process.stdout
            # print(output)
            # os.system('ahh')

            if twofa != None:

                flag = False

                # putamadre = "b'" + twofa + "\n'"
                # proc.communicate(putamadre)
                # proc.stdin.write(putamadre)
                # proc.stdin.flush()
                # os.system('%s'%(twofa))

    return render(request, 'consolidacion/consolidacion.html')
