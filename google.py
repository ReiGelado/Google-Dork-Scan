#!/usr/bin/python
import argparse
import urllib2
import json
import urllib
import cookielib
from time import sleep
from sys import exit
from random import choice

parser = argparse.ArgumentParser()
parser.add_argument('--dork',action = 'store', dest = 'dork' , required = True , help = 'Dork que voce vai utilizar na pesquisa do google :)\nExemplo:\ninurl:noticia.php?id=')
parser.add_argument('--arquivo',action = 'store', dest = 'arquivo', required = True, help = 'Nome do arquivo que voce vai salvar as urls....')
parser.add_argument('--paginas', dest='pagina', action='store',required = False,help = 'Quantas paginas voce quer de pequisa....')
parser.add_argument('--reigelado-mode',dest = 'reigelado', action = 'store_true',required = False,help = 'Modo especial do reigelado que voce consegue mais resultados :)\nObs na hora de usar a dork nao coloque numero depois do = :)')
parser.add_argument('--useragent-escolha',dest = 'user_agent_1',action = 'store',required = False,help = 'Voce define o User-Agent que o script vai usar :)')
parser.add_argument('--useragent-random',dest = 'user_agent_2',action = 'store_true',required = False,help = 'O programa escolhe o user agente de forma randomica :D')
parser.add_argument('--useragent-txt',dest = 'user_agent_3',action = 'store',required = False,help = 'Voce define um .txt com o UserAgent  o script identifica por linha!')
parser.set_defaults(reigelado=False)
parser.set_defaults(user_agent_1="")
parser.set_defaults(user_agent_2=False)
parser.set_defaults(user_agent_3="")
parser.set_defaults(pagina="")
arguments = parser.parse_args()

lista_keys = ['AIzaSyCwWrjytJ-qmamxkeEFdAiUT9pTUClj0VU','AIzaSyAh8i756jTGxQ56RJb5RL9HTNq9UJfBlWc','AIzaSyAcjg1Nq2EhhgYMUOSN2NqCwixbsj2bKXo','AIzaSyBUfvpfclLWB-0LXoSmcrFw1ieX3rexyFw','AIzaSyAPq1_9olu0cNmTSMSQEpcNWahK8Q6Edvs','AIzaSyAMYYUdMTNDabQS8kOHibOKWoT29hMp6Dg','AIzaSyBSn-Ylr2CfbEBMxgLlDu803p6PzdTjj04','AIzaSyCjcZ4cNcof8_eUK213RXS0MpHhl3akHkE','AIzaSyAMYYUdMTNDabQS8kOHibOKWoT29hMp6Dg','AIzaSyA-4q8QaPuu6d8iXJYOH91CMuNaVrVJ2-M']
lista_user = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19','Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Ubuntu/10.10 Chromium/8.0.552.237 Chrome/8.0.552.237 Safari/534.10','Opera/5.11 (Windows 98; U) [en]','Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fi-fi) AppleWebKit/420+ (KHTML, like Gecko) Safari/419.3','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1','Mozilla/5.0 (Ubuntu; Mobile) WebKit/537.21','Mozilla/4.0 (compatible; MSIE 5.0; Windows NT;)','Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0 IceDragon/20.0.1.14']

def funcao_acessa_api(string):
	try:
		api = urllib2.Request(string)
		cj = cookielib.MozillaCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		if arguments.user_agent_2 == True:
			print '[+]Escolhendo User-Agent de forma randomica....\n'
			user_random = choice(lista_user)
			print '[+]O user agent e %szn' % user_random
			api.add_header('User-agent',user_random)
			return opener.open(api)
		else:
			pass
		if arguments.user_agent_1 == "":
			pass
		else:
			api.add_header('User-agent',arguments.user_agent_1)
			print '[+]User-Agent: %s \n'  % arguments.user_agent_1
			return opener.open(api)
		if arguments.user_agent_3 == "":
			pass
		else: 
			reigelado_gostoso = []
			print '\n[+]Lendo seu .txt...\n'
			for reigelado in open(arguments.user_agent_3,'r'):
				reigelado.strip()
				reigelado_gostoso.append(reigelado)
			print '+]Escolhendo user-agent....\n'
			user_agent_4 = choice(reigelado_gostoso) 
			print '[+]User-agent escolhido %s\n' % user_agent_4
			api.add_header('User-agent',user_agent_4)
			return opener.open(api)
		if arguments.user_agent_1 == "" or arguments.user_agent_2 == False or arguments.user_agent_3 == "":
			print '[+]Conectando.....\n'
			print '[+]Usando user-agent padrao do script....\n'
			print '[+]User-Agent:Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19\n'
			api.add_header('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19')
			return opener.open(api)
		else:
			pass
	except:
		print '\n[+]ERRO 403 TENTE NOVAMENTE......\n'
		print '[+]Bye ;)'
		exit()

print '''
......::::::::Gooogle Dork Scan V0.5 build 1 by Rei_Gelado::::::::......
......::::::::Forum:http://caveiratech.com/forum/::::::::......
......::::::::ATENCAO : NA HORA DE USAR A DORK COLOQUE O INURL::::::::::..... 
           OBS:NO REIGELADO-MODE USE DORKS COM NUMEROS NO FINAL 
                              EXEMPLO:
    script.py --dork=inurl:videos_pornos.php?id=1 --arquivo=caveiratech.txt
    script.py --dork=inurl:videos_pornos.php?id=1 --arquivo=caveiratech.txt --paginas=2 #beta
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --reigelado-mode 
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --useragent-random
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --useragent-escolha="Seu User-Agent Aqui" #Use Aspas
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --useragent-txt=meu_arquivo.txt #beta

'''
print '[+]Conectando....... :)\n'


key_key = choice(lista_keys) 

url_encode = urllib.quote(arguments.dork)

limpo2 = 'https://www.googleapis.com/customsearch/v1?key=' + key_key + '&cx=001045170015531635135:bprdircwxpe&num=10'
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
			try:
				reigelado_ct.write(json_reigelado['items'][x]['link'] + '\n')
			except:
				print '[+]Opa as dorks acabaram :( que pena...'
				exit()
			reigelado_ct.close()
			print '[+] + 1 dork adicionada....\n'
else:
	pass
if arguments.pagina == "":
	print '[+]Salvando dados.....\n'
	for x in range(0,10):
		escrever = open(arguments.arquivo,'a')
		try:
			escrever.write(json_api['items'][x]['link'] + '\n')
		except:
			print '[+]Ooopaaaa foram coletadas menos de 10 dorks :c\n'
			print '[+]Bye\n'
			exit()
			print 
		escrever.close()
	print '[+]Scan finalizado Bye :)\n'
	exit()
else:
	while True:
		n = n + 1
		valor = limpo2 + '&start=' + str(n) + '&q=' + arguments.dork
		html = funcao_acessa_api(valor)
		json_api2 = json.loads(html)
		for x in range(0,10):
			escrever = open(arguments.arquivo,'a')
			escrever.write(json_api2['items'][x]['link'] + '\n')
			escrever.close()
			print '[+]+ 1 dork adicionada...\n'
		if n == arguments.pagina:
			print '[+]Scan Finalizado Bye :)'
			exit()
		else:
			pass
