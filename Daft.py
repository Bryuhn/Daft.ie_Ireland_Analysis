# from requests_html import HTML, HTMLSession
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import pprint as pp
import matplotlib.pyplot as plt

counter = 00
z = []
try:
    while counter <= 1200:
        url = "https://www.daft.ie/property-for-rent/ireland?from="+str(counter)
        print(url)
        webpage_response = requests.get(url)
        webpage = webpage_response.content
        soup = BeautifulSoup(webpage, "html.parser")
        cards = soup.find_all(class_ = "Cardstyled__TitleBlockWrapper-nngi4q-4 eMeJos")
        text = soup.getText()
        cork = text.split("HighPrice High to Low Map")
        y = ' '.join(cork)
        next = y.split("Save")

        next.pop(0)
        for i in range(len(next)):
            m = next[i].split('€')
            try:
                z.append(m[1][:6])
            except:
                pass
        counter += 20
        print(counter,len(z))


except:
    pass

for index, val in enumerate(z):
    if 'pe' in val:
        i = val[:3]
        i = round(((int(i)*52)/12))
        z[index] = 5*round(i/5)
    else:
        z[index] = val

n = []
for i in z:
    try:
        n.append(int(i.replace(',','')))
    except:
        n.append(i)

bin = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 20500]

df = pd.DataFrame(n)
df.to_csv("test.csv", index=False)

plt.hist(n, bins=bin)
plt.show()


