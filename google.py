import argparse
import urllib2
import json
import urllib
from time import sleep
from sys import exit

def funcao_acessa_api(string):
	try:
		api = urllib2.Request(string)
		api.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201') 
		return urllib2.urlopen(api).read()
	except:
		print '\n[+]Desculpe usuario mais o google esta dando 403 no script :(\n'
		print '[+]Tente novamente :)\n'
        print '[+]Maldito seja ele e sua API :)\n'
        exit()

parser = argparse.ArgumentParser()
parser.add_argument('--dork',action = 'store', dest = 'dork' , required = True , help = 'Dork que voce vai utilizar na pesquisa do google :)\nExemplo:\ninurl:noticia.php?id=')
parser.add_argument('--arquivo',action = 'store', dest = 'arquivo', required = True, help = 'Nome do arquivo que voce vai salvar as urls....')
parser.add_argument('--paginas', dest='pagina', action='store',required = False,help = 'Quantas paginas voce quer de pequisa....')
parser.set_defaults(pagina="")
arguments = parser.parse_args()
print '''
......::::::::Gooogle Dork Scan V0.2 by Rei_Gelado::::::::......
......::::::::Forum:http://caveiratech.com/forum/::::::::......
           ATENCAO : NA HORA DE USAR A DORK COLOQUE O INURL 
                          EXEMPLO:
    script.py --dork=inurl:videos_pornos.php?id= --arquivo=caveiratech.txt
    script.py --dork=inurl:videos_pornos.php?id= --arquivo=caveiratech.txt --paginas=2
'''
#print '[+]Bypass:%s' % arguments.bypass
print '[+]Conectando....... :)\n'

url_encode = urllib.quote(arguments.dork)

string = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBSn-Ylr2CfbEBMxgLlDu803p6PzdTjj04&cx=001045170015531635135:bprdircwxpe&num=10&q=%s' % url_encode #ERRO API DO GOOGLE

html = funcao_acessa_api(string)

print '[+]Conectado,JSON baixado :)\n'

json_api = json.loads(html)

print '[+]Dados salvos...fazendo parser....\n'
print '[+]#############INFORMACOES!##########[+]\n'
print '[+]Dork:%s\n' % arguments.dork
print '[+]Arquivo:%s\n' % arguments.arquivo
print '[+]Resultado:%s\n' % json_api['queries']["nextPage"][0]['totalResults']
print '[+]Exbindo 10 resultados por pagina....\n'
print '[+]###################################[+]\n'

sleep(3)
n = 0
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
		json_api = json.loads(html)
		for x in range(0,10):
			escrever = open(arguments.arquivo,'a')
			escrever.write(json_api['items'][x]['link'] + '\n')
			escrever.close()
		if n == arguments.pagina:
			print '[+]Scan Finalizado Bye :)'
			exit()
		else:
			pass
