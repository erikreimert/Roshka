Web app para Consolidaciones y storage de archivos consolidados y de donde se saco las Consolidaciones

--Hosteado en django, programado en Python3, js y html
--Modulos que se tienen que descargar para Python3
-xlrd, Selenium, Django, pyvirtualdisplay

--Upgrades
  Para agregar mas coperativas simplemente entre al archivo consolidacion.html y agregue una nueva opcion al SELECT que esta en la seccion de opciones de brosco. Ponga de valor las indices de la coperativa como esta en el servidor de produccion, por ej. el valor de Comecipar seria MECI y luego ponga el nombre de la corporativa como la opcion.

  Si se quiere crear nuevas carpetas para tener a las diferentes coperativas en lugares diferentes recomiendo tomar el input que haran arriba para el link y pasarlo a todas las funciones para nombrar los archivos con su coperativa.  De ahi no seria extremadamente complicado separar esos archivos por nombre.

  Si quieren editar el path de los directorios en el codigo lo podran hacer en una sola linea si lo editan en myapp/program/folders.py, ese archivo sirve como un database de los path que es impoortado por todos los otros archivos.

  Tambien recomendaria redisenhar la pagina downloads.html, ahora mismo no es muy ergonomica

  En statics esta el CSS de las paginas por si quieren cambiarlos a algo mas atractivo/eficiente

  En downloadbot.py hay una segunda opcion en bot2 para la espera de descarga. No estoy 100% seguro que funcione pero si alguien quiere explorarla seria probablemente la mejor opcion en cuanto a esperar a la descarga de los archivos

  En downloadbot.py no estaria mal agregar una forma de detectar cuando el input del usuario del 2fa tarda demasiado por que la pagina de bancop tira un input de reenvio si tarda mucho y eso crashea la pagina. Entonces estaria bueno tener una forma de detectar eso y borrar ese input para que reenvie el 2fa o inclusive para que pase el input a traves de la pagina al usuario para que lo decida desde la pagina de 2fa.

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

-Archivos se quedan en la carpeta de descargas
  El programa escanea la carpeta de descargas luego de descargar los dos archivos (Bancop y Brosco), en la forma que esta integrada no deberia NUNCA haber archivos en la carpeta de descarga (que sean .xls o .xlsx). Si falla la aplicacion a la mitad, o va la luz, o alguna especie de error ocurre y archivos quedan en la carpeta de descargas (que sean de tipo .xls o .xlsx) esto confundiria a la aplicacion y posiblemente haga que las consolidaciones no ocurran correctamente. Esto es de alto riesgo

-Archivos descargados del servidor Brosco dejan de tener la palabra Brosco en el nombre del archivo
  La forma que detecta el programa si el xlsx es de brosco es leyendo los nombres de los archivos, esto esta en mover.py, si se cambian los nombres de los archivos porfavor actualizar eso en mover.py
