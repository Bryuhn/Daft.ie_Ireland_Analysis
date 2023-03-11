import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import datetime
import seaborn as sb


# Import data
df = pd.read_csv('test.csv', sep=' ', header=None)

# Convert df to list
list_of_rent_prices = df.values.tolist()

# Extract list from nested list
rent_price_list_ordered = []
for i in list_of_rent_prices:
    for price in i:
        rent_price_list_ordered.append(price)

# Sort list
rent_price_list_ordered.sort()
rent_price_list_ordered.pop(0)

# Remove ',' and convert to int from str
rent_price_master = []
for i in rent_price_list_ordered:
    if ',' in i:
        pass
    else:
        rent_price_master.append(int(i))

# Remove Outliers Function
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
    return resultList

# Remove Outliers

rent_price = RemoveOutliers(rent_price_master, 1.5)

# Calculate mean and Standard deviation.
mean = np.mean(rent_price)
sd = np.std(rent_price)

# Create comparible sample
sample = normal(loc=2280, scale=990, size=len(rent_price))
sample = abs(sample)
sample_mean = np.mean(sample)
samples_sd = np.std(sample)
sample.sort()

# Find distance
dist = norm(sample_mean, samples_sd)

# Create Probablity Curve
values = [value for value in range(int(min(sample)), int(max(sample)))]
probabilities = [dist.pdf(value) for value in values]

# Colours for plot styling
colours = ['#00589C', '#016FC4', '#1891C3', "#3AC0DA", '#3DC6C3', '#50E3C2']

# Create date for plot
date = datetime.datetime.now().strftime("%d-%m-%Y")

# Labeling X axis
xtick = []
xlabel = []
number = 0
while number <=5500:
    xtick.append(number)
    xlabel.append('€'+str(number))
    number += 500

# labeling Y axis
ytick = []
ylabel = []
percent = 0
while percent <= 6:
    ytick.append(percent)
    ylabel.append(str(percent)+'%')
    percent +=1

plt.rcParams['figure.figsize'] = (12, 9)

# Create plot
with plt.style.context('fivethirtyeight'):
    ax = sb.histplot(rent_price,
                bins=50,
                color=colours[0],
                stat='percent',
                kde=True,
                edgecolor=colours[1],
                linewidth=1,)
    ax.lines[0].set_color(colours[4])
    ax.lines[0].set_linestyle('dashdot')
    ax.lines[0].set_label('Kernal Density Estimate')
    plt.axvline(round(mean),
                label='Average rent across ROI = €' + str(round(mean)),
                c=colours[2],
                linestyle="--")
    plt.axvline(1100, label='My previous rent price in ROI = €' + str(1100),
                c=colours[3],
                linestyle="--")
    plt.title('Rent Prices Across All Of The Republic of Ireland \n Total number of places = ' +
              str(len(rent_price_master)) + ' \n ' + str(date))
    plt.xticks(xtick,labels=xlabel)
    plt.yticks(ytick,ylabel)
    plt.xlabel('Price of Rent')
    plt.ylabel('Places Available as a Percent %')
    kwargs = {'fontstyle':'italic','fontsize':'x-small'}
    plt.text(x=1, y=-1,
             s='*Statisical outliers have been removed, prices presented as per month,where price was presented per week the '
               'formula (Price*52)/12 was used. \n Places where more than one place was availible for rent only 1 place '
               'was considered.',
             **kwargs)
    plt.subplots_adjust(left=0.053, bottom=0.125, right=0.975, top=0.853, wspace=0.19, hspace=0.337)
    plt.legend()
    plt.savefig(fname='Rent Price Histogram.png',format='png',dpi=600)
plt.show()
plt.close()
print('Process Complete :)')
