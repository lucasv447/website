from django.shortcuts import render
from django.http import HttpResponse # Estudar 
from django.http import HttpResponseRedirect


def index (request):
    
	#return HttpResponse("<h1> Olá mundo! </h1>") 

	return render (request, 'core/index.html')

def entrar(request):

	esperto = 'Lucas Vilela'

	context = {'nome':esperto}

	return render(request, 'core/entrar.html', context)