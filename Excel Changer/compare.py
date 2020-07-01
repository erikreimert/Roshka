import csv, xlrd

def compare(src, src2):
    src = 'C:/Users/erikr/github/Roshka/Excel Changer/data/01-07-2020_15-12-06.csv'
    src2 = 'C:/Users/erikr/github/Roshka/Excel Changer/BrosCo Original/01-07-2020_15-12-06.xls'

    ### BrosCo info and open
    book = xlrd.open_workbook(src2)
    sheet = book.sheet_by_index(0)
    fin = sheet.nrows -1
    brosco = []
    bancop = []
    ### Bancop info and open
    with open(src, 'r') as file:
        bancopCsv = csv.reader(file)
        next(file)

        for row in bancopCsv:
            insert = int(row[1])
            bancop.append(insert)

    missing = []
    brosco.sort()
    for x in range(1, fin):
        ahh = sheet.row_values(x)
        insert = int(ahh[0])
        brosco.append(insert)
        if (brosco[x-1] in bancop):
            continue
        else:
            missing.append(brosco[x-1])

    print(missing)
if __name__ == "__main__":
    compare('ah', 'ah')
