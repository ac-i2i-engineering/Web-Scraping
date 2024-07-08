import scrapy

class ProductSpider(scrapy.Spider):
    name = "products"
    start_urls = ['https://example-ecommerce-website.com/products']

    def parse(self, response):
        # Extract product details
        for product in response.css('div.product-item'):
            yield {
                'name': product.css('h2.product-title::text').get(),
                'price': product.css('span.product-price::text').get(),
                'availability': product.css('span.availability::text').get()
            }

        # Follow pagination links (if any)
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
