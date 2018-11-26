Website Scraping:
The project aims at preparing a CSV file which categorizes data about into State, City, Latitude, Longitude, Elevation, and 		Estimated Population
	
The link of the website which needs to be scraped: http://www.fallingrain.com/world/IN/

File to be executed: main.py 

Languages Used: Python

Libraries Required: requests, bs4 (Beautiful Soup), os, csv and re

Installation:
To run the file, mainly some of installation would be required.	
1. Python 3 
2. Requests – can be downloaded by using pip install requests
3. Bs4 -  can be downloaded by using pip install bs4

Approach:
Python is chosen as it supports significant libraries to support web scraping. The aim was to parse all the relevant URLs and extract 	the data from them. So, from the main page all the URLs were stored in a data structure and then one by one each of them were visited. 	On the visit to a page, it was found that 2 types of table might be present i.e. one with map embedded in it and other with the required data entries. A page may contain 3 types of responses:  	
1) URLs to some other pages containing data entries (Like in Rajasthan we have A followed by Aj)
2) URLS along with map (in the form of table)
3) Map along with a valid data table (or entry).
The relevant links found on the page were added to the data structure; otherwise the page was looked upon for 8 <th> tags. If found then the rows, beside the header row, are added to the ResultSet. Finally, the data stored in form of list is written to the CSV file.
