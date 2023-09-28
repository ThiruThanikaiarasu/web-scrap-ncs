from bs4 import BeautifulSoup 
import requests

url = 'https://www.sarkariresult.com/latestjob/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
table_unordered_list = table.find_all('ul')

# table_list = table_unordered_list.find_all('li')
table_anchor = table.find_all('a')
href_values = [a['href'] for a in table_anchor]

# print(href_values)


# Iterate through the URLs
for href in href_values:
    # Send an HTTP GET request to the URL
    response = requests.get(href)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and print the details you need from the page
        # For example, let's extract and print the page title
        page_title = soup.find('h1')
        print(f"Title of the page at {href}: {page_title.text}")
        
        # You can extract other information as needed from the page

    else:
        print(f"Failed to retrieve data from {href}. Status code: {response.status_code}")
