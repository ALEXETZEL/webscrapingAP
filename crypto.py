
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

import keys2

from twilio.rest import Client

client=Client(keys2.accountSID, keys2.authToken)

TwilioNumber='+18585445760'
myCellPhone='+18327767907'


url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req= Request(url, headers=headers)
webpage=urlopen(req).read()
soup=BeautifulSoup(webpage,'html.parser')

rank=0
rows=soup.findAll('tr')



for x in rows[1:6]:
    cell=x.findAll('td')
    p=x.findAll("p")
    div=cell[3].findAll('div')
    rank+=1
    curreny=p[0].text
    symbol=cell[2].text
    symbol=symbol.replace(curreny,'')
    if symbol=='':
        symbol='None'
    price=div[0].text
    change=cell[4].text
    price=price.replace(change,'')
    print(f' Rank: {rank}')
    print(f' Name: {curreny} ')
    print(f' Symbol: {symbol} ')
    print(f' Current Price: {price}')
    print(f' 24hr %Change: {change}')
    print()
    print()
    
    
    if symbol=='BTC' and float(price.replace('$','').replace(',',''))<40000:
        textmessage=client.messages.create(to=myCellPhone, from_=TwilioNumber, body='The Price of Bitcoin has fallen below $40,000. The current price of Bitcoin is '+ price)
        #print(textmessage.status)
    if symbol=='ETH' and float(price.replace('$','').replace(',',''))<3000:
        textmessage=client.messages.create(to=myCellPhone, from_=TwilioNumber, body='The Price of Ethereum has fallen below $3,000. The current price of Ethereum is '+ price)
        #print(textmessage.status)
    