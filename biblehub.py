import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://biblehub.com/asv/'
name='john'
random_chapter=random.randint(1,21)
webpage=webpage + name+'/'+str(random_chapter) +'.htm'
print(webpage)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage=urlopen(req).read()

soup=BeautifulSoup(webpage,'html.parser')

page_verses=soup.findAll("div",class_='main')

for verse in page_verses:
    verse_list=verse.text.split('.')
    #re.[]
print(verse_list)

myverse=random.choice(verse_list[:len(verse_list)-5])

#print(page_verses)

#print(f"Chapter: {random_chapter} , Verse: {myverse}")

message="Chapter: " +random_chapter+ "Verse: "+myverse
print(message)
