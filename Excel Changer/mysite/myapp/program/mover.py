import glob, os, shutil, changer

def move(fromd, to):
    source_dir = 'C:/Users/erikr/Downloads/'
    dst = 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/data/'
    dst2 = 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/BrosCo_Original/'

    #consigue los archivos de la carpeta de descarga
    files = glob.iglob(os.path.join(source_dir, "*.xls"))
    brosco = glob.iglob(os.path.join(source_dir, "*.xlsx"))

    ## Prepara el numero y le anexa al source para mover a la carpeta deseada
    num = len([name for name in os.listdir(dst) if os.path.isfile(os.path.join(dst, name))])
    num+=1
    num = str(num) + '.xls'
    name = source_dir + '/' + num

    #mueve y renombra el archivo a data y BrosCo_Original respectivamente
    for file in files:
        if 'movimientos' in file:
            os.rename(file, name)
            if os.path.isfile(name):
                shutil.move(name, dst)
    for file in brosco:
        if 'BrosCo' in file:
            os.rename(file, name)
            if os.path.isfile(name):
                shutil.move(name, dst2)
    path = dst + num
    changer.adapt(path, fromd, to)

#renombrar archivos bancop para que tengan el mismo nombre que los archivos en data y lo mismo para archivos Brosco
def move2(f):
    src = 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/data/'
    dst = 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/Bancop_Original/'

    files = glob.iglob(os.path.join(src, "?.xls"))
    # n = f.split('.')
    name = f.replace('.csv', '.xls')
    # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    # print(name)
    # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for file in files:
        os.rename(file, name)
        if os.path.isfile(name):
            shutil.move(name, dst)
    src2 = 'C:/Users/erikr/github/Roshka/Excel Changer/mysite/statics/BrosCo_Original/'
    brosco = glob.iglob(os.path.join(src2, "?.xls"))
    name2 = name.split('data/')
    name2 = name2[1]
    for file in brosco:
        os.rename(file, name2)
        if os.path.isfile(name2):
            shutil.move(name2, src2)
    fin1 = name2.replace('xls','csv')
    fin2 = name2

    return fin1,fin2
