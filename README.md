# **Curso Básico de Django**
[![](https://crowdbotics.ghost.io/content/images/2019/05/django.png)](http://https://crowdbotics.ghost.io/content/images/2019/05/django.png)

- Instalar Django.
1. Debemos crear la carpeta donde trabajaremos:` mkdir django_premiosplatzi`
y nos dirigimos a la carpeta creada. 
2. Crear el entorno virtual con venv en Windows  `py -m venv venv`  y en linux` python3 -m venv venv`.
3. Activar entorno virtual Windows: `.\venv\Scripts\activite` y en linux `source venv/Scripts/activate` si por alguna razón no funciona utilice todo el link del donde se encuentra el activador Ej: `C:\Users\monbre\OneDrive\Escritorio\programación\premiosPlatzi\venv\Scripts\activate`
4. Instalar django: `pip install django`
5. Iniciar el repositorio de git: `git init`
6. Iniciar el proyecto de django: `django-admin startproject premiosplatziapp`
7. Para evitar llevar al repositorio remoto archivos innecesarios es importante crear el archivo:` .gitignore` (Donde se suele agregar la carpeta venv o archivos que no se dese subir al repositorio) para windows de crea con  `fsutil file createnew .gitignore 0` y linux `touch .gitignore`

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
 Al carger el server nos da una direccion Ip  o localhost http://127.0.0.1:8000/
 nos muestra la sigiente pagina de inicio.
 ![](https://parzibyte.me/blog/wp-content/uploads/2019/04/4-Abrir-nuestra-primera-webapp-con-Django-en-el-navegador.png)

[Tutorial De Django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/ "Tutorial De Django")

### link de Django  File Structure
[http://https://techvidvan.com/tutorials/django-project-structure-layout/](http://https://techvidvan.com/tutorials/django-project-structure-layout/)

![](https://i1.wp.com/techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/06/Django-file-structure.jpg?fit=1200%2C628&ssl=1)

**Reference:**(*N.d.). Techvidvan.com. Retrieved April 28, 2023, from https://techvidvan.com/tutorials/django-project-structure-layout/*