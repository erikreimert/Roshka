import glob, os, shutil
from . import folders, changer

def move(fromd, to, corporativa):

    source_dir = folders.dl
    dst = folders.data
    dst2 = folders.BrosCo_Original

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
    changer.adapt(path, fromd, to, corporativa)

#renombrar archivos bancop para que tengan el mismo nombre que los archivos en data y lo mismo para archivos Brosco
def move2(f):
    src = folders.data
    dst = folders.Bancop_Original

    files = glob.iglob(os.path.join(src, "?.xls"))
    # n = f.split('.')
    name = f.replace('.csv', '.xls')
    for file in files:
        os.rename(file, name)
        if os.path.isfile(name):
            shutil.move(name, dst)
    src2 = folders.BrosCo_Original
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
if __name__ == '__main__':
    move('2020-07-01','2020-07-30', 'MECI')
