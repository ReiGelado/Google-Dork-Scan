Versão Atualizada : v0.6
Correções:<br>
--Verificação de arquivos(caso alguem não baixe...)<br>
--Erro em uma função da classe ReiGelado(Esqueci uma aspas rsrsr)<br>
Novidades:<br>
--Adicionando comando --api-antiga que sé conecta a api velha do google.....
--Adicionado o script que futuramente sera usado para threads no google dork :)(ainda off)

------------------------------

Comando script.py -h

Resultado:

<img src= "http://puu.sh/dKCgU/38bd120031.png" ></img>

Obs:Não é obrigatório usar todas os comandos,tente usar so um :)
Ex:

script.py --dork=inurl:noticia.php?id=1 --arquivo=meu.txt

Nesse comando acima você recebe 10 resultados

No modo reigelado não coloque numeros depois do = na sua dork,porque o script vai sair adicionando no loop o que da mais resultados exemplo:

Ex:
script.py --dork=inurl:noticia.php?id= --arquivo=meu.txt --reigelado-mode


Loop1:
noticia.php?id=1
Loop2:
noticia.php?id=2
Loop3:
noticia.php?id=3

Dicas user-agents....

Comando --useragent-escolha

Exemplo de comando...

Obs na hora de usar este comando sempre na hora de por o user-agent
depois do iqual coloque uma aspas , veja no código abaixo.

script.py --dork=noticia.php?id= --reigelado-mode --arquivo=100.txt --useragent-escolha="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0"

Retornaria:

<img src = 'http://puu.sh/dFNu9/23fc53c0e7.png' ></img>
<img src = 'http://puu.sh/dFNwy/238ec50201.png' ></img>
<img src = 'http://puu.sh/dFNB4/13d52ad836.png' ></img>

Print Resultado .txt:

Talvez ele retorne alguns resultados estranhos mais e so ignorar :p

<img src = 'http://puu.sh/dFNHl/16c65c3600.png' ></img>
<img src = 'http://puu.sh/dFNKr/1b941f5a50.png' ></img>

Comando --useragent-random

Essa opção ainda esta na beta mais e otima porque a cada conexão que ele cria com um servidor o User-Agent e trocado.

Exemplo de comando:

script.py --dork=news.php?id= --reigelado-mode --arquivo=100.txt  --useragent-random

Retornaria:

<img src = 'http://puu.sh/dFO0g/cf020fa83b.png' ></img>
<img src = 'http://puu.sh/dFO1Z/60d2918342.png' ></img>

Resultado .txt:

<img src = 'http://puu.sh/dFOnw/6389298a88.png' ></img>

Como vocês pode observar ele retornou muitos resultados....

<img src = 'http://puu.sh/dFOsI/2994a9f8e5.png' ></img>

Alguns resultados podem vir errados mais isto e pro lado do google na proxima versão vou desenvolver um script que vai parsear os valores corretos :)

Comando --useragent-txt

Bom este comando eu demorei a cria digamos que deu um trabalinho mais valeu a pena bom vamos explicar ele :)
Lembrando na hora de botar o script pra ler o arquivo ele deve estar organizado da seguinte maneira:

User-Agent1
User-Agent2
User-Agent3


Cada user agente em uma linha nada de misturar nada sé não o script não vai ler...
Bom ele vai pegar os User-agents do .txt e criar uma lista e a partir de cada conexão escolher um de forma aleatoria

Exemplo de comando:

script.py --dork=news.php?id= --reigelado-mode --arquivo=100.txt  --useragent-txt=4.txt

Vai gerar o mesmo resultado dos prints acima :)

Na versão v0.6 adicionei um sisteminha de Proxy :p.
Os comandos adicionados ao script foram...

--proxy-tipo="http" # ou https , socks5 ou socks4 #Prescisa do comando --proxy-ip

--proxy-ip="127.0.0.1:2424" IP+PORTA #Prescisa do comando --proxy-tipo

--useragent-proxy="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)" #Não e obrigatorio

User-Agent padrão : Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19

Exemplo de comando:

script.py --dork=inurl:noticia.php?id=  --arquivo=caveiratech.txt --proxy-ip="199.200.120.140:7808" --proxy-tipo="http" --reigelado-mode

Resultado:

<img src = "http://puu.sh/dKCDs/4765e25bbb.png" ></img>
<img src = "http://puu.sh/dKCG4/bf86601456.png"></img>

Resultado .TXT:

<img src = "http://puu.sh/dKCHX/c005e5cca1.png" ></img>

Exemplo de comando:
 
script.py --dork=inurl:noticia.php?id=  --arquivo=caveiratech.txt --proxy-ip="199.200.120.140:7808" --proxy-tipo="http" --useragent-proxy="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)" --reigelado-mode


Resultado:

<img src = "http://puu.sh/dKD8k/28c439c116.png" ></img>
<img src = "http://puu.sh/dKDaF/4b8ed0342b.png" ></img>

Resultado .TXT:

<img src = "http://puu.sh/dKDdX/8d4bdec45d.png" ></img>
<img src = "http://puu.sh/dKDfW/3866053e56.png" ></img>


Na versão v0.7 adicionei a opção --api-antiga que sé conecta a versão antiga da api do google....
Aproveitem ela porque ela não tem limites de conexões então você pode estravassar....
Lembrando que por padrão ela retorna so 4 resultados então recomendo você usar ela com o comando --reigelado-mode
Que você tera mais proveito :D

Comando:

script.py --dork=inurl:noticia.php?id=1 --arquivo=github.txt --api-antiga

Resultado:

<img src = "http://puu.sh/dV4Dr/ddf3fdec38.png" ></img>
<img src = "http://puu.sh/dV4LZ/e375a4fdc0.png" ></img>

.TXT:

<img src = "http://puu.sh/dV4P7/49dc8ac267.png"></img>

Comando:(com --reigelado-mode)

script.py --dork=inurl:noticia.php?id=1 --arquivo=github.txt --api-antiga --reigelado-mode

Resultado:

<img src = "http://puu.sh/dV4Zx/02a616497a.png"></img>
<img src = "http://puu.sh/dV53b/68f9859eaf.png"></img>
<img src = "http://puu.sh/dV55h/2cce04db62.png"></img>
<img src = "http://puu.sh/dV573/915570e941.png"></img>
E teve mais algunas paginas rsrsrs...


.TXT:(Me retornou 49 resultados...:))

<img src = "http://puu.sh/dV5ad/b2f588d85d.png"></img>



Dica sé você quiser dorks de um pais especifico utilize os dominios dele nas dorks 
Exemplo(Dorks do Brasil):

script.py --dork=inurl:.com.br/noticia.php?id=1 --arquivo=meutxt.txt

Da india:

script.py --dork=inurl:.in/noticia.php?id=1 --arquivo=meutxt.txt

Obs as regras dos comandos --paginas e --reigelado-mode valem do mesmo jeito pros dominios diferenciados e as dorks podem não retornar resultados legais porque noticia não sé escreve do mesmo jeito em indiano kkk


Obs2 eu não aconselho usar as funções --paginas e --reigelado-mode juntas 
:)

Obs3  Sé o script der 403 isso e mais ou menos bom porque ele ja estorou o limite da API que são 1mil solicitações por dia...
Em breve vou ajeitar isso com umas contas fakes :)

Acho que eu mereço um Star no meu projeto do Git né <3 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />O trabalho <span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Google Dork Scan</span> de <a xmlns:cc="http://creativecommons.org/ns#" href="http://caveiratech.com/forum/profile/reigelado/" property="cc:attributionName" rel="cc:attributionURL">Rei_Gelado</a> está licenciado com uma Licença <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons - Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional</a>.<br />Baseado no trabalho disponível em <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/ReiGelado/Google-Dork-Scan/blob/master/google.py" rel="dct:source">https://github.com/ReiGelado/Google-Dork-Scan/blob/master/google.py</a>.<br />Podem estar disponíveis autorizações adicionais às concedidas no âmbito desta licença em <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/ReiGelado/Google-Dork-Scan/" rel="cc:morePermissions">https://github.com/ReiGelado/Google-Dork-Scan/</a>.
