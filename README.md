Versão Atualizada : v0.5 build
Correções:<br>
--Paginas sem resultado gerava erro<br>
--Erro no comando --paginas<br>
--Pequeno erro quando não sé usava user-agent<br>
--Erro Json Paginas<br>
Novidades:<br>
--Conexão com Cookies<br>

------------------------------

Essa versão foi mais pra correção de bugs :) 
E aproveitem meus doces :p

Resultado:

<img src= "http://puu.sh/dFMUQ/3d53665e67.png" ></img>

Obs:Não é obrigatório usar todas os comandos,tente usar so um :)
Ex:

script.py --dork=inurl:noticia.php?id=1 --arquivo=meu.txt

Nesse comando acima você recebe 10 resultados


script.py --dork=inurl:noticia.php?id=1 --arquivo=meu.txt --paginas=2

Já com este você recebera 20 ,porque 20?
Porque você vai em 2 paginas e cada pagina da dork contem 10 resultados sendo assim 10+10 = 20 :D


script.py --dork=inurl:noticia.php?id= --arquivo=meu.txt --reigelado-mode

No modo reigelado não coloque numeros depois do = na sua dork,porque o script vai sair adicionando no loop o que da mais resultados exemplo:
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

[/i]
[code]script.py --dork=news.php?id= --reigelado-mode --arquivo=100.txt  --useragent-random[/code]
[i]

Retornaria:

<img src = 'http://puu.sh/dFO0g/cf020fa83b.png' ></img>
<img src = 'http://puu.sh/dFO1Z/60d2918342.png' ></img>

Resultado .txt:

<img src = 'http://puu.sh/dFOnw/6389298a88.png' ></img>
#como vocês podem observar a barrinha de rolar do notepad esta pequena de tantos resultados que o script retornou(esqueci de desligar ehuehue)
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
