import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import datetime
import seaborn as sb
import os

os.chdir("C:/Users\Bryuhn\PycharmProjects\Daft")

font_colour = '#000000'
outline_colour = '#ffffff'
colours = ['#00589C', '#016FC4', '#1891C3', "#3AC0DA", '#3DC6C3', '#50E3C2']


# Create date for plot
date = datetime.datetime.now().strftime("%d-%m-%Y")

df = pd.read_csv("Daft_rental_data_"+str(date)+'.csv', header=0)
df = df.dropna()
k = df.transpose()
z = k.set_axis(['Price', 'Property Type', 'No.Beds', 'No.Baths'], axis=1)
z = z.astype({"Price": 'float64', "Property Type": 'str', 'No.Beds':'int', 'No.Baths':'int' })

l = z.loc[(z['No.Beds'] == 1) & (z['Price'] >= 100)]
p = z.loc[(z['No.Beds'] == 2) & (z['Price'] >= 100)]
t = z.loc[(z['No.Beds'] == 3) & (z['Price'] >= 100)]
w = z.loc[(z['No.Beds'] == 4) & (z['Price'] >= 100)]
h = z.loc[(z['No.Beds'] == 5) & (z['Price'] >= 100)]

onebed = l['Price'].tolist()
twobed = p['Price'].tolist()
threebed = t['Price'].tolist()
fourbeds = w['Price'].tolist()
fivebeds = h['Price'].tolist()


def RemoveOutliers(nums, outlierConstant):
    ary = np.array(nums)
    upper_quartile = np.percentile(ary, 75)
    lower_quartile = np.percentile(ary, 25)
    IQR = (upper_quartile - lower_quartile) * outlierConstant
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    resultList = []
    for y in ary.tolist():
        if quartileSet[0] <= y <= quartileSet[1]:
            resultList.append(y)
        else:
            pass
    return resultList

onebedn = RemoveOutliers(onebed,1.5)
twobedn =  RemoveOutliers(twobed,1.5)
threebedn = RemoveOutliers(threebed,1.5)
fourbedsn = RemoveOutliers(fourbeds,1.5)
fivebedsn = RemoveOutliers(fivebeds,1.5)

bed = [onebed, twobed, threebed, fourbeds, fivebeds]
beds = [onebedn, twobedn, threebedn, fourbedsn, fivebedsn]

for i in range(5):
    # Labeling X axis
    xtick = []
    xlabel = []
    number = 0
    if max(beds[i]) > 6000:
        while number <= max(beds[i]):
            xtick.append(number)
            xlabel.append('€' + str(number))
            number += 1000

        # labeling Y axis
        ytick = []
        ylabel = []
        percent = 0
        while percent <= 15:
            ytick.append(percent)
            ylabel.append(str(percent) + '%')
            percent += 1
        positions = [1,-2.2]


    if max(beds[i]) < 6000:
        while number <= max(beds[i]):
            xtick.append(number)
            xlabel.append('€' + str(number))
            number += 500

        # labeling Y axis
        ytick = []
        ylabel = []
        percent = 0
        while percent <= 10:
            ytick.append(percent)
            ylabel.append(str(percent) + '%')
            percent += 1
        positions = [1,-1.5]

    # Create and style plot
    plt.rcParams['figure.figsize'] = (15, 9)
    plt.rcParams.update({'text.color' : font_colour, 'font.weight':'bold'})
    ww = {'fontweight':'bold'}
    with plt.style.context('seaborn-v0_8-talk'):
        plt.grid(visible=True, which='major', axis='both', linewidth=.5)
        ax = sb.histplot(beds[i],
                         bins=40,
                         color=colours[0],
                         stat='percent',
                         kde=True,
                         edgecolor=outline_colour,
                         linewidth=1, )
        ax.set_axisbelow(True)
        ax.lines[0].set_color(colours[4])
        ax.lines[0].set_linestyle('dashdot')
        ax.lines[0].set_label('Kernel Density Estimate')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.axvline(round(np.mean(beds[i])),
                    label='Average rent across ROI = €' + str(round(np.mean(beds[i]))),
                    c=colours[2],
                    linestyle="--")
        plt.title('Rent Prices For A '+str(i+1)+' Bed Across All Of The Republic of Ireland \n Total number of places = ' +
                  str(len(beds[i])) + ' \n ' + str(date), ww)
        plt.xticks(xtick, labels=xlabel)
        plt.yticks(ytick, ylabel)
        plt.xlabel('Price of Rent')
        plt.ylabel('Places Available as a Percent %')
        kwargs = {'fontstyle': 'italic', 'fontsize': 'x-small'}
        plt.text(x=positions[0], y=positions[1],
                 s='*Statistical outliers have been removed: ' + str(len(bed[i]) - len(beds[i])) + ''
                  '. Prices presented as per month,where price was presented per week the '
                  'formula (Price*52)/12 was used.',
                 **kwargs)
        plt.subplots_adjust(left=0.093, bottom=0.125, right=0.975, top=0.853, wspace=0.19, hspace=0.337)
        plt.legend()
        plt.savefig(fname=str(i) + str(date)+'.png', format='png', dpi=600)
        plt.cla()

print('Process Complete :)')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import datetime
import seaborn as sb

# Colours
font_colour = '#000000'
outline_colour = '#ffffff'
colours = ['#00589C', '#016FC4', '#1891C3', "#3AC0DA", '#3DC6C3', '#50E3C2']


# Create date
date = datetime.datetime.now().strftime("%d-%m-%Y")
print(date)
# Read SCV
df = pd.read_csv("Daft_rental_data_" + str(date) +".csv")

print(df)