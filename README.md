Google-Dork-Scan
================
Dicas,sé não sou souber como usar o dork utilize o comando.

Código:

script.py -h

print:http://puu.sh/dBZCF/5ad454e264.png

Obs:Não é obrigatório usar todas os comandos,tente usar so um :)

Ex:

Código: 

script.py --dork=inurl:noticia.php?id=1 --arquivo=meu.txt


Nesse comando acima você recebe 10 resultados


Código: 

script.py --dork=inurl:noticia.php?id=1 --arquivo=meu.txt --paginas=2


Já com este você recebera 20 ,porque 20?
Porque você vai em 2 paginas e cada pagina da dork contem 10 resultados sendo assim 10+10 = 20 :D


Código: 

script.py --dork=inurl:noticia.php?id= --arquivo=meu.txt --reigelado-mode


No modo reigelado não coloque numeros depois do = na sua dork,porque o script vai sair adicionando no loop o que da mais resultados exemplo:

Loop1:
noticia.php?id=1

Loop2:
noticia.php?id=2

Loop3:
noticia.php?id=3

Dica sé você quiser dorks de um pais especifico utilize os dominios dele nas dorks
Exemplo(Dorks do Brasil):

Código: 

script.py --dork=inurl:.com.br/noticia.php?id=1 --arquivo=meutxt.txt

Da india:

Código: 

script.py --dork=inurl:.in/noticia.php?id=1 --arquivo=meutxt.txt


Obs as regras dos comandos --paginas e --reigelado-mode valem do mesmo jeito pros dominios diferenciados e as dorks podem não retornar resultados legais porque noticia não sé escreve do mesmo jeito em indiano kkk


Obs eu não aconselho usar as funções --paginas e --reigelado-mode juntas 


(Atualização - Quinta Feira 18 de dezembro de 2014) -- Google Dork Scan v0.1

Google fechou sua api publica,portanto google dork scan by Rei_Gelado não esta funcionando no momento mais estou providenciando uma key para a nova API.

(Atualização - Sexta Feira 19 de dezembro de 2014) -- Google Dork Scan v0.2

Atualize o dork scan para a api fechado do google que requer uma key que encontrei na internet mais você pode obter ela no google.com/cse.
A api para mais 'bugada' pois retorna menos resultados do que em uma busca normal .
Exemplo:
Google normal...
inurl:/noticia.php?id= (milhões de resultados)
Api
inurl:/noticia.php?id= (463 resultados e oscilando)
E quase toda vez ele retorna um 403.
Resumindo a versão free da API e um lixo.
Mais da pra brincar com as dorks :)

(Atualização - Sabado 20 de dezembro de 2014) -- Google Dork Scan v0.3

Correção de Bugs:

-- 403 Google

-- arguments.pagina ficando sempre false

Novidades:

-- Modo ReiGelado(Sem criatividade pra nome) que você consegue gerar mais de 100 dorks

-- Escolha de Key api de forma randomica :D

-- sleeps para ajudar no 403 do google :D

-- except para Dorks sem resultados

Futuro:

-- Test de vulnerabilidades nos links encontrados(blind sqli)

-- Test de Fopen
