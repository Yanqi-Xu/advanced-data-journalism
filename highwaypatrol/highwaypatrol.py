import requests, mechanize

from bs4 import BeautifulSoup


url = 'https://www.mshp.dps.missouri.gov/HP71/search.jsp'


br = mechanize.Browser()

br.open(url)

html = br.response().read()


soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table',
    {'class': 'accidentOutput'}
)

row_list = main_table.find_all('tr')


for r in row_list:

    cell_list = r.find_all('td',{'class': 'infoCell'})

    if len(cell_list) > 0:
        for c in cell_list:
            print c.text.strip()

        print '----------'
print 'IT WORKED!'