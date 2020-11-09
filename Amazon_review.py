import scrapy
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
 
    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['amazon.in']
 
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.co.uk/HORIZN-STUDIOS-Luggage-Suitcase-Lightweight/dp/B0778QWHW6?pf_rd_r=X55V4YCSMMADWHRV3A97&pf_rd_p=61faa84c-4386-462b-9257-9f1a062154b3&pd_rd_r=40694941-058b-4212-bd46-ad5f15f91baa&pd_rd_w=XluWI&pd_rd_wg=Y9Di3&ref_=pd_gw_unk&th=1"
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,146):
        start_urls.append(myBaseUrl+str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
 
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
 
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
 
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
