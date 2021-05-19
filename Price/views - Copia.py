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
	categ = moeda = data = dia = None
	url = context = result = None
	dollar = euro = real = yen = None
	nomemoeda = nomecotacao = None
	diaform = None
	w = 0

	#2 comando for para pegar os 7 dias anteriores da semana
	#---------------------------------------------------------------------		
	for i in range(0,7):

		if i == 0:
			diaform = dt.date.today()
		else:
			today = dt.date.today()
			diaform = today - dt.timedelta(days = int(i))	

		#2 comando para pegar a data corrente
		#---------------------------------------------------------------------	
		diaform = dt.date.today()
		dia = str(diaform.strftime("%d/%b"))


		#3 processo para configuração da API 
		#---------------------------------------------------------------------	
		url = 'https://api.vatcomply.com/rates?date='+str(diaform)

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
			nomemoeda = 'EURO' 
			nomecotacao = 'Cotação do DOLLAR vs EURO'

		elif pk == '2':

			moeda = "%.2f" % float(rjson['rates']['JPY'])
			nomemoeda = 'YEN' 
			nomecotacao = 'Cotação do DOLLAR vs YEN'

		else:
			
			moeda = "%.2f" % float(rjson['rates']['BRL'])
			nomemoeda = 'REAL' 
			nomecotacao = 'Cotação do DOLLAR vs REAL'

		dollar = "%.2f" % float(rjson['rates']['USD'])
		

		#6 atribuir os valores das moedas as variaveis 
		#---------------------------------------------------------------------	
		# euro   = str(rjson['rates']['EUR'])
		# dollar = str(rjson['rates']['USD'])
		# real   = str(rjson['rates']['BRL'])
		# yen    = str(rjson['rates']['JPY'])

		'''print('-' * 70)
		print('EURO   : ', str(rjson['rates']['EUR']))
		print('DOLLAR : ', str(rjson['rates']['USD']))
		print('REAL   : ', str(rjson['rates']['BRL']))
		print('YEN    : ', str(rjson['rates']['JPY']))
		print('-' * 70, '\n\n')'''

	#7 carregar a variavel context com  os valores como dicionario
	#---------------------------------------------------------------------
	context = {'pk':pk, 'dollar':dollar,'dia':dia, 
	 'moeda':moeda, 'nomemoeda' :nomemoeda, 'nomecotacao' :nomecotacao}

	#8 enviar os dados processados para o arquivo html(quotes)
	#---------------------------------------------------------------------
	return render(request, 'price/quote.html', context)


