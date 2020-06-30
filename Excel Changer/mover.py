import glob, os, shutil, changer

def move():
    source_dir = 'C:/Users/erikr/Downloads'
    dst = 'C:/Users/erikr/github/Roshka/Excel Changer/data/'

    #consigue los archivos de la carpeta de descarga
    files = glob.iglob(os.path.join(source_dir, "*.xls"))

    ## Prepara el numero y le anexa al source para mover a la carpeta deseada
    num = len([name for name in os.listdir(dst) if os.path.isfile(os.path.join(dst, name))])
    num+=1
    num = str(num) + '.xls'
    name = source_dir + '/' + num

    #mueve y renombra el archivo
    for file in files:
        os.rename(file, name)
        if os.path.isfile(name):
            shutil.move(name, dst)

    return 'data/' + num

if __name__ == "__main__":

    path = move()
    changer.adapt(path)
