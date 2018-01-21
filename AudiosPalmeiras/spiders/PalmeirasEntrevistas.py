import scrapy
from scrapy.http import FormRequest

class PalmeirasSpider(scrapy.Spider):
    name = "Audios"
    urlAudio = 'http://www.palmeiras.com.br/audios/ajax_audios'
    countItens = 4
    page = 1

    def start_requests(self):
        arrUrls = []
        for i in range(1,2):
            frmData = {
             'page': str(i),
             'count': str(self.countItens)
            }
            arrUrls.append(FormRequest(self.urlAudio, formdata=frmData, callback=self.parse))
        return arrUrls
#        yield scrapy.Request(url=self.urlAudio, method='POST', body=frmData, callback=self.parse)


    def parse(self, response):
        if(response.body != ''):
            for boxAudio in response.css(".boxAudio"):
                yield {
                    'calendario' : boxAudio.css('.calAudio::text').extract_first(),
                    'titulo' : boxAudio.css('.titAudio::text').extract_first(),
                    'urlFile' : boxAudio.css('::attr(file)').extract_first()
                }
            self.page = self.page + 1
            frmData = {
             'page': str(self.page),
             'count': str(self.countItens)
            }
            yield FormRequest(self.urlAudio, formdata=frmData, callback=self.parse)
