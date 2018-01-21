import json
import requests
import os
import validators

def carregarArquivoLocal():
    with open('audios.json') as data_file:
       return json.load(data_file)

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
    open(caminhoDoArquivo, 'wb').write(r.content)

arquivos = carregarArquivoLocal()
for arquivo in arquivos:
    urlArquivo = arquivo['urlFile']
    if validators.url(urlArquivo):
        extensaoArquivo = urlArquivo.split('.')[-1].split('?')[0].strip()
        nomeArquivo = ExtrairNomeDoArquivo(arquivo['titulo']).strip()
        dataArquivo = ExtrairDatasCalendario(arquivo['calendario'])
        diretorioArquivo = CriarDiretorio(dataArquivo['ano'], dataArquivo['mes'])
        caminhoDoArquivo = '{0}/{1}.{2}'.format(diretorioArquivo, nomeArquivo, extensaoArquivo)
        DownloadArquivo(urlArquivo, caminhoDoArquivo)
        print('{0} - {1}'.format(urlArquivo, caminhoDoArquivo))

