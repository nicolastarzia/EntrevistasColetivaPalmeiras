# -*- coding: UTF-8 -*-
import scrapy
from scrapy.http import FormRequest
import json
import os.path

class PalmeirasSpider(scrapy.Spider):
    name = "Audios"
    urlAudio = 'http://www.palmeiras.com.br/audios/ajax_audios'
    countItens = 4
    page = 1
    dataAlreadyScraped = []

    def start_requests(self):
        if os.path.isfile('audios.json'):
            with open('audios.json') as data_files:
                self.dataAlreadyScraped = json.load(data_files)
        frmData = {
         'page': str(self.page),
         'count': str(self.countItens)
        }
        return [FormRequest(self.urlAudio, formdata=frmData, callback=self.parse)]

    def alExists(self, data, value):
        if data is None:
            return False
        return len([x for x in data if x['urlFile'] == value]) > 0

    def parse(self, response):
        audios = response.css('.boxAudio')
        if(audios != []): #Se nao tiver mais informacoes a variavel nao é preenchida
            for boxAudio in audios:
                calendario = boxAudio.css('.calAudio::text').extract_first()
                titulo = boxAudio.css('.titAudio::text').extract_first()
                urlFile = boxAudio.css('::attr(file)').extract_first()
                data = self.dataAlreadyScraped
                print(self.alExists)
                alExst = self.alExists(data=data, value=urlFile)
                if(alExst == True):
                    return
                yield {
                    'calendario': calendario,
                    'titulo': titulo,
                    'urlFile': urlFile
                }
            self.page = self.page + 1
            frmData = {
             'page': str(self.page),
             'count': str(self.countItens)
            }
            yield FormRequest(self.urlAudio, formdata=frmData, callback=self.parse)
