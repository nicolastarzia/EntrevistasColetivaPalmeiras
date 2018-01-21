## Objetivos
O principal objetivo deste projeto é disponibilizar o arquivo com todas as coletivas realizadas pela Sociedade Esportiva Palmeiras.
- Catalogar todos os arquivos de maneira didatica, atualmente todos os arquivos estão com nomes de dificil entendimento.

## Futuro
Em um futuro proximo, disponibilizar o formato de Podcast de todas as entrevistas coletivas, e principalmente manter atualizado as informações.
Utilizar inteligencia cognitiva para entender como foi a entrevista coletiva (calma, exaltada, etc)

## Como executar
Este projeto foi construido em *Python*, e foi dividido em duas partes:

Primeira parte, é a construção do arquivo JSON com com as seguintes informações:
    - Data da coletiva
    - Breve informação disponibilizada no site
    - URL do arquivo de audio

Dependencias:
    - scrapy - [sudo] pip install scrapy


Procedimento para executar:
    - scrapy crawl Audios -o audios.json


Segunda etapa, é o download de todos os audios das entrevistas.
A estrutura de download dos arquivos são:
    - mp3 / {ano} / {mês} / arquivo de audio

Dependencias:
    - requests - [sudo] pip install requests
    - os
    - JSON
    - validators - [sudo] pip install validators

Procedimento para executar:
    - python importMP3.py
