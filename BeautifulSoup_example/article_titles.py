import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example-news-website.com'

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
