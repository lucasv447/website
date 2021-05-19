from django.shortcuts import render
import requests # biblioteca para recuperar dados da API 
import json # biblioteca para tratar os dados recuperados pela API
import datetime as dt # biblioteca para recuperar a data 
from datetime import datetime


# função para buscar os dados da API, com dois parametros:
# a) request parametros def das funções em django 
# b) pk parametro que representa moeda
#---------------------------------------------------------------------
def quotes(request, pk): 

	#1 instaciar variaveis e objetos
	#---------------------------------------------------------------------
	w = 0
	days, categ, dollar, euro, yen, real, value = [], [], [], [], [], [], [] #criação de listas para armazenar os valores da moeda
	coindollar = coineuro = coinyen = coinreal = None
	coins = {} # criação de uma variavel dicionario/json para receber as listas 

	#2 comando for para pegar os 7 dias anteriores da semana
	#---------------------------------------------------------------------		
	for i in range(0,7): #estudar o range

		if i == 0:
			day   = dt.date.today()
		else:
			today = dt.date.today()
			day   = today - dt.timedelta(days=int(i))

		#2 comando para pegar a data corrente
		#---------------------------------------------------------------------	
		coindate = str(day.strftime("%d/%b"))
		days.append(str(day.strftime("%d/%b")))


		#3 processo para configuração da API 
		#---------------------------------------------------------------------	
		url = 'https://api.vatcomply.com/rates?date='+str(day)

		#4 popular os dados recuperados da API dentro de uma variavel 
		#---------------------------------------------------------------------
		result = requests.get(url)

		#5 a variavel rjson recebe os dados da api no formato json
		#---------------------------------------------------------------------	
		rjson  = result.json()

		#6 verificar a moeda corente
		#---------------------------------------------------------------------	
		if pk == '1':

			moeda = float(rjson['rates']['EUR'])
			namemoeda = 'EURO' 
			namecotacao = 'Cotação do DOLLAR vs EURO'
			labelx      = 'Euro € '

		elif pk == '2':

			moeda = "%.2f" % float(rjson['rates']['JPY'])
			namemoeda = 'YEN' 
			namecotacao = 'Cotação do DOLLAR vs YEN'
			labelx      = 'Yen ¥ '

		else:
			
			moeda = "%.2f" % float(rjson['rates']['BRL'])
			namemoeda = 'REAL' 
			namecotacao = 'Cotação do DOLLAR vs REAL'
			labelx      = 'Real R$ '

		coindollar = "%.2f" % float(rjson['rates']['USD'])
		

		# start load data in list to after that plot in chart
		#-------------------------------------------------------------------------------------------------
		categ.append(coindate) # atribuindo cada dia dos 7 a lista
		dollar.append(coindollar) # atribuindo a variavel dollar o seu valor em cada um dos 7 dias
		value.append(moeda) # atribuindo a moeda corrente o valor de cada dia
		

		# start load data to in dictionary
		#--------------------------------------------------------------------------------------------------
		coins[w] = {'code': w, 'coindate':coindate, 'coindollar': coindollar, 'moeda':moeda}
		
		# start increment variable to next flow
		#--------------------------------------------------------------------------------------------------
		w += True	

    # variavelque recebe todos os dados processados e é enviada como parametro pro html 
	context = {'coins':coins,'categ':json.dumps(categ), 'dollar':json.dumps(dollar), 'value':json.dumps(value),
	'labelx':json.dumps(labelx), 'namemoeda':namemoeda, 'namecotacao':namecotacao,} 
	
	#8 enviar os dados processados para o arquivo html(quotes)
	#---------------------------------------------------------------------
	return render(request, 'price/quote.html', context)


