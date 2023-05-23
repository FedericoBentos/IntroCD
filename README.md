# IntroCD
Repositorio vinculado a la Materia Introducción a la Ciencia de Datos (2023)

En este repositorio se encuentra el archivo "shakespeare_propuesta.pdf", que contiene el informe de la Entrega 1 respecto a la Materia (FING MCDAA-IntroCD).

El mismo es creado a partir de correr la siguiente instrucción:
**_"jupyter nbconvert --to pdf --template hidecode shakespeare_propuesta.ipynb"_**

Se crea a partir del mismo Notebook de Jupyter que fue entregado por los Docentes, el mismo fue editado y la metada de las celdas contienen un codigo json que le indica si se debe imprimir el input y el output de la celda del Notebook. Para ello se utiliza un template (carpeta hidecode) que debe ser incluido en el entorno virtual: **_"...\intro-cd\.venv\share\jupyter\nbconvert\templates"_**.
Dicha carpeta permite con el siguiente código en la metadata de la celda:
<code>
{
  "nbconvert": {
    "show_code": false
  }
}
</code>
impedir que se imprima a Latex/PDF en el informe dicha celda (tanto Input como Output). El template fue realizado a partir del template de la libreria **_nbconvert_** llamado **_"latex"_** editando el bucle que recorre las celdas con un If que controla si se encuentra dicho código en la metadata de la celda del Jupyter Notebook.

Las librerias utilizadas en el entorno virtual se encuentran en el archivo "requirements.txt" contenido en la branch main de este repositorio.
