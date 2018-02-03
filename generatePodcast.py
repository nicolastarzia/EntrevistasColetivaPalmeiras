import json
import validators
import requests
import os
from feedgen.feed import FeedGenerator



def carregarArquivoLocal():
    with open('audios.json') as data_file:
       return json.load(data_file)

def CorrigirURLArquivo(urlArquivo):
    urlArquivo = urlArquivo.split('?')[0].lower()
    if(not urlArquivo.endswith(('.mp3','.mp4','.m4a','.wav'))):
        urlArquivo = urlArquivo + '.mp3'
    return urlArquivo

def ExtrairNomeDoArquivo(titulo):
    nomeArquivo = titulo.replace('/','-') #Folder structure
    return nomeArquivo[:255] #Max file length

def ExtrairDatasCalendario(calendario):
    dataDoArquivo = calendario.split('-')[0].split('/')
    return {
        'ano': dataDoArquivo[2].strip(),
        'mes': dataDoArquivo[1],
        'dia': dataDoArquivo[0]
    }

def CriarDiretorio(ano, mes):
    diretorioArquivo = 'mp3/{0}/{1}'.format(ano, mes)
    if not os.path.exists(diretorioArquivo):
        os.makedirs(diretorioArquivo)
    return diretorioArquivo

def DownloadArquivo(urlArquivo, caminhoDoArquivo):
    r = requests.get(urlArquivo, allow_redirects=True)
    if(r.status_code == requests.codes.ok):
        open(caminhoDoArquivo, 'wb').write(r.content)
    else:
        open('urlswithproblem.json', 'wb').write(urlArquivo + ';' + caminhoDoArquivo + '\n')



fg = FeedGenerator()
fg.id('https://nicolastarzia.com/audiospalmeiras')
fg.title('Palmeiras - Entrevistas coletivas')
fg.author({'name':'Nicolas Tarzia', 'email':'podcastpalmeiras@nicolastarzia.com'})
fg.link(href='http://www.palmeiras.com.br', rel='alternate')
fg.logo('http://static.palmeiras.com.br/content/public/upload/imagem/times/imagem_20_original.png')
fg.subtitle('Podcast com as entrevistas coletiva do Palmeiras')
fg.link(href = 'https://nicolastarzia.com/palmeiras.atom',rel='self')
fg.language('pt-BR')

arquivos = carregarArquivoLocal()
for arquivo in arquivos:
    urlArquivo = arquivo['urlFile']
    urlArquivo = CorrigirURLArquivo(urlArquivo)
    if validators.url(urlArquivo):
        fe = fg.add_entry()
        fe.id(urlArquivo)
        fe.title('')
        fe.content('')
        fe.link(href='http://palmeiras.com.br/audios', rel='alternate')
        fe.author(name='Nicolas Tarzia', email='podcastpalmeiras@nicolastarzia.com')

fg.load_extension('podcast')
fg.podcast.itunes_author('Nicolas Tarzia')
fg.podcast.itunes_category('Sport')
fg.podcast.itunes_explicit('no')
fg.podcast.itunes_complete('no')
fg.podcast.itunes_new_feed_url('https://nicolastarzia.com/palmeiras.rss')
fg.podcast.itunes_owner('Nicolas Tarzia','podcastpalmeiras@nicolastarzia.com')
fg.podcast.itunes_summary('Podcast com todos os audios da entrevista coletivas do Palmeiras')
fg.rss_str(pretty=True)
fg.rss_file('podPalmeiras.rss')
