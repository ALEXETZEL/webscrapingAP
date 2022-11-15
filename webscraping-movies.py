
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

table=soup.findAll('tr')
rows=soup.findAll('tr')

for x in rows[1:6]:
    cell=x.findAll("td")
    rank=(cell[0].text)
    name=(cell[1].text)
    total_gross=(cell[7].text)
    distributor=cell[9].text
    avg_gross=float(total_gross.replace(',',"").replace('$',""))/float((cell[6].text.replace(',',"").replace('$',"")))

    print(f'Rank: {rank}')
    print(f'Movie Name: {name}')
    print(f'Total Gross: {total_gross}') 
    print(f'Distributor: {distributor} ')
    print(f'Average per Theatre: {"${:,.2f}".format(avg_gross)}')
    print()
    print()