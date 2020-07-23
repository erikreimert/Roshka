from django.shortcuts import render, redirect
from myapp.program.downloadbot import bot
from threading import Thread
from datetime import datetime
import os, time

# Create your views here.

#Landing Page para Consolidcaciones
def consolidacion(request):
    if request.method == "POST":
            return consolidacion_post(request)
    elif request.method == "GET":
        return consolidacion_get(request)


def consolidacion_post(request):
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

        t = Thread(group=None, target=bot, name=None, args=(cedula,pword,ruc,option, fechain, fechafin,), kwargs={}, daemon=None)

        t.start()

        return consolidacion2fa(request)

def consolidacion_get(request):
    return render(request, 'consolidacion/consolidacion.html')

#Page para la parte 2fa de Consolidaciones
def consolidacion2fa(request):

    if request.method == "POST":
        consolidacion2fa_post(request)
    elif request.method == "GET":
        return consolidacion2fa_get(request)

        ############DEBERIA PODER BORRAR ESTO PERO NO ME DEJA
    return render(request, 'consolidacion/consolidacion2fa.html')

def consolidacion2fa_post(request):

    twofa = request.POST.get('twofa')

    if twofa != None:
        auth_file = open('2fa.txt', 'w+')
        auth_file.write(twofa)
        auth_file.close()
        time.sleep(10)
        os.remove('2fa.txt')
        return render(request, 'consolidacion/test-session.html')

def consolidacion2fa_get(request):
    return render(request, 'consolidacion/consolidacion2fa.html')

def download(request):
    return render(request, 'consolidacion/download.html')
##################################################################
#TESTING
def test_session(request):
    if request.method == "POST":
        return test_session_post(request)
    elif request.method == "GET":
        return test_session_get(request)

def test_session_get(request):
    return render(request, 'consolidacion/test-session.html')

def test_session_post(request):
    person_name = request.POST['t']
    person_created = datetime.now()
    request.session['person_name'] = person_name
    request.session['person_created'] = person_created.timestamp()
    return redirect("/test-session-result")

def test_session_result(request):
    return render(request, 'consolidacion/test-session-result.html', {
        'person_name': request.session['person_name'],
        'person_created': request.session['person_created'],
    })
#################################################################
