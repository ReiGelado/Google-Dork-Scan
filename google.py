import argparse
import urllib2
import json
parser = argparse.ArgumentParser()
parser.add_argument('--dork',action = 'store', dest = 'dork' , required = True , help = 'Dork que voce vai utilizar na pesquisa do google :)\nExemplo:\ninurl:noticia.php?id=')
parser.add_argument('--arquivo',action = 'store', dest = 'arquivo', required = True, help = 'Nome do arquivo que voce vai salvar as urls....')
arguments = parser.parse_args()
print '''
......::::::::Gooogle Dork Scanv0.0.0.0.0.1 by Rei_Gelado::::::::......
......::::::::Forum:http://caveiratech.com/forum/::::::::......
           ATENCAO : NA HORA DE USAR A DORK COLOQUE O INURL 
                          EXEMPLO:
  google.py --dork=inurl:videos_pornos.php?id= --arquivo=caveiratech.txt
'''
print '[+]Dork:%s' % arguments.dork
print '[+]Arquivo:%s' % arguments.arquivo
print '[+]Conectando....... :)'
string = 'http://ajax.googleapis.com/ajax/services/search/web?v=2.0&q=%s' % arguments.dork
api = urllib2.Request(string)
api.add_header('User-agent', 'Mozilla 5.10') #404 RESOLVIDO
html = urllib2.urlopen(api).read()
print '[+]Conectado,JSON baixado :)'
json_api = json.loads(html)
print '[+]Dados salvos...fazendo parser....'
for x in range(0,4):
	escrever = open(arguments.arquivo,'a')
	escrever.write(json_api['responseData']['results'][x]['unescapedUrl'] + '\n') #escrever.write eheuheuheuehueh
	escrever.close()
print '[+]Dados salvos no %s e script finalizado :D' % arguments.arquivo
print '[+]bye ;)'
