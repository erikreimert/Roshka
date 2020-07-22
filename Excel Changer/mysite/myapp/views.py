from django.shortcuts import render, redirect
from myapp.program.downloadbot import bot
from threading import Thread
from myapp.twofaClass import twofaHold
from datetime import datetime

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
        if ruc != None:
            twofa = request.POST.get('twofa')
            Intermediary = twofaHold()

            #input para el downloadbot
            # botArg = 'py downloadbot.py ' + ruc + ' ' + cedula + ' ' + pword + ' ' + option + ' ' + fechain + ' ' + fechafin
            # print(bot)
            # proc = subprocess.Popen(bot, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Thread(group=None, target=bot(), name=None, args=(Intermediary,), kwargs={}, daemon=None)
            t = Thread(group=None, target=bot, name=None, args=(cedula,pword,ruc,option, fechain, fechafin,Intermediary,), kwargs={}, daemon=None)
            t.start()

            # output = process.stdout
            # print(output)
            # os.system('ahh')

            if twofa != None:

                Intermediary.set2fa(twofa)

                # putamadre = "b'" + twofa + "\n'"
                # proc.communicate(putamadre)
                # proc.stdin.write(putamadre)
                # proc.stdin.flush()
                # os.system('%s'%(twofa))

    return render(request, 'consolidacion/consolidacion.html')


def test_session_get(request):
    return render(request, 'consolidacion/test-session.html')


def test_session_post(request):
    person_name = request.POST['t']
    person_created = datetime.now()
    request.session['person_name'] = person_name
    request.session['person_created'] = person_created.timestamp()
    return redirect("/test-session-result")


def test_session(request):
    if request.method == "POST":
        return test_session_post(request)
    elif request.method == "GET":
        return test_session_get(request)


def test_session_result(request):
    return render(request, 'consolidacion/test-session-result.html', {
        'person_name': request.session['person_name'],
        'person_created': request.session['person_created'],
    })
