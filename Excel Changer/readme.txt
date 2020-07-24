Web app para Consolidaciones y storage de archivos consolidados y de donde se saco las Consolidaciones

--Hosteado en django
--Modulos requeridos para Python3
-xlrd, csv, glob, shutil, threading, time, os, Selenium

--Upgrades
  Si se quiere agregar una opcion para distintas o mas coperativas se tendra que editar el html de consolidacion.html para que tenga ese input,
    views.py para que mande ese input a downloadbot.py y la funcion bot() para que tome ese input y se lo pase a la funcion bot2() (tambien se tendra que editar el link en bot2() para que se agregue la coperativa deseada al link)

  Si se quiere crear nuevas carpetas para tener a las diferentes coperativas en lugares diferentes recomiendo tomar el input que haran arriba para el link y pasarlo a todas las funciones para nombrar los archivos con su coperativa. De ahi no seria extremadamente complicado separa esos archivos por nombre.

  En statics esta el CSS de las paginas por si quieren cambiarlos a algo mas atractivo/eficiente

  Seria una buena idea poner una traba en mover.move() para que no ejecture hasta que note que hay dos archivos en la carpeta de descarga

--Como correr
  Ir al url de descargas '/download/' si se quiere simplemente acceder a los archivos previamente consolidados
  Ir al url de consolidaciones '/consolidacion/' si se quiere conseguir nuevos archivos consolidados. Al llegar ahi llene los inputs requeridos y espere

--Como corre
  Al llenar el input de '/consolidacion/' un thread es inicializado que corre download.py. Ese script abre dos instancias de selenium, una que descarga los arhivos de la cuenta de BrosCo en bancop y otro que descarga los archivos del servidor en Brosco. Luego corre otro script que mueve esos archivos (mover.py) de la carpeta de descargas a donde deben permanecer en el servidor. Luego, el archivo de bancop es editado por un script (changer.py) ya que el archivo de Bancop tiene muy mala estructura y es inusable en su estado post-descarga. Luego se consolida el archivo de bancop (con el script compare.py) con el de brosco y se crea un nuevo archivo con las diferencias (Brosco - Bancop). Todos estos archivos luego son visibles en los drop down menus en '/download/' y se pueden descargar del servidor.

--Posibles futuros problemas
-Bancop actualiza su pagina:
  Va tener que reconfigurarse el downloadbot

-Bancop actualiza su archivo
  Si el archivo de bancop deja de ser tan caca posiblemente se va a poder utilizar sin changer.py y pasarlo directo a compare.py
