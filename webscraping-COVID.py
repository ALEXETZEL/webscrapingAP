# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from cgi import test
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req= Request(url, headers=headers)

webpage=urlopen(req).read()

soup=BeautifulSoup(webpage,'html.parser')



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

table_rows=soup.findAll("tr")
high_death_rate=0
low_death_rate=100
high_test_rate=0
low_test_rate=100
#th is table head class
for row in table_rows[2:52]:
    td=row.findAll("td")
    state=td[1].text
    total_cases=float(td[2].text.rstrip('\n').replace(",",""))
    total_deaths=float(td[4].text.rstrip('\n').replace(",",""))
    total_tests=float(td[10].text.rstrip('\n').replace(",",""))
    population=float(td[12].text.rstrip('\n').replace(",",""))
    death_rate=round(((total_deaths/total_cases)*100),2)
    test_rate=round(((total_tests/population)*100),2)
    if low_death_rate>death_rate:
        low_death_rate=death_rate
        state_low_death=state
    if high_death_rate<death_rate:
        high_death_rate=death_rate
        state_high_death=state
    if high_test_rate<test_rate:
        high_test_rate=test_rate
        state_high_test=state
    if low_test_rate>test_rate:
        low_test_rate=test_rate
        state_low_test=state

        '''
    print(f'State: {state}')
    print(f'Total Cases: {total_cases}')
    print(f'Total Deaths: {total_deaths}')
    print(f'Total Tests: {total_tests}')
    print(f'Population: {population}')
    print(f'death rate: {death_rate}')
    print(f'test rate: {test_rate}')
    input()
    '''


print(f'High death rate: {high_death_rate}% State: {state_high_death}')
print(f'Low death rate: {low_death_rate}% State: {state_low_death}')
print(f'High test rate: {high_test_rate}% State:{state_high_test}')
print(f'Low test rate: {low_test_rate}% State: {state_low_test}')


    
