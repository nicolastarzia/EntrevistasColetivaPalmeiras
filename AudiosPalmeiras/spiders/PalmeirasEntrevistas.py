# -*- coding: UTF-8 -*-
import scrapy
from scrapy.http import FormRequest
class PalmeirasSpider(scrapy.Spider):
    name = "Audios"
    urlAudio = 'http://www.palmeiras.com.br/audios/ajax_audios'
    countItens = 4
    page = 1

    def start_requests(self):
        frmData = {
         'page': str(1),
         'count': str(self.countItens)
        }
        return [FormRequest(self.urlAudio, formdata=frmData, callback=self.parse)]
    def parse(self, response):
        audios = response.css('.boxAudio')
        if(audios != []): #Se nao tiver mais informacoes a variavel nao é preenchida
            for boxAudio in audios:
                calendario = boxAudio.css('.calAudio::text').extract_first()
                titulo = boxAudio.css('.titAudio::text').extract_first()
                urlFile = boxAudio.css('::attr(file)').extract_first()
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
