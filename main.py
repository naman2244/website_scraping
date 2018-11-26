import requests
from bs4 import BeautifulSoup
import os, os.path, csv
import re

def checkeng(s):																						    #Function to check if city name is in English characters
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


page = requests.get('http://www.fallingrain.com/world/IN/')					
soup = BeautifulSoup(page.text, "html.parser")
weblinks=[]																								        #Weblinks is collection of 'relevant' URLS  
data=[]																									          #Data is where the results are stored
data.append(['state', 'city', 'latitude', 'longitude', 'elevation', 'population'])
url = 'http://www.fallingrain.com'

print("Web scraping has started")

soup1 = soup.findAll('li')																			  #Process to extract links on Home page
main_links = len(soup1)
for i in range(0, main_links):
	for a in soup1[i].find_all('a', href=True):
		zz = a['href']
		weblinks.append(url+zz)
	
n = len(weblinks)

#count=0

for i in weblinks:																					      #Each link is parsed and visited
	page_l = requests.get(i)
	soup_l = BeautifulSoup(page_l.text, "html.parser")
	
	tab = soup_l.findAll('table')
									#count = count+1
									#print(count)
	ww = len(tab)																						        #More than one form of table on a page may be present
	flag=0
	if(len(tab)>=1):
		for j in range(0, ww):																			  #Accessing all tables on page
			if(len(tab[j].findAll('th'))==8):													  #Checking if table found is relevant
				flag=1
				r = tab[j].findAll('tr')
				number = len(r)
				
				for q in range(1, number):																#Loop to add a valid row to ResultSet
				  city = r[q].findAll('td')[0].text
					if(checkeng(city)):
						state = r[q].findAll('td')[2].text
						latitude = r[q].findAll('td')[4].text
						longitude = r[q].findAll('td')[5].text
						elevation = r[q].findAll('td')[6].text
						population = r[q].findAll('td')[7].text
					
					
					
					data.append([state, city, latitude, longitude, elevation, population])
					
				
					
	if(len(tab)==1 and flag==0):																	   #Loop to add relevant URLS
		for rows_l in soup_l.findAll('a', attrs={'href': re.compile("/world/IN/")}):
			weblinks.append(url+rows_l.get('href'))
		
			
			
	
with open("final_data.csv", 'w', encoding='utf-8', newline='') as toWrite:											   #Segment to write data to CSV
    writer = csv.writer(toWrite)		
    writer.writerows(data)


#print(count)
#print("\n")
print("Done")
	
					
 
