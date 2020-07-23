from django.shortcuts import render, redirect
from myapp.program.downloadbot import bot
from threading import Thread
import os, glob, mimetypes

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
        return consolidacion2fa_post(request)
    elif request.method == "GET":
        return consolidacion2fa_get(request)

        ############DEBERIA PODER BORRAR ESTO PERO NO ME DEJA
    # return render(request, 'consolidacion/consolidacion2fa.html')

def consolidacion2fa_post(request):
    twofa = request.POST.get('twofa')

    if twofa != None:
        auth_file = open('2fa.txt', 'w+')
        auth_file.write(twofa)
        auth_file.close()
        time.sleep(.01)
        os.remove('2fa.txt')
        return redirect("/download")

def consolidacion2fa_get(request):
    return render(request, 'consolidacion/consolidacion2fa.html')

def download(request):
    # if request.method == "POST":
    #     return download_post(request)
    # elif request.method == "GET":
    #     return download_get(request)
    items = dicter(request)
    return render(request, 'consolidacion/download.html', {'items' : items})


# def download_post(request):
#     bancop = request.POST.get('bancop')
#     Consolidado = request.POST.get('Consolidado')
#     BrosCo = request.POST.get('BrosCo')
#     bancopOG = request.POST.get('Bancop_Original')
#
#     list =[bancop, Consolidado, BrosCo, bancopOG]
#     src = {
#     1: 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/data/',
#     2: 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/BrosCo_Si_Bancop_No/',
#     3: 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/BrosCo_Original/',
#     4: 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/Bancop_Original/'
#     }
#     i = 0
#     for x in list:
#         i+=1
#         if x != None:
#             fpath = src.get(i)
#             fl = open(fpath, 'r')
#             mime_type, _ = mimetypes.guess_type(fpath)
#             response = HttpResponse(fl, content_type=mime_type)
#             response['Content-Disposition'] = "attachment; x=%s" % x
#             return response
#
# def download_get(request):
#     items = dicter(request)
#     return render(request, 'consolidacion/download.html', {'items' : items})

def lister(src):
    dir =  glob.glob(src)
    list = []
    for x in dir:
        item = x.split('\\')
        item = item[1]
        list.append(item)
    return list
def dicter(request):
    bancop = lister('C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/data/*')
    brosco = lister('C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/BrosCo_Original/*')
    consolidado = lister('C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/BrosCo_Si_Bancop_No/*')
    bancop_og = lister('C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/Bancop_Original/*')
    request.session['bancopList'] = bancop
    request.session['broscoList'] = brosco
    request.session['consolidadoList'] = consolidado
    request.session['bancop_ogList'] = bancop_og
    items = {
    'bancopList' : request.session['bancopList'],
    'broscoList' : request.session['broscoList'],
    'consolidadoList' : request.session['consolidadoList'],
    'bancop_ogList' : request.session['bancop_ogList'],
    }
    return items
