# **Curso Básico de Django**
[![](https://crowdbotics.ghost.io/content/images/2019/05/django.png)](http://https://crowdbotics.ghost.io/content/images/2019/05/django.png)

# Editor.md

![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

- Instalar Django.
1. Debemos crear la carpeta donde trabajaremos:` mkdir django_premiosplatzi`
y nos dirigimos a la carpeta creada. 
2. Crear el entorno virtual con venv en Windows  `py -m venv venv`  y en linux` python3 -m venv venv`.
3. Activar entorno virtual Windows: `.\venv\Scripts\activite` y en linux `source venv/Scripts/activate` si por alguna razón no funciona utilice todo el link del donde se encuentra el activador Ej: `C:\Users\monbre\OneDrive\Escritorio\programación\premiosPlatzi\venv\Scripts\activate`
4. Instalar django: `pip install django`
5. Iniciar el repositorio de git: `git init`
6. Iniciar el proyecto de django: `django-admin startproject premiosplatziapp`
7. Para evitar llevar al repositorio remoto archivos innecesarios es importante crear el archivo:` .gitignore` (Donde se suele agregar la carpeta venv o archivos que no se desea subir al repositorio) para windows se crea con  `fsutil file createnew .gitignore 0` y linux `touch .gitignore`

7. Para que ignore la carpeta venv ingresamos al archivo .gitignore y colocamos `venv/` para que no lo suba a github

** Django Project Structure Best Practice 2022Django Project Structure Best Practice 2022**
![](https://studygyaan.com/wp-content/uploads/2019/07/Best-Practice-to-Structure-Django-Project-Directories-and-Files-1024x676.png?ezimgfmt=ngcb1/notWebP)

**Reference**: *Samyak. (2019, July 2). Django project structure best practice 2022. StudyGyaan. https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files*

### Contenido de las carpetas creadas por Django

- `manage.py `: Muestra los diferentes comandos disponibles para hacer que el proyecto funcione.
- `_init_.py` : Indica que la carpeta es un paquete que contiene los archivos de la aplicación web.
- `asgi.py / wsgi.py `: Sirven para hacer el despliegue de la aplicación.
- `settings.py` : Contiene toda la información de la configuración del proyecto como el lenguaje, la zona horaria, las bases de datos, etc.
- `urls.py` : Donde se trabajan las direcciones con las que nos podemos mover a través del proyecto como la ruta admin o user.

 ## El servidor de desarrollo

 Para iniciar el servidor remoto nos dirigimos a la carpeta `premiosPlatziapp` y lo iniciamos con el comando `py manage.py runserver`. 
 Al cargar el server nos da una dirección Ip o localhost http://127.0.0.1:8000/
 Nos muestra la siguiente página de inicio.
 ![](https://parzibyte.me/blog/wp-content/uploads/2019/04/4-Abrir-nuestra-primera-webapp-con-Django-en-el-navegador.png)

[Tutorial De Django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/ "Tutorial De Django")

### link de Django  File Structure
[http://https://techvidvan.com/tutorials/django-project-structure-layout/](http://https://techvidvan.com/tutorials/django-project-structure-layout/)

![](https://i1.wp.com/techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/06/Django-file-structure.jpg?fit=1200%2C628&ssl=1)

**Reference:**(*N.d.). Techvidvan.com. Retrieved April 28, 2023, from https://techvidvan.com/tutorials/django-project-structure-layout/*

## Primer Proyecto
Entramos a nuestro ambiente virtual como se explicó anteriormente y para crear otro proyecto se utiliza los comandos` py manage.py startapp polls` y en Linux `python3 manage.py startapp polls`, en visual encontramos ya el proyecto polls. 

Para comprobar su conexión nos dirigimos a la carpeta `polls` al archivo `views.py`y se agrega el siguiente código:

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world", 2+8)```

Luego nos dirigimos a la carpeta `urls.py` de premiosplatziapp y le agregamos a urlpatterns un nuevo path.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls"))
]```
Luego creamos la parpeta de `urls.py `en mi proyecto `polls`.

y en el archivo agregamos el siguiente código:
```Python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]```

Luego podemos agregar todos los archivos al `git con git add -A` y luego le damos un commit `git commit -a "Descripción"`

## ORM

Un ORM (Object-Relational Mapping) es una técnica que nos permite crear una Base de Datos Orientada a Objetos (virtual), que opera sobre la Base de Datos Relacional (real).
Utilizando un ORM podemos operar sobre la base de datos aprovechando las características propias de la orientación a objetos, como herencia y polimorfismo.
También podemos acceder a los atributos de una Entidad de la misma forma que accedemos a los atributos de una Clase, realizar operaciones para obtener, crear, modificar y eliminar datos, todo desde el código de programación sin tener que escribir SQL. Esto además nos permite escribir el código una sola vez y garantizarnos que va a seguir funcionando incluso si en el futuro se cambia el motor de Base de Datos (por ejemplo, de MySQL a Microsoft SQL Server).

## Creando los modelos Question y Choice

ingresamos al proyecto **polls** al archivo `models.py` e ingresamos el siguiente código para crear los modelos.

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vptess = models.IntegerField(default=0)
```

Luego nos dirigimos a la carpeta **premiosplatziapp** al archivo `settings.py`Nota: este archivo es el principal de configuración del proyecto.

En el archivo agregado en la parte de `INSTALLED_APP` y agregamos `"polls.apps.PollsConfig",` esto referencia al archivo `apps.py`  de la carpeta **polls** 

Luego ingresamos en la línea de comandos a la carpeta premiosplatziapp o donde esté el archivo manage.py e ingresamos el siguiente código:
 `py manage.py makemigrations polls`
 Lo cual nos muestra lo siguiente.
 ```Python
 Migrations for 'polls':
  polls\migrations\0003_rename_vptess_choice_votes.py
    - Rename field vptess on choice to votes```
 Luego el comando `py manage.py migrate`, lo que aplica todos los cambios que se ha realizado en el proyecto.
 
##### Nota
 `py manage.py makemigrations polls` Crea un archivo `migration/001_initial-py` en el que django automáticamente describe toda la creación de las tablas en las BD, uso del concepto ORM

`py manage.py migrate` Tomar el archivo creado y ejecutarlo en la BD. “Applying polls.001_initial”

### **La consola interactiva de Django**

para iniciar la consola de comandos, no dirigimos a la carpeta **premisplatziapp** e ingresamos el comando `py manage.py shell`

luego colocamos el siguiente comando `from polls.models import Question, Choice`

 `Question.objects.all()` para ingresar a todos los objetos que se han creado.
 Nos muestra:
  `<QuerySet [ ]>`
  
  Para crear una pregunta se utiliza para  `from django.utils import timezone` para crear objetos tipo time.
  Para la pregunta usamos `q=Question(question_text="¿Cual es el mejor curso de platzi?" , pub_date= timezone.now())` y luego la guardamos con `q.save()`
  
 otras formas de realizar este paso son:
` q  = Question.objects.create(question_text="¿Cuál es el mejor curso de platzi?" , pub_date=timezone.now())`

`q  = Question(question_text="¿Cuál es el mejor curso de platzi?" , pub_date=timezone.now()).save()`


La consola interactiva de Django comandos:

### Importación de los modelos
`from polls.models import Question, Choice`

### Llamado de todos los registros de un modelo
`Question.objects.all()`

### Creación de un nuevo registro
`q = Question(question_text="¿Cual es el mejor curso de Platzi?", pub_date=timezone.now())`

### Guardado del nuevo registro
`q.save()`

para verificar si guardo nuestra pregunta utilizamos:
`q.question_text` y nos muestra `'¿Cuál es el mejor curso de platzi?`'.

y para ver la fecha se utiliza:
q.pub_date y nos arroja `datetime.datetime(2023, 4, 29, 1, 0, 4, 168785, tzinfo=datetime.timezone.utc)`

Al repetir el comando `Question.objects.all()` nos muestra `<QuerySet [<Question: Question object (1)>]>`

para que nos muestre algo más entendible se cambian parámetros en `models.py`  y creamos un método con el siguiente código:


### El método __str__

```python
import datetime #tiempo de python

from django.db import models
from django.utils import timezone #importar para la timezona 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self,): # metodo de question_text
        return self.question_text
    
    def was_published_recenttly(self):
        return self.pub_date >= timezone.now()- datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self,): # metodo de choice_text
        return self.choice_text```

para guardar los cambios volvemos a utilizar, nos salimos con `exit()`
y usamos de nuevos `py manage.py makemigrations polls`

al terminar esto ingresamos de nuevo y repetimos `from polls.models import Question, Choice`
`usamos Question.objects.all()` y nos arroja `<QuerySet [<Question: ¿Cual es el mejor curso de Platzi?>, <Question: ¿Cual es el mejor curso de platzi?>]>`