# import libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# specify the url
quote_page = 'web_link_specific_region'


data = []

req = Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


event_footer = soup.find_all('div', attrs={'class': 'festival-card__footer'})

for e in event_footer:
	name_box = e.find('a', attrs={'class': 'festival-card__title truncate gray-link'})
	event_name = name_box.text.strip() # strip() is used to remove starting and trailing
	event_link = 'web_link' + name_box['href']
	festival_date_box = e.find('span', attrs={'class': 'festival-card__date'})
	festival_date = festival_date_box.text.strip() # strip() is used to remove starting and trailing
	festival_location_box = e.find('span', attrs={'class': 'festival-card__location truncate'})
	festival_location = festival_location_box.text.strip() # strip() is used to remove starting and trailing

	req_details = Request(event_link, headers={'User-Agent': 'Mozilla/5.0'})
	details_page = urlopen(req_details).read()

	# parse the html using beautiful soup and store in variable `soup`
	dsoup = BeautifulSoup(details_page, 'html.parser')

	event_details_box = dsoup.find_all('div', attrs={'class': 'card-white'})
	for ed in event_details_box:
		if 'About This Festival' in ed.find('h4').text.strip():
			event_details = event_details_box.text.strip()

	data.append((event_name, festival_date, festival_location, event_link, event_details))
	#print(datetime.now(),event_name, festival_date, festival_location, event_link)

# open a csv file with append, so old data will not be erased
with open('festivals_details.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
# The for loop
	for event_name, festival_date, festival_location, event_link, event_details in data:
		writer.writerow([datetime.now(), event_name, festival_date, festival_location, event_link, event_details])
