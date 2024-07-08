# Web Scaping using BeautifulSoap and Requests

BeautifulSoup is a flexible and intuitive HTML and XML parsing library that excels in handling poorly formatted markup. It provides a simple and straightforward API, making it ideal for small to medium-sized scraping tasks where quick data extraction from specific parts of HTML documents is needed. 

BeautifulSoup can be easily combined with the Requests library for making HTTP requests, allowing for manual handling of web page downloads and parsing. Its support for multiple parsers, such as lxml and html5lib, provides versatility in dealing with different types of HTML. 

BeautifulSoup is perfect for quick prototyping, one-off scraping scripts, and projects where you need to extract data from a few pages or specific elements without the overhead of setting up a full project structure. It is well-suited for tasks like extracting information from specific web page sections, scraping data from blogs, and processing simple web forms.

## Preparation

Before trying out this example, please use this like to install the necessary libraries:

```
pip install requests beautifulsoup4
```

## Explanation of the Example

In this example the the code first sends a request to the specified URL and stores the response. Ensures the request was successful before attempting to parse the content. It then parses the HTML content of the page using BeautifulSoup. To do so, it finds all h2 tags with the class article-title, and adjusts this selector based on the actual HTML structure of the target website.

## Customization

Apart from chaing the url variable to the website that we want to scrap, we can adjust the selector in soup.find_all to match the HTML structure of the data you want to scrape. You can inspect the HTML structure using browser developer tools.

## Respecting websites' rules

Websites have a file called 'robots.txt' which lay out the rules for the website, and it is crucial to adhere to them so that legal and ethical boundaries are not breached. When using BeautifulSoap it is important to take extra care of this as the library itself does not ensure this be default. 

To implement a safe algorithm first do more installation:

```
pip install requests robotexclusionrulesparser
```

The 'is_allowed' function in the example shows how the code checks the website's robots.txt and essentially ensures that it has permission to scrap the website. The rest of the code is in an if statement and will only be executed if permission is granted.

For more advanced use cases, you can find documentation for BeautifulSoup here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

