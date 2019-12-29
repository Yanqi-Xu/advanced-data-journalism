# import the library used for scraping
import requests
import mechanize
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# assign the string of the website to a variable called "url"
url = 'https://www.njconsumeraffairs.gov/phar/Pages/actions.aspx'

# Get the HTML of the page
# define the br function for browser
br = mechanize.Browser()
# use the br and add a dot notation
br.open(url)
# used the functinos to define the html
html = br.response().read()

# Transform the HTML into a BeautifulSoup object and parse it
soup = BeautifulSoup(html, "html.parser")

# Find what the tables contain
# The function identifies the objects for scraping by their ids
main_table = soup.find('tbody',
                       #{'class': 'mrc_main_table'}
                       )
# Use the findall() methodto loop through every <tr>element
#row_list = main_table.find_all('tr')
print(main_table)
# Use a for loop to get the data from each table row
# for r in row_list:
# Find the individual entries in the cells of the same row
#cell_list = r.find_all('td')
# If the row is not empty, then find what's in the cells and print them one by one, also removing whitespaces
"""     if len(cell_list) > 0:
        for c in cell_list:
            print c.text.strip() """
# Add a divider in the form of '----------'
# print '----------'

print('IT WORKED!')
