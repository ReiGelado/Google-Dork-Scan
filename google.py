#!/usr/bin/python
#!C:/Python27/
import argparse
import json
import urllib
import conexao #arquivo local
import os
from time import sleep
from sys import exit
from random import choice

parser = argparse.ArgumentParser()
parser.add_argument('--dork',action = 'store', dest = 'dork' , required = True , help = 'Dork que voce vai utilizar na pesquisa do google :)\nExemplo:\ninurl:noticia.php?id=')
parser.add_argument('--arquivo',action = 'store', dest = 'arquivo', required = True, help = 'Nome do arquivo que voce vai salvar as urls....')
parser.add_argument('--reigelado-mode',dest = 'reigelado', action = 'store_true',required = False,help = 'Modo especial do reigelado que voce consegue mais resultados :)\nObs na hora de usar a dork nao coloque numero depois do = :)')
parser.add_argument('--proxy-tipo',dest = 'tipo_proxy',action = 'store',required = False,help = 'Tipo de proxy...Https/Https/Socks5/4')
parser.add_argument('--proxy-ip',dest = 'ip_proxy',action = 'store' , required = False,help = 'Ip do Proxy ou Dns :)')
parser.add_argument('--useragent-proxy',dest = 'user_agent_proxy',action = 'store',required = False,help = 'User-Agent do Proxy :)')
parser.add_argument('--useragent-escolha',dest = 'user_agent_1',action = 'store',required = False,help = 'Voce define o User-Agent que o script vai usar :)')
parser.add_argument('--useragent-random',dest = 'user_agent_2',action = 'store_true',required = False,help = 'O programa escolhe o user agente de forma randomica :D')
parser.add_argument('--useragent-txt',dest = 'user_agent_3',action = 'store',required = False,help = 'Voce define um .txt com o UserAgent  o script identifica por linha!')
parser.add_argument('--api-antiga',dest = 'api_antiga',action = 'store_true',required = False,help = 'Voce pode usar a api antiga do google que so gera 4 resultado por pagina....')
parser.set_defaults(api_antiga=False)
parser.set_defaults(reigelado=False)
parser.set_defaults(tipo_proxy = "")
parser.set_defaults(ip_proxy = "")
parser.set_defaults(user_agent_proxy="")
parser.set_defaults(user_agent_1="")
parser.set_defaults(user_agent_2=False)
parser.set_defaults(user_agent_3="")
arguments = parser.parse_args()

falta = 0

if os.path.isfile('keys.txt') == False:
	print '[+]O arquivo keys.txt esta faltando....\n'
	sleep(2) # para o usuario ler....
	falta = 1
if os.path.isfile('ua.txt') == False:
	print '[+]O arquivo ua.txt esta faltando.....\n'
	sleep(2)
	falta = falta + 1
if os.path.isfile('conexao.py') == False:
	print '[+]O arquivo conexao.py esta faltando....\n'
	sleep(2)
	falta = falta + 1
if falta >= 1:
	print '[+]Finalizando o script por falta de arquivos.....\n'
	exit()
else:
	pass

def funcao_acessa_api(url):
	#Um breve ensinamento gafanhotos,se o script bugar e o seu nome nao estiver na classe pode festejar que a culpa nao e sua U.U
	ua = conexao.ReiGelado()
	try:
		if arguments.user_agent_1 == "":
			pass
		else:
			return ua.user_agent_1(url,arguments.user_agent_3)
		if arguments.user_agent_2 == True:
			return ua.user_agent_2(url)
		else:
			pass
		if arguments.user_agent_3 == "":
			pass
		else:
			return ua.user_agent_3(url,arguments.user_agent_3)
		if arguments.ip_proxy == "" or arguments.tipo_proxy == "":
			pass
		else:
			print '[+]Iniciando Conexao...\n'
			print '[+]Proxy-Ip:%s\n' % arguments.ip_proxy
			print '[+]Tipo de Proxy:%s\n' % arguments.tipo_proxy
			if arguments.user_agent_proxy == "":
				return ua.user_proxy(url,arguments.ip_proxy,arguments.tipo_proxy)
			else:
				return ua.proxy_user(url,arguments.ip_proxy,arguments.tipo_proxy,arguments.user_agent_proxy)
		if arguments.user_agent_1 == "" or arguments.user_agent_2 == False or arguments.user_agent_3 == "":
			return ua.user_off(url)
		else:
			pass
	except:
		print '\n[+]ERRO 403 TENTE NOVAMENTE......\n'
		print '[+]Bye ;)'
		exit()

print '''
                    ......::::::::Google Dork Scan V0.7 by Rei_Gelado::::::::......
                    ......::::::::Forum:http://caveiratech.com/forum/::::::::......
                                            EX:
    script.py --dork=inurl:videos_pornos.php?id=1 --arquivo=caveiratech.txt
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --reigelado-mode
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --api-antiga  
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --api-antiga --reigelado-mode 
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --useragent-random
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --useragent-escolha="Seu User-Agent Aqui" #Use Aspas
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --useragent-txt=meu_arquivo.txt #beta
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --proxy-ip="127.0.0.1:2424" --proxy-tipo="https" #https,socks5,socks4
    script.py --dork=inurl:videos_pornos.php?id=  --arquivo=caveiratech.txt --proxy-ip="127.0.0.1:2424" --proxy-tipo="https" --useragent-proxy="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)"

'''
lista_keys = []

for keys2 in open('keys.txt','r'):
	lista_keys.append(keys2.strip())

key_key = choice(lista_keys) 

url_encode = urllib.quote(arguments.dork)

if arguments.api_antiga == True:
	string = 'http://ajax.googleapis.com/ajax/services/search/web?v=2.0&q=%s' % url_encode
	limpo = 'http://ajax.googleapis.com/ajax/services/search/web?v=2.0&q='
	api_info = 'ANTIGA'
	print '[+]Lembrando a api antiga nao tem limite de conexa...pode se estragar euhuehe :D...\n'
else:
	limpo = 'https://www.googleapis.com/customsearch/v1?key=' + key_key + '&cx=001045170015531635135:bprdircwxpe&num=10&q='
	string = 'https://www.googleapis.com/customsearch/v1?key=' + key_key + '&cx=001045170015531635135:bprdircwxpe&num=10&q=%s' % url_encode #ERRO API DO GOOGLE
	api_info = 'NOVA'
	pass

html = funcao_acessa_api(string)

print '[+]Conectado,JSON baixado :)\n'

json_api = json.loads(html)

print '[+]Dados salvos...fazendo parser....\n'
print '[+]#############INFORMACOES!##########[+]\n'
print '[+]API:%s\n' % api_info
print '[+]Dork:%s\n' % arguments.dork
print '[+]Arquivo:%s\n' % arguments.arquivo
try:
	if arguments.api_antiga == True:
		print '[+]Resultados:%s\n'% json_api['responseData']['cursor']['estimatedResultCount']
	else:
		print '[+]Resultados:%s paginas\n' % json_api['queries']["nextPage"][0]['totalResults']
except KeyError:
	print '[+]###################################[+]\n'
	print '[+]Infezlimente a dork que voce pesquisou nao teve resultados na api :('
	exit()
if arguments.api_antiga == True:
	print '[+]Exibindo 4 resultados por pagina....\n'
else:
	print '[+]Exibindo 10 resultados por pagina....\n'
print '[+]###################################[+]\n'
sleep(3)
n = 0
t = 0
if arguments.reigelado == True:
	print '[+]Iniciando.....\n'
	while True:
		t = t + 1
		dork = arguments.dork + str(t)
		acessa_reigelado = limpo + urllib.quote(dork)
		html = funcao_acessa_api(acessa_reigelado)
		json_reigelado = json.loads(html)
		if arguments.api_antiga == True:
			for x in range(0,4):
				reigelado_ct = open(arguments.arquivo,'a')
				try:
					reigelado_ct.write(json_reigelado['responseData']['results'][x]['unescapedUrl'] + '\n')
					print '[+]1 dork adicionada....\n'
				except:
					print '[+]Opa as dorks acabaram :( que pena...'
					exit()
					reigelado_ct.close()
		else:
			for x in range(0,10):
				reigelado_ct = open(arguments.arquivo,'a')
				try:
					reigelado_ct.write(json_reigelado['items'][x]['link'] + '\n')
					print '[+]1 dork adicionada......\n'
				except:
					print '[+]Opa as dorks acabaram :( que pena...'
					exit()
					reigelado_ct.close()
else:
	pass
if arguments.reigelado == False:
	print '[+]Salvando dados.....\n'
	try:
		if arguments.api_antiga == True:
			for x in range(0,4):
				escrever = open(arguments.arquivo,'a')
				escrever.write(json_api['responseData']['results'][x]['unescapedUrl'] + '\n')
				print '[+]1 dork adicionada...\n' 
		else:
			for x in range(0,10):
				escrever = open(arguments.arquivo,'a')
				escrever.write(json_api['items'][x]['link'] + '\n')
				print '[+]1 dorkm adicionada....\n'
	except:
		print '[+]Ooopaaaa foram coletadas menos de 10 dorks :c\n'
		print '[+]Bye\n'
	escrever.close()
	print '[+]Scan finalizado Bye :)\n'
	exit()
else:
	pass
