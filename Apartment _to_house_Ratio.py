import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import pprint as pp

# Get date
date = datetime.datetime.now().strftime("%d-%m-%Y")

# Create counter variable to scape all webpages
counter = 0
index = 0
dic = {}
rent_price_list = []


#  Create Dict for types
rents = {'House': 0, 'Apartment': 0, 'Studio':0}
removal_characters = ('€', ',')

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
                prop_price = price.find(attrs={'data-testid': 'sub-title'})
                money = prop_price.text.strip()
                if 'per month' in money:
                    money = money.split(' ')[0]
                    if ',' in money or '€' in money:
                        for character in removal_characters:
                            money = money.replace(character, '')
                        rent_price_list.append(money)
                elif 'per week' in money:
                    money = (int(money.split(' ')[0])*52)/12
                    rent_price_list.append(money)
            except:
                pass

        # Loop through returns and sort into Apartment or House
        for listing in listings:
            try:
                dic[index] = []
                text = listing.text
                type = text.split('·')[2].strip(' ')
                bath = text.split('·')[1].strip(' ')
                beds = text.split('·')[0]
                dic[index].append(rent_price_list[index])
                dic[index].append(type)
                dic[index].append(beds[:1])
                dic[index].append(bath[:1])
                # dic[index].append(addresses[index])
                index += 1

            except:
                pass
        counter += 20
except:
    pass

# Remove final index which is empty
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

                if 'Studio' in type:
                    # Get Price
                    rent_price = listing.find(attrs={'data-testid': 'price'})
                    price = rent_price.text.strip()
                    #  Check if rent is per month or per week
                    if 'per month' in price:
                        price = price.split(' ')[0]
                        if ',' in price or '€' in price:
                            for character in removal_characters:
                                price = price.replace(character, '')
                            dic[index].append(price)
                    elif 'per week' in price:
                        price = price.split(' ')[0]
                        if ',' in price or '€' in price:
                            for character in removal_characters:
                                price = price.replace(character, '')
                            price = round((int(price.split(' ')[0]) * 52) / 12)
                        dic[index].append(price)
                    dic[index].append('Studio')
                    dic[index].append(1)
                    dic[index].append(1)

                # If not studio
                elif 'Studio' not in type:
                    try:
                        #  Get Price
                        rent_price = listing.find(attrs={'data-testid': 'price'})
                        price = rent_price.text.strip()
                        #  Check if rent is per month or per week
                        if 'per month' in price:
                            price = price.split(' ')[0]
                            # Convert to int
                            if ',' in price or '€' in price:
                                for character in removal_characters:
                                    price = price.replace(character, '')
                                dic[index].append(price)
                        elif 'per week' in price:
                            price = price.split(' ')[0]
                            # Convert to int
                            if ',' in price or '€' in price:
                                for character in removal_characters:
                                    price = price.replace(character, '')
                                price = round((int(price.split(' ')[0]) * 52) / 12)
                            dic[index].append(price)
                        dic[index].append(type)
                    except:
                        pass

                    # Add number of bedrooms
                    try:
                        beds = listing.find(attrs={'data-testid': 'beds'})
                        num_beds = beds.text.strip()
                        dic[index].append(num_beds[:1])
                    except:
                        dic[index].append('NaN')

                    # Add number of bathrooms
                    try:
                        baths = listing.find(attrs={'data-testid': 'baths'})
                        num_baths = baths.text.strip()
                        dic[index].append(num_baths[:1])
                    except:
                        dic[index].append(0)
                index += 1
        except:
            pass
        counter += 20
except:
    pass

#  Remove missing data
for k,v in dic.items():
    if len(v) != 3:
        print(v)
        dic[k].pop()

print('nearly there')
df = pd.DataFrame.from_dict(dic)
df.to_csv("Daft_rental_data_"+str(date)+'.csv', index=False)
print('Process Complete :)')
