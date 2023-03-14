import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

# Create counter variable to scape all webpages
counter = 0
dic = {}
index = 0
xx = []

#  Create Dict for types
rents = {'House': 0, 'Apartment': 0, 'Studio':0}

#  First while statement to catch promo'd ads
try:
    while counter <= 60:
        # Access Daft.ie via Url for all of Ireland and save response for reach webpage
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        webpage_response = requests.get(url)
        webpage = webpage_response.content
        #  Create soup
        soup = BeautifulSoup(webpage, "html.parser")
        listings = soup.find_all('div', class_='SubUnit__CardInfoItem-sc-10x486s-7 YYbRy')
        prices = soup.find_all('div',class_="SubUnit__StyledCol-sc-10x486s-4 bIjqYp")
        for price in prices:
            try:
                prop_type = price.find(attrs={'data-testid': 'sub-title'})
                z = prop_type.text.strip()
                xx.append(z)
            except:
                pass
        print(len(xx))

         # Loop through returns and sort into Apartment or House
        for listing in listings:
            try:
                dic[index] = []
                text = listing.text
                type = text.split('·')[2].strip(' ')
                bath = text.split('·')[1].strip(' ')
                beds = text.split('·')[0]
                dic[index].append(xx[index])
                dic[index].append(type)
                dic[index].append(beds[:1])
                dic[index].append(bath[:1])
                index += 1
            except:
                pass
        counter += 20
except:
    pass

dic.pop(index)

# Reset Counter
counter = 0

 # Second while statement to catch non-promo'd ads

try:
    while counter <= 1300:
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        webpage_response = requests.get(url)
        webpage = webpage_response.content

        #  Create second Soup
        soup = BeautifulSoup(webpage, "html.parser")
        listings = soup.find_all('div', class_='Cardstyled__TitleBlockWrapper-nngi4q-4 eMeJos')

        # Loop through each listing and extract the price
        try:
            for listing in listings:
                # Find the price element within the listing
                dic[index] = []
                prop_type = listing.find(attrs={'data-testid': 'property-type'})
                type = prop_type.text.strip()
                if type in 'Studio':
                    dic[index].append(type)
                    dic[index].append(price)
                    dic[index].append(1)
                    dic[index].append(1)

                else:
                    rent_price = listing.find(attrs={'data-testid': 'price'})
                    price = rent_price.text.strip()
                    dic[index].append(price)
                    type = prop_type.text.strip()
                    dic[index].append(type)

                    try:
                        beds = listing.find(attrs={'data-testid': 'beds'})
                        num_beds = beds.text.strip()
                        dic[index].append(num_beds[:1])
                    except:
                        dic[index].append('NaN')

                    try:
                        baths = listing.find(attrs={'data-testid': 'baths'})
                        num_baths = baths.text.strip()
                        dic[index].append(num_baths[:1])
                    except:
                        dic[index].append('NaN')
                index += 1
        except:
            print(listing)
        counter += 20
except:
    pass


df = pd.DataFrame.from_dict(dic)
print('nearly there')
df.to_csv("all_data.csv", index=False)
print('Process Complete :)')
