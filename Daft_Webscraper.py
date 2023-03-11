import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime


# Create counter variable to scape all webpages
counter = 0

# List for prices to be added too
rent_price_list = []

try:
    while counter <= 1300:
        # Access Daft.ie via Url for all of Ireland and save response for reach webpage
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        webpage_response = requests.get(url)
        webpage = webpage_response.content

        # Parse each response to get all text
        soup = BeautifulSoup(webpage, "html.parser")
        cards = soup.find_all(class_ = "Cardstyled__TitleBlockWrapper-nngi4q-4 eMeJos")
        text = soup.getText()

        # Wrangle the text to usable state to extract the numerical price
        listings = text.split("HighPrice High to Low Map")
        Listings_joined = ' '.join(listings)
        next = Listings_joined.split("Save")

        for i in range(len(next)):
            m = next[i].split('€')
            try:
                rent_price_list.append(m[1][:6])
            except:
                pass
        counter += 20
except:
    pass

print('scaping complete')

# Convert weekly to monthly prices
for index, val in enumerate(rent_price_list):
    if 'p' in val:
        i = val[:3]
        i = round(((int(i)*52)/12))
        rent_price_list[index] = 5 * round(i / 5)

    else:
        rent_price_list[index] = val

print('wrangling complete')


# Create data variable
date = datetime.datetime.now().strftime("%d-%m-%Y")

# Save to CSV
df = pd.DataFrame(rent_price_list)
df.to_csv("Daft_non_shared_renting_" + str(date) +".csv", index=False)
print('Process Complete :)')