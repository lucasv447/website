# comando para startup o servidor 
 python manage.py runserver

# comando para parar o servidor 
 ctrl + c 

# comando para criar um projeto 
 django-admin.py startproject <nome_do_projeto> 
 django-admin startproject <nome_do_projeto>
 EX: django-admin startproject website

# comando para criar aplicações no django
# obs : para criara a aplicação tenho que entrar na pasta do projeto
 python manage.py startapp <nome_do_app>
 EX : python manage.py startapp niteroi

# prcesso fluxo do django 
 # primeiro :  urls 
 # segundo  :  views 
 # terceiro :  models
 # quarto   :  html 

# comando para atualizar uma nova aplicação(app)
 python manage.py makemigrations

# comando para atualizar o banco de dados
 python manage.py makemigrations 
 python manage.py migrate

# comando para criar uma função ou modulo no django
 def  <nome_do_função>(request):
 	...
 	return ...  ()

# biblioteca utilizada para recuperar API's 
 pip install requests   	