import requests
from bs4 import BeautifulSoup
from robotexclusionrulesparser import RobotExclusionRulesParser


# Function to check if a URL is allowed to be scraped
def is_allowed(url, user_agent='*'):
    domain = '/'.join(url.split('/')[:3])
    robots_url = f"{domain}/robots.txt"
    response = requests.get(robots_url)

    if response.status_code == 200:
        rp = RobotExclusionRulesParser()
        rp.parse(response.text)
        return rp.is_allowed(user_agent, url)
    return True
    
# URL of the website to scrape
url = 'https://example-news-website.com'

if is_allowed(url):
# Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find all article titles
        # This will vary based on the website's HTML structure. Adjust the selector as needed.
        titles = soup.find_all('h2', class_='article-title')
    
        # Print out the titles
        for title in titles:
            print(title.get_text())
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

else:
    print("Scraping is not allowed by robots.txt")
