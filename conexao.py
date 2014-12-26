#!/usr/bin/python
#!C:/Python27/
#Google Dork Scan by Rei_Gelado
#Acesse
#http://caveiratech.com/forum/
#E seja feliz :)
import cookielib
import urllib2
from random import choice
from sys import exit
class ReiGelado():
	def __init__(self):
		print '[+]Classe ativada....\n'
		self.useragent = ""
	def user_agent_1(self,url,useragent):
		print '[+]Usando seu User-Agent :)\n'
		print '[+]Seu User-Agent e %s\n' % useragent
		print '[+]Conectando....\n'
		api = urllib2.Request(url)
		try:
			api.add_header('User-Agent',useragent)
		except:
			print '[+]Voce informou um User-Agent invalido...\n'
			exit()
		cj = cookielib.MozillaCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		return opener.open(api).read()
	def user_agent_2(self,url):
		print '[+]Escolhendo User-Agent de forma randomica :)...\n'
		lista = []
		try:
			for escolha_20 in open('ua.txt','r'):
				lista.append(escolha_20.strip())
		except:
			print '[+]ERRO - Arquivo ua.txt nao esta no diretorio :(\n'
			exit()
		lalala = choice(lista)
		print '[+]User-Agent escolhido : %s \n' % lalala
		api = urllib2.Request(url)
		api.add_header('User-Agent',lalala)
		print '\n[+]Iniciando conexao....\n'
		cj = cookielib.MozillaCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		return opener.open(api).read()
	def user_agent_3(self,url,txt):
		reigelado = []
		print '[+]Pegando o User-Agent....\n'
		try:
			for txt_rei in open(txt,'r'):
				reigelado.append(txt_rei.strip())
		except:
			print '[+]o arquvo %s nao esta no diretorio do script....' % txt
			exit()
		print '[+]%s Carregado....\n' % txt
		lalala2 = choice(reigelado)
		api = urllib2.Request(url)
		api.add_header('User-Agent',lalala2)
		print '[+]Seu User-Agent e %s \n' % lalala2
		print '[+]Iniciando conexao...\n'
		cj = cookielib.MozillaCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		return opener.open(api).read()
	def user_off(self,url):
		print '[+]Conectando.....\n'
		print '[+]Usando user-agent padrao do script....\n'
		print '[+]User-Agent:Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19\n'
		api = urllib2.Request(url)
		api.add_header('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19')
		cj = cookielib.MozillaCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		return opener.open(api).read()
	def user_proxy(self,url,proxy,tipo):
		api = urllib2.Request(url)
		print '[+]Usando User-Agent do Script...\n'
		print '[+]User-Agent : Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19\n'
		try:
			api.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19')
		except:
			print '[+]Erro user-agent ;/'
			exit()
		try:
			proxy_1 = urllib2.ProxyHandler({tipo : proxy})
			pass
		except KeyError:
			print '[+]Erro Proxy/Formato Incorreto\n'
			exit()
		b1 = urllib2.build_opener(proxy_1)
		urllib2.install_opener(b1)
		try:
			return urllib2.urlopen(url).read()
		except KeyError:
			print '[+]Time-Out / ERRO PROXY..\n'
			exit()
	def proxy_user(self,url,proxy,tipo,useragent):
		api = urllib2.Request(url)
		print '[+]Usando User-Agent Definido Por Voce....\n'
		print '[+]User-Agent : %s\n' % useragent
		try:
			api.add_header('User-Agent',useragent)
		except:
			print '[+]Erro User-Agent ;/'
			exit()
		try:
			proxy_2 = urllib2.ProxyHandler({tipo : proxy})
		except:
			print '[+]Erro Proxy/Formato Incorreto...\n'
			exit()
		b2 = urllib2.build_opener(proxy_2)
		urllib2.install_opener(b2)
		try:
			return urllib2.urlopen(url).read()
		except:
				print '[+]Time-Out / ERRO PROXY'
				exit()
