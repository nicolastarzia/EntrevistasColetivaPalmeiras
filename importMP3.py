import json
import requests
import os
import validators


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

arquivos = carregarArquivoLocal()
for arquivo in arquivos:
    urlArquivo = arquivo['urlFile']
    urlArquivo = CorrigirURLArquivo(urlArquivo)
    if validators.url(urlArquivo):
        extensaoArquivo = urlArquivo.split('.')[-1].split('?')[0].strip()
        nomeArquivo = ExtrairNomeDoArquivo(arquivo['titulo']).strip()
        dataArquivo = ExtrairDatasCalendario(arquivo['calendario'])
        diretorioArquivo = CriarDiretorio(dataArquivo['ano'], dataArquivo['mes'])
        caminhoDoArquivo = '{0}/{1}{2}.{3}'.format(diretorioArquivo,dataArquivo['dia'], nomeArquivo, extensaoArquivo)
        if not os.path.exists(caminhoDoArquivo):
            print(urlArquivo)
            print(caminhoDoArquivo)
            DownloadArquivo(urlArquivo, caminhoDoArquivo)
            print('{0} - {1}'.format(urlArquivo, caminhoDoArquivo))

