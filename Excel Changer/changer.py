import xlrd, csv, os, glob, shutil, compare, mover

from datetime import date,datetime

#le saca los '' demas a los row en el xls
def cleanCell(ahh, y):

    #saca las celdas vacias entre las que importan
    for x in ahh:
        if x == '':
            ahh.pop(ahh.index(x))
    #por alguna razon no detecta todas las celdas vacias... Bancop es un desastre con sus excel
    ahh.pop(3)
    ahh.pop(3)
    ahh.pop(4)

    #le saco los puntos por que no entiende que en Paraguay se usa el punto y coma al revez con numeros
    num = ahh[4].split('.')
    ahh[4] = ''.join(num)
    num = ahh[3].split('.')
    ahh[3] = ''.join(num)
    rompebola = ahh[5].split('.')
    num2 = ''.join(rompebola)
    ahh[5] = num2

    #Cambia los valores de las celdas vacias que intercalan entre Debe y Haber con 0
    if y > 5:
        ahh[1] = int(ahh[1])
        if ahh[3] == '':
            ahh[3] = 0
            ahh[4] = int(ahh[4])
        elif ahh[4] == '':
            ahh[4] = 0
            ahh[3] = int(ahh[3])
        else:
            ahh[3] = int(ahh[3])
            ahh[4] = int(ahh[4])
        ahh[5] = int(ahh[5])

    return ahh

def adapt(path, fechaini, fechafin):

    #abre el archivo con xlrd
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    #consigue el largo del xls file
    fin = sheet.nrows

    today = date.today()

    ################################
    ####consigue la fecha para nombrar el archivo
    dia = today.strftime("%d-%m-%Y")
    hora = str(datetime.now().time())
    hora = hora.split('.')
    hora = hora[0]
    hora = hora.split(":")
    hora ='-'.join(hora)
    ###############################

    #nombre del archivo
    f = 'data/' + dia + '_'+ hora + '.csv'

    #esribe el nuevo archivo arreglado de bancop
    with open(f, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #escribe las celdas con informacion y hace skip las que pongan la tabla titular
        for x in range(5, fin):
            ahh = sheet.row_values(x)
            if x > 5 and ahh[1] == 'FECHA':
                continue
            filewriter.writerow(cleanCell(ahh, x))

    #ver que hace en mover.py
    fin = mover.move2(f)
    name3 = fechaini + fechafin
    #ver que hace en compare.py
    compare.compare(fin[0],fin[1], name3)
