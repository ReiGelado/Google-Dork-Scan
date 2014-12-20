import argparse
import urllib2
import json
import urllib
from time import sleep
from sys import exit
from random import choice

def funcao_acessa_api(string):
	try:
		api = urllib2.Request(string)
		api.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201') 
		return urllib2.urlopen(api).read()
	except:
		print '\n[+]Verifique o .txt :D'
		print '\n[+]Usuario meu amigo voce ou alguem bateu o limite de conexoes pela api :( :(\n'
		print '[+]Tente novamente :)\n'
		print '\n[+]Se o erro continuar provalmente so amanha :('
		exit()

parser = argparse.ArgumentParser()
parser.add_argument('--dork',action = 'store', dest = 'dork' , required = True , help = 'Dork que voce vai utilizar na pesquisa do google :)\nExemplo:\ninurl:noticia.php?id=')
parser.add_argument('--arquivo',action = 'store', dest = 'arquivo', required = True, help = 'Nome do arquivo que voce vai salvar as urls....')
parser.add_argument('--paginas', dest='pagina', action='store',required = False,help = 'Quantas paginas voce quer de pequisa....')
parser.add_argument('--reigelado-mode',dest = 'reigelado', action = 'store_true',required = False,help = 'Modo especial do reigelado que voce consegue mais resultados :)\nObs na hora de usar a dork nao coloque numero depois do = :)')
parser.set_defaults(reigelado=False)
parser.set_defaults(pagina="")
arguments = parser.parse_args()
print '''
......::::::::Gooogle Dork Scan V0.3 by Rei_Gelado::::::::......
......::::::::Forum:http://caveiratech.com/forum/::::::::......
......::::::::ATENCAO : NA HORA DE USAR A DORK COLOQUE O INURL::::::::::..... 
           OBS:NO REIGELADO-MODE USE DORKS COM NUMEROS NO FINAL 
                              EXEMPLO:
    script.py --dork=inurl:videos_pornos.php?id=1 --arquivo=caveiratech.txt
    script.py --dork=inurl:videos_pornos.php?id=1 --arquivo=caveiratech.txt --paginas=2 #Beta
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --reigelado-mode #Beta

'''
print '[+]Conectando....... :)\n'

lista_keys = ['AIzaSyCwWrjytJ-qmamxkeEFdAiUT9pTUClj0VU','AIzaSyAh8i756jTGxQ56RJb5RL9HTNq9UJfBlWc','AIzaSyAcjg1Nq2EhhgYMUOSN2NqCwixbsj2bKXo','AIzaSyBUfvpfclLWB-0LXoSmcrFw1ieX3rexyFw','AIzaSyAPq1_9olu0cNmTSMSQEpcNWahK8Q6Edvs','AIzaSyAMYYUdMTNDabQS8kOHibOKWoT29hMp6Dg','AIzaSyBSn-Ylr2CfbEBMxgLlDu803p6PzdTjj04','AIzaSyCjcZ4cNcof8_eUK213RXS0MpHhl3akHkE','AIzaSyAMYYUdMTNDabQS8kOHibOKWoT29hMp6Dg','AIzaSyA-4q8QaPuu6d8iXJYOH91CMuNaVrVJ2-M']
key_key = choice(lista_keys) 

url_encode = urllib.quote(arguments.dork)

limpo = 'https://www.googleapis.com/customsearch/v1?key=' + key_key + '&cx=001045170015531635135:bprdircwxpe&num=10&q='
string = 'https://www.googleapis.com/customsearch/v1?key=' + key_key + '&cx=001045170015531635135:bprdircwxpe&num=10&q=%s' % url_encode #ERRO API DO GOOGLE

html = funcao_acessa_api(string)

print '[+]Conectado,JSON baixado :)\n'

json_api = json.loads(html)

print '[+]Dados salvos...fazendo parser....\n'
print '[+]#############INFORMACOES!##########[+]\n'
print '[+]Dork:%s\n' % arguments.dork
print '[+]Arquivo:%s\n' % arguments.arquivo
try:
	print '[+]Resultados:%s paginas\n' % json_api['queries']["nextPage"][0]['totalResults']
except:
	print '[+]Infezlimente a dork que voce pesquisou nao teve resultados na api :('
	exit()
print '[+]Exbindo 10 resultados por pagina....\n'
print '[+]###################################[+]\n'
sleep(3)
n = 0
t = 0
if arguments.reigelado == True:
	print '[+]Obrigado por usar o ReiGelado Mode :)\n'
	print '[+]Que lembrando ainda esta em fase Beta Beta Beta :D\n'
	print '[+]Iniciando.....\n'
	while True:
		t = t + 1
		dork = arguments.dork + str(t)
		acessa_reigelado = limpo + urllib.quote(dork)
		html = funcao_acessa_api(acessa_reigelado)
		json_reigelado = json.loads(html)
		for x in range(0,10):
			reigelado_ct = open(arguments.arquivo,'a')
			reigelado_ct.write(json_reigelado['items'][x]['link'] + '\n')
			reigelado_ct.close()
else:
	pass
if arguments.pagina == "":
	print '[+]Salvando dados.....\n'
	for x in range(0,10):
		escrever = open(arguments.arquivo,'a')
		escrever.write(json_api['items'][x]['link'] + '\n')
		escrever.close()
	print '[+]Scan finalizado Bye :)\n'
	exit()
else:
	while True:
		n = n + 1
		valor = string + '%26start%3D' + str(n)
		html = funcao_acessa_api(valor)
		sleep(2) #google 403
		json_api2 = json.loads(html)
		for x in range(0,10):
			escrever = open(arguments.arquivo,'a')
			escrever.write(json_api2['items'][x]['link'] + '\n')
			escrever.close()
		if n == arguments.pagina:
			print '[+]Scan Finalizado Bye :)'
			exit()
		else:
			pass
