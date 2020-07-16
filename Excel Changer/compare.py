import csv, xlrd

def compare(name, name2, name3):
    src = 'C:/Users/erikr/github/Roshka/Excel Changer/data/' + name
    src2 = 'C:/Users/erikr/github/Roshka/Excel Changer/BrosCo Original/' + name2
    want = 'C:/Users/erikr/github/Roshka/Excel Changer/BrosCo Si Bancop No/' + 'Consolidacion ' + name3
    ### BrosCo info and open
    book = xlrd.open_workbook(src2)
    sheet = book.sheet_by_index(0)
    fin = sheet.nrows
    brosco = []
    bancop = []
    # missing = []
    ### Bancop info and open
    with open(src, 'r') as file:
        bancopCsv = csv.reader(file)
        next(file)

        #Conseguir los ID de bancop y poner en una lista
        for row in bancopCsv:
            insert = int(row[1])
            bancop.append(insert)
    #escribe archivo con las tablas que no estan en Bancop
    with open(want, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(sheet.row_values(0))

        #compares item per item en BrosCo a Bancop, si hay equivalente en bancop se ignora
        # si no se pone en un excel nuevo
        for x in range(1, fin):
            ahh = sheet.row_values(x)
            insert = int(ahh[0])
            brosco.append(insert)
            if (brosco[x-1] in bancop):
                continue
            else:
                # missing.append(brosco[x-1])
                #si no esta en bancop copia la linea de Brosco en un nuevo archivo
                filewriter.writerow(ahh)

    # print(brosco)
    # print(missing)
    print("Archivo Procesado")
if __name__ == "__main__":
    src = input()
    src2 = input()
    compare(src, src2)
