import scrapy 


Class BlogSpider(scrapy.Spider):

      name = 

start_urls = [
    'https://za.indeed.com/jobs?q=&l=South+Africa',
    "https://za.indeed.com/jobs?q=&l=South+Africa&start=10",
    'https://za.indeed.com/jobs?q=&l=South+Africa&start=20'
]

def parse(self, response):
    page = response.url.split('/')[-1]
    filename = 'posts-%s.html' % page 
    with open(filename, 'wb') as f:
        f.write(response.body)

