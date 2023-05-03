# **Curso Básico de Django**
[![](https://crowdbotics.ghost.io/content/images/2019/05/django.png)](http://https://crowdbotics.ghost.io/content/images/2019/05/django.png)

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
    return HttpResponse("Hello world", 2+8)
```

Luego nos dirigimos a la carpeta `urls.py` de premiosplatziapp y le agregamos a urlpatterns un nuevo path.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls"))
]
```
Luego creamos la parpeta de `urls.py `en mi proyecto `polls`.

y en el archivo agregamos el siguiente código:
```Python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

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
    - Rename field vptess on choice to votes
  ```
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
        return self.choice_text
```

para guardar los cambios volvemos a utilizar, nos salimos con `exit()`
y usamos de nuevos `py manage.py makemigrations polls`

al terminar esto ingresamos de nuevo y repetimos `from polls.models import Question, Choice`
`usamos Question.objects.all()` y nos arroja `<QuerySet [<Question: ¿Cual es el mejor curso de Platzi?>, <Question: ¿Cual es el mejor curso de platzi?>]>`

### Filtrando los objetos creados desde la consola interactiva

activamos la consola con el código `py manage.py shell` 
creamos las preguntas con el código `Question(question_text="Pregunta", pub_date=timezone.now()).save()`

Para nuestro proyecto usamos las siguientes `Question(question_text="¿Quién es el mejor profesor de platzi?", pub_date=timezone.now()).save()` y `Question(question_text="¿Cual es la mejor escuela de platzi?", pub_date=timezone.now()).save()`.

Para ver si se crearon las preguntas usamos `Question.objects.all()`.

Para filtrar alguna de las preguntas usamos get con `pk= #`
ejemplo: `Question.objects.get(pk=1)`

y por fecha se usa el código: `Question.objects.get(pub_date__year=timezone.now().year)`
Nota: arrojará error por qué es para buscar un solo argumentó, en pocas palabras una pregunta.

Para año, mes y día se usa:
- `get(pub_date__year=timezone.now().year)`

- `get(pub_date__year=timezone.now().month)`
- `get(pub_date__year=timezone.now().day)`

Para usar con filter:
####  El método filter
para filtrar y no nos arroja error como get   con la pk nos muestra `Question.objects.filter(pk=1)`,
`<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>]>`
`Question.objects.filter(pk=2)` y con esto nos muestra 
`<QuerySet [<Question: ¿Quién es el mejor profesor de Platzi?>]>`.

Para filtrar con una palabra en específico, utilizamos   `Question.objects.filter(question_text__startswith='¿Cuál')`  y nos muestra la que cumple esta condición y  `Question.objects.filter(pub_date__year=timezone.now().year)` nos muestra todas las que cumple la condición. 

`__gt` = Mayor que
`__gte` = Mayor o igual que
`__lt` = Menor que
`__lte` = Menos o igual que
`__startswith` = Empieza con
`__endswith` = Termina con
`__iexact` = Coincidencia que no distingue entre mayúsculas y minúsculas.
`__contains`: Contiene
`__icontains` = Versión que no distingue entre mayúsculas y minúsculas de la anterior
`__istartswith` = versión insensible a mayúsculas y minúsculas de beginwith
`__iendswith` = versión insensible y termina con mayúsculas y minúsculas.

 En SQL
```
# startswith
SELECT * FROM table WHERE field LIKE 'Whatever%';
# endswith
SELECT * FROM table WHERE field LIKE '%whatever';
# contains
SELECT * FROM table WHERE field LIKE '%whatever%';
# endswith
SELECT * WHERE headline LIKE '%Lennon';
```

**link** : [http://https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups](http://https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups)

Ejemplo:
`Questions.objects.filter( pub_time__lte = (timezone.now() - timedelta(hours=12) ) )`

### Para limpiar la pantalla

En Windows
`import os`
`os.system("cls")`

En linux.
`import os`
`os.system("clear")` o `CTRL + R`

####  para crear la respuesta utilizamos los siguientes pasos:

Miramos todas las preguntas con el comando `Question.objects.all()` que nos arroja:
`<QuerySet [ <Question: ¿Cual es el mejor curso de platzi?>, <Question: ¿Quién es el mejor profesor de platzi?>, <Question: ¿Cual es la mejor escuela de platzi?>]>`

Ingresamos a la respuesta con `q = Question.objects.get(pk=1`)

luego `q` que nos muestra lo que vamos a modificar `<Question: ¿Cual es el mejor curso de Platzi?>`

para ver qué respuestas contiene utilizamos `q.choice_set.all()`, que nos muestra su contenido  `<QuerySet []>` y para agregar la respuesta utilizamos  `q.choice_set.create(choice_text="Curso Básico de Python", votes= 0)` que nos arroja `<Choice: Curso Básico de Python>` luego creamos las otras dos
`q.choice_set.create(choice_text="Curso de fundamentos de Ingenieria de Software", votes= 0)` y `q.choice_set.create(choice_text="Curso de Elixer", votes= 0)`

para ver ya el contenido utilizamos `q.choice_set.all()`
para que nos diga la cantidad usamos `q.choice_set.count()` y para filtrar por año usamos `Choice.objects.filter(question__pub_date__year=timezone.now().year)`

## crear usuario
Crear un usuario se utiliza `py manage.py createsuperuser`  nos pide nombre de usuario, correo y una contraseña.
luego nos dirigimos a la carpeta **polls**  y nos dirigimos al archivo `admin.py`.
y agregamos el sigiente codigo:
```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```
y luego de esto nos dirigimos al navegador al localhost http://127.0.0.1:8000/admin he ingresamos el usuario y el passwork 

![](https://tutorial.djangogirls.org/es/django_admin/images/login_page2.png) 

y ingresamos a esta interfaz.
![](https://media.geeksforgeeks.org/wp-content/uploads/20201024140816/Screenshotfrom20201024140459.png)

## crear usuario
Crear un usuario se utiliza `py manage.py createsuperuser`  nos pide nombre de usuario, correo y una contraseña.
Luego nos dirigimos a la carpeta **polls**  y nos dirigimos al archivo `admin.py`.
y agregamos el siguiente código:
```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```
y luego de esto nos dirigimos al navegador al localhost http://127.0.0.1:8000/admin e ingresamos el usuario y el passwork 

![](https://tutorial.djangogirls.org/es/django_admin/images/login_page2.png) 

y ingresamos a esta interfaz.
![](https://media.geeksforgeeks.org/wp-content/uploads/20201024140816/Screenshotfrom20201024140459.png)

## Diferencia entre MVC y MTV 😮
Muy similar a MVC (Modelo, vista, controlador) donde:
.
Modelo - Hace referencia a todo lo que tiene que ver con bases de datos.
Vista - Con la parte visual.
Controlador - Con toda la parte lógica.

En Django siendo MTV 😃

Modelo - Hace referencia a todo lo que tiene que ver con bases de datos (En este caso Django hace demasiada alusión a su nombre donde las bases de datos quedan implícitas y manejamos todo con el ORM)

Template - En este caso no debemos confundir el View del MTV con el del MVC puesto en que en Django no hace referencia a lo visual, template si hace alusión con la parte visual de las Web Apps con Django.

View - Todo lo relacionado con la lógica es aquí donde entra el tema de las vistas genéricas y demás (Que si solo nos especializamos en el back con Django es lo que mas utilizaremos)

### Creando vistas para la aplicación
nos dirigimos a la carpeta polls al archivo views.py y agregamos las vista con el  codigo 
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estas en la página principal de Premios Platzi App")

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número{question_id}")
```

luego para poderla visualizar, nos dirigimos al archivo urls.py ya agregamos los siguientes `path`

```python
from django.urls import path

from . import views

urlpatterns = [
    #ex: /polls/
    path("", views.index, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    #ex: /polls/5/results
    path("<int:question_id>/results/", views.result, name="result"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
para probar si todo funcionas nos dirigimos al siguiente link:
Para  index:
[Index](http://http://127.0.0.1:8000/polls/)
para la pregunta 5
[pregunta 5](http://http://127.0.0.1:8000/polls/5/ "pregunta 5")
para results:
[results](http://http://127.0.0.1:8000/polls/5/results/ "results")
Para vote:
[vote](http://http://127.0.0.1:8000/polls/5/vote/ "vote")

## Templates de Django
en visual en el programa `polls` creamos una nueva carpeta con el nombre `templates` y luego otra carpeta llamada `polls`.
y creamos un archivo nuevo con index.html

luego descargamos la extensión **Django**  y la instalamos, para que funcione el **shortcuts** de Django presionamos CTRL +SHIFP +  P y buscamos **settings.json**  y hacemos clip en** Open User settings(JSON)** y nos abre un archivo **JSON**  y agregamos el siguiente código 
```python
"emmet.includeLanguages": {
        "html": "django-html"
    }
```

archivo JSON
```json
{
    "liveServer.settings.donotShowInfoMsg": true,
    "editor.wordWrap": "on",
    "jupyter.askForKernelRestart": false,
    "security.workspace.trust.untrustedFiles": "open",
    "extensions.autoUpdate": "onlyEnabledExtensions",
    "editor.accessibilitySupport": "off",
    "terminal.integrated.enableMultiLinePasteWarning": false,
    "files.autoSave": "afterDelay",
    "[python]": {
        "editor.formatOnType": true
    },
    "breadcrumbs.enabled": false,
    "redhat.telemetry.enabled": true,
    "emmet.includeLanguages": {
        "html": "django-html"
    }
}
```
si no realiza el **shortcuts** no dirigimos a la extensión de `django` lo deshabilitamos y lo recargamos y ya funciona el **shortcuts**

Si no funciona utilizamos el siguiente código. 
```json
"emmet.includeLanguages":{
        "django-html": "html"
    } 
```

En el archivo index de la carpeta templates el siguiente código:
```html
{% if latest_question_list %}
  <ul>
    {% for question in latest_question_list %}
    <li><a href="/polls/{{ question.id}}">{{ question.question_text}}</a></li>
    {% endfor %}

  </ul>
  {% else %}
    <p>No polls are available.</p>
{% endif %}
```

en el archivo `views.py`  el models y modificamos el index como lo muestra el siguiente código:
```python
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número{question_id}")

```

### Elevando el error 404

vamos al archivo `views.py`  y en `detail` modificamos y importamos `get_object_or_404` como  lo muestra el codigo:
```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{
        "question": question
    } )

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número{question_id}")
```
luego creamos el archivo `detail.html` en la carpeta `templates\polls ` y agregamos el siguiente código:
```html
<h1>{{question.question_text}}</h1>
<ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }}</li>
    {% endfor %}
</ul>
```
### Formularios: lo básico
trabajamos en el archivo `detail.py` y usamos el siguiente código:
```html
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text}}</h1></legend>
    {% if error_message %}
        <p><strong>{{ error_message }}</strong></p>
    {% endif %}
    {% for choice in question.choice_set.all %}
        <input 
            type="radio"
            name="choice"
            id="choice{{ forloop.counter }}" 
            value="{{ choice.id }}"      
        >
        <label for="choice{{ forloop.counter }}">
            {{ choice.choice_text }}
        </label>
        <br>
    {% endfor %}
</fieldset>
<input type="submit" value="Votar">
</form>
```
### Creando la vista vote
en esta parte, se agrega el conteo de los votos en la carpeta polls en abrir el archivo views.py y agregamos el siguiente código:
```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{
        "question": question
    } )

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número {question_id}")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message":"No eligiste una respuesta"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
```
### Creando la vista results
Creando la vista results
Hasta ahora tenemos la interfaz de voto y el conteo de votos programado, ahora vamos a programar la vista, resultados para ver la cantidad de votos por opción cuando votamos, para esto hacemos cambios en los archivos `views.py` y `results.html`, este último lo vamos a crear, recordemos que todo lo trabajamos dentro de la carpeta de la aplicación.
En el archivo `views.py`
```python
def results(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question
    })
```
Recordemos que al llamar los templates debemos enviar los argumentos si son necesarios, en este caso “question”

En el archivo `results.html`

```python
<h1>{{ question.question_text }}</h1>
<ul>
    {% for choice in question.choice_set.all %}
        <li>
            {{ choice.choice_text }} -- {{ choice.votes }}
            vote{{ choice.votes|pluralize  }}
        </li>
    {% endfor %}
</ul>
<a href="{% url 'polls:detail' question.id %}">
    ¿Te gustaría votar de nuevo?
</a>
```
## CRUD
C = Create
R = Read
U = Update
D = Delete

### Implementando generic views en la aplicaciónImplementando generic views en la aplicación

en views.py comentamos el anterior código y agregamos el siguiente:
```python
from django.views  import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published question"""
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
```
y en urls.py cambiamos el question_id por pk y agregamos el siguiente código:

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    #ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
### Curso de Django Intermedio: Testing, Static Files, Django Admin

#### **¿Qué son los tests?**
Es una función que verifica que el código funciona correctamente

#### **¿Por qué debería hacer tests?**
Porque me permite evitar errores futuros a través de funciones que trabajan sobre las funciones principales de mi código.

- Nos permite ver errores que a simple vista no hubiéramos visto.
- Nos hace ver más profesionales.
- Permite trabajar en equipo.

#### **Test Driven Developer**
TDD o Test-Driven Development (desarrollo dirigido por tests) es una práctica de programación que consiste en escribir primero las pruebas (generalmente unitarias), después escribir el código fuente que pase la prueba satisfactoriamente y, por último, refactorizar el código escrito.

### Escribiendo nuestro primer test
ingresamos a `menage.py ` en la carpeta de nuestro proyecto con el código `py manage.py shell` e implementamos los siguientes modulos en el **shell **
```python
import datetime
from django.utils import timezone
from polls.models import Question```

después de cargas las modulos creamos nuestra pregunta:
` q = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=timezone.now()+ datetime.timedelta(days=30))`
para ver la pregunta usamos el código `q.was_published_recently()`
pero el método nos arroja true y debe arrojar false.
Para corregir esto no dirigimos a la carpeta **poll** al archivo **tests.py**

y agregamos este código para crear un **tests** nuevo usando el siguiente código:

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

#se van a testear 
# Models
# Vistas
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """"was_published_recently return False for question whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿quién es el mejor Course de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recenttly(), False)```

Luego regresamos a la shell y ejecutamos la prueba con el siguiente código `py manage.py test polls`, pero el método nos sigue arrojando true.

### **Solucionando el error encontrado**
solo nos dirigimos a `models.py` y modificamos el siguiente código:
```python
def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

**Pasos a seguir para los tests**
1. Identificamos un problema.
2. Creamos un test.
3. Corremos el test.
4. Arreglamos el problema.
5. Corremos el test.

### Testing de Views

para realizar el testing sobre los objetos y no aparezca las pregunta que se deben publicar a futuro usamos el siguiente código y solucionamos este problema.
Nos dirigimos a `views.py` y agregamos el siguiente código:

```python
#importamos reverse
from django.urls import reverse

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published question"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]```

Luego creamos el testing.
Para que no nos vuelva a suceder esto:
```python
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If not question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])```

Recordar que __lte me trae las preguntas presentes y del pasado, no las futuras.

### Creando más tests para IndexView

en el archivo polls ingresamos a testing y se crea lo siguiente 
```python
def create_question(question_text, days):
    """
    Create a question with the given "question_test", and published the given numbre of day offset to now (negative for question published in the past, positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def test_future_question(self):
        """
        Question with a pub_date in the future aren't displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_past_question(self):
        """
        Question wiht a pub_date in the past are displayed on the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[question])
```
### Ajustando detalles en los tests para IndexView

con los siguientes código pasado, futuro y para dos preguntas pasadas y futuras:
```python
def test_future_question_and_past_question(self):
        """
        Even is both past and future question exist, only past question are displayed.
        """
        past_question= create_question(question_text="Past question", days=-30)
        future_question= create_question(question_text="Future question", days=30)
        response =self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question]
        )


    def text_two_past_question(self):
        """The questions index page may display multiple questions"""
        past_question1= create_question(question_text="Past question 1", days=-30)
        past_question2= create_question(question_text="Past question 2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1, past_question2]
        )

    def text_two_future_question(self):
        """The questions index page may display multiple future questions"""
        future_question1= create_question(question_text="Future question 1", days=50) 
        future_question2= create_question(question_text="Future question 2", days=60)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [future_question1, future_question2]
        )
```
### Creando tests para DetailView

solo agregamos este código a testing:
```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future return a 404 error not found
        """
        future_question = create_question(question_text="Future question",days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the question's text
        """
        past_question = create_question(question_text="Past question",days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

y en la parte de view alteramos DetailView:

```python
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
         """
         Excludes any question that aren't published yet
         """
         return Question.objects.filter(pub_date__lte=timezone.now())
```

### gregando estilos a nuestro proyecto
para crear loa estilos lo que se debe hacer es en el proyecto crear una nueva carpeta con el nombre **static** y dentro de ellla creamos otra con el nombre **polls**, se crea un archivo con el nombre  **style.css**, para probar usamos los siguiente.
```css
li a {
    color: green;
}
```

despues nos dirigimos al index de nuestro proyecto y linkiamos el archivo `style.css` que acabamos de crear.
agregamos lo siguiente al inicio de nuestro html:
```html 
{% load static %}
<link rel="stylesheet" href="{% static 'polls/style.css' %}"
```
### Añadiendo una imagen de fondo
descargamos nuestra imagen que deseemos de fondo para nuestro proyecto buscamos una imagen, al guardarla en nuestro proyecto en la carpeta `premiosplatziapp/polls/static/polls` y aqui creaomos la creamos la carpeta `images`  y se guarda la imagen, luego creamos en el archivo style.css el código:
```css
body {
	background: white url("images/background.gif") no-repeat;
}
```
### Mejorando el Admin: Questions

se cambia el orden de los campos del  modelos y como combinarlos campos del modelos, esto lo cambiamos en nuestro archivo admin.py y creamos lo siguiente:
```python
from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```
### Mejorando el Admin: Change List

en este punto le agregamos a la clase QuestionAdmin que son para filtrar las fechas y crear un buscador de preguntas y eso realiza con los siguiente:
```python
	list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
```
