import xlrd, csv, os, glob, shutil
from datetime import date,datetime

#le saca los '' demas a los row en el xls
def cleanCell(ahh):
    for x in ahh:
        if x == '':
            ahh.pop(ahh.index(x))
    ahh.pop(3)
    ahh.pop(3)
    ahh.pop(4)

    #cuando se cambia del xls al csv toma el 6.000 y le hace 6, esto le hace 6000, lo mismo con los otros numeros
    num = ahh[4].split('.')
    ahh[4] = ''.join(num)
    num = ahh[3].split('.')
    ahh[3] = ''.join(num)
    rompebola = ahh[5].split('.')
    num2 = ''.join(rompebola)
    ahh[5] = num2
    # print(ahh)
    # for x in range(1,5):
    #     fix = ahh[x].split("'")
    #     print(fix[0])
    #     ahh[x] = fix[1]

    return ahh

def adapt(path):

    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

# ####################################    Nombres y detalles de la cuenta
#     # read a cell
#     tituloV = sheet.cell(0,2)
#     titulo = tituloV.value
#
#     hsV = sheet.cell(1,5)
#     hs = hsV.value
#
#     cuentaV = sheet.cell(2,4)
#     cuenta = cuentaV.value
#
#     denominacionV = sheet.cell(3,4)
#     denominacion = denominacionV.value
#
#     monedaV = sheet.cell(4,4)
#     moneda = monedaV.value
#
#     tipoV = sheet.cell(2,13)
#     tipo = tipoV.value
#
#     saldoActualV = sheet.cell(3,13)
#     saldoActual =saldoActualV.value
# #####################################

    #consigue el largo del xls file
    fin = sheet.nrows -1

    today = date.today()

    # d1 = today.strftime("%d/%m/%Y")

    dia = today.strftime("%d-%m-%Y")
    hora = str(datetime.now().time())
    hora = hora.split('.')
    hora = hora[0]
    hora = hora.split(":")
    hora ='-'.join(hora)

    f = 'data/' + dia + '_'+ hora + '.csv'

    with open(f, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # filewriter.writerow(['', titulo])
        # filewriter.writerow(['', '', hs])
        # filewriter.writerow(['', 'Cuenta:', cuenta, 'Tipo:', tipo])
        # filewriter.writerow(['', 'Denominacion', denominacion,"Saldo Actual", saldoActual])
        # filewriter.writerow(['', 'Moneda', moneda])
        #limpia el xls y escribe la parte importante del xls
        for x in range(5, fin):
            ahh = sheet.row_values(x)
            filewriter.writerow(cleanCell(ahh))

    print("Archivo Procesado")


    src = 'C:/Users/erikr/github/Roshka/Excel Changer/data'
    dst = 'C:/Users/erikr/github/Roshka/Excel Changer/Bancop Original/'
    files = glob.iglob(os.path.join(src, "*.xls"))
    n = f.split('.')
    name = n[0] + '.xls'
    for file in files:
        os.rename(file, name)
        if os.path.isfile(name):
            shutil.move(name, dst)

if __name__ == "__main__":
     path = input()
     adapt(path)
