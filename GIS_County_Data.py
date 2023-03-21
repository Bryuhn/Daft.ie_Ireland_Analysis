import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pprint as pp


date = datetime.datetime.now().strftime("%d-%m-%Y")

count = 0

counties = {'Carlow': 0, 'Cavan': 0, 'Clare': 0, 'Cork': 0, 'Donegal': 0, 'Dublin': 0, 'Galway': 0, 'Kerry': 0,
            'Kildare': 0, 'Kilkenny': 0, 'Laois': 0, 'Leitrim': 0, 'Limerick': 0, 'Longford': 0, 'Louth': 0, 'Mayo': 0,
            'Meath': 0, 'Monaghan': 0, 'Offaly': 0, 'Roscommon': 0, 'Sligo': 0, 'Tipperary': 0, 'Waterford': 0,
            'Westmeath': 0, 'Wexford': 0, 'Wicklow': 0}



# Create counter variable to scape all webpages
counter = 0

# List for prices to be added too
rent_price_list = []
dublin = []

try:
    while counter <= 1500:
        # Access Daft.ie via Url for all of Ireland and save response for reach webpage
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        webpage_response = requests.get(url)
        webpage = webpage_response.content

        # Parse each response to get all text
        soup = BeautifulSoup(webpage, "html.parser")
        cards = soup.find_all(class_ = "TitleBlock__Address-sc-1avkvav-8 hCMmam")
        text = soup.getText()

        # Wrangle the text to usable state to extract the numerical price
        listings = text.split("HighPrice High to Low Map")
        Listings_joined = ' '.join(listings)
        next = Listings_joined.split("Save")
        next.pop(0)
        for i in next:
            if 'Co. Carlow' in i:
                count += 1
            elif 'Co. Dublin' in i:
                dublin.append(i)
            else:
                pass
            for county in counties:
                if county in i:
                    counties[county] +=1
                else:
                    pass

        counter += 20
except:
    pass

sum = 0
nums = []
names = []
for i in counties.keys():
    names.append(i.upper())

for i in counties.values():
    sum += i
    nums.append(i)

counties = {k.upper():v for k,v in counties.items()}


df = pd.DataFrame.from_dict(counties,orient='index')

df.to_csv('Daft_GIS_Counties_Data_'+str(date)+'.csv',index=True)
print('Process Finish')
