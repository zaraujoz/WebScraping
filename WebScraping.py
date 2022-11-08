import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []

response = requests.get('https://ge.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da noticia 
noticias = site.findAll('div', attrs={'class':'feed-post-body'})

for noticia in noticias:
    #Titulo, 'a' são as tags de links 
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    #print(titulo.text)
    #Link da noticia 
    #print(titulo['href'])

    #Subtitulo
    subtitulo = noticia.find('div', attrs={'class', 'feed-post-body-resumo'})

    #Verificando se o subtitulo existe, se exister sera capturado 
    if (subtitulo):
        print(subtitulo)
        #Salvando a lista com titulo, subtitulo e link
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '' , titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

#Salando a lista em formato de tabela excel
#news.to_excel('noticias.xlsx', index=False)

print(news)