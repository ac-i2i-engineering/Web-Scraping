# Web Scraping using scrapy

Scrapy is a powerful, full-fledged web scraping framework designed for handling large-scale and complex scraping projects. Its asynchronous requests, managed by the Twisted networking library, enable efficient and fast scraping, making it ideal for crawling large websites and processing multiple pages simultaneously. 

Scrapy’s built-in support for crawling allows for easy link following and data extraction across an entire site. The framework also offers item pipelines for processing scraped data, middleware for managing requests and responses, and a structured project layout that facilitates the organization and maintenance of large scraping projects. With extensive documentation and a large community, Scrapy is suitable for tasks requiring scalability, efficiency, and robustness, such as aggregating data from multiple sources, monitoring websites for changes, and scraping e-commerce sites for product information.

## Preparation

1. Use this line to install scrapy on your terminal/shell/command prompt window:

```
pip install scrapy
```
2. Navigate to the folder where you want to start your new project, and use this command line to start a project using scrapy:

```
scrapy startproject ecommerce_scraper

```

## Explanation of the Example of Ecommerce scraping

for product in response.css('div.product-item'): Iterates through each product item on the page.

Extracts the product name, price, and availability using CSS selectors. Adjust the selectors based on the actual HTML structure of the target website.

Handles pagination by following the "next page" link and continuing to scrape.

## Execution

To run the scrapper, navigate to the appropriate directory in the terminal/shell again and run this command line argument:

```
scrapy crawl products -o products.json
```

## Respecting the websites' rules

Scrapy has built-in support for respecting robots.txt files. By default, Scrapy respects the robots.txt rules of the websites it scrapes. 

You can see more advanced examples and functions using scrapy on its official documentation page: https://docs.scrapy.org/en/latest/


