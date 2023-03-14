import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

# Create counter variable to scape all webpages
counter = 0

#  Create Dict for types
rents = {'House': 0, 'Apartment': 0}

#  First while statement to catch promo'd ads
try:
    while counter <= 1300:
        # Access Daft.ie via Url for all of Ireland and save response for reach webpage
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        webpage_response = requests.get(url)
        webpage = webpage_response.content
        #  Create soup
        soup = BeautifulSoup(webpage, "html.parser")
        listings = soup.find_all('div', class_='SubUnit__CardInfoItem-sc-10x486s-7 YYbRy')

        #  Loop through returns and sort into Apartment or House
        for listing in listings:
            try:
                text = listing.text
                type = text.split('·')[2].strip(' ')
                for place in rents:
                    if place in type:
                        rents[place] += 1
                    else:
                        rents['Apartment'] += 1
            except:
                pass
        counter += 20
except:
    pass

# Reset Counter
counter = 0

#  Second while statement to catch non-promo'd ads

try:
    while counter <= 1300:
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        webpage_response = requests.get(url)
        webpage = webpage_response.content

        #  Create second Soup
        soup = BeautifulSoup(webpage, "html.parser")
        listings = soup.find_all('div', class_='Cardstyled__TitleBlockWrapper-nngi4q-4 eMeJos')

        # Loop through each listing and extract the price
        for listing in listings:
            # Find the price element within the listing
            price_element = listing.find(attrs={'data-testid': 'property-type'})
            # Extract the text content of the price element
            price = price_element.text.strip()
            for place in rents:
                if place in price:
                    rents[place] += 1
                else:
                    pass
        counter += 20
except:
    pass

print(rents)
