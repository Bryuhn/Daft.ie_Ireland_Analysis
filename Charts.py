import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import datetime
import seaborn as sb
import os
from matplotlib.patheffects import PathPatchEffect, SimpleLineShadow, Normal

counter = 0
os.chdir("C:/Users\Bryuhn\PycharmProjects\Daft")

font_colour = '#000000'
outline_colour = '#ffffff'
colours = ['#00589C', '#016FC4', '#1891C3', "#3AC0DA", '#3DC6C3', '#50E3C2']
cc = {'House':'#00589C', 'Apartment':'#1891C3', 'Studio':'#50E3C2'}

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
k = z.loc[(z['No.Beds'] <= 6) & (z['Price'] >= 100)]

o = z.loc[(z['No.Beds'] <= 6) & (z['Price'] >= 100) &(z['Property Type'] == 'House')]
g = z.loc[(z['No.Beds'] <= 6) & (z['Price'] >= 100) &(z['Property Type'] == 'Apartment')]
s = z.loc[(z['No.Beds'] <= 6) & (z['Price'] >= 100) &(z['Property Type'] == 'Studio')]
onebed = l['Price'].tolist()
twobed = p['Price'].tolist()
threebed = t['Price'].tolist()
fourbeds = w['Price'].tolist()
fivebeds = h['Price'].tolist()

labels = ['Studio','AP1B','AP2B','AP3B','AP4B','H1B','H2B','H3B','H4B','H5B','H6B','H7B']
labels = ['AP1B','AP2B','AP3B','AP4B','AP5B','H1B','H2B','H3B','H4B','H5B','H6B','Studio']
ooo = k.groupby(['Property Type','No.Beds'], as_index=False)['Price'].mean().round()
plt.rcParams.update({'text.color' : font_colour, 'font.weight':'bold'})
ww = {'fontweight':'bold'}
counter = 0
xticks = []
xlabels = []
with plt.style.context('seaborn-v0_8-talk'):
    while counter <= max(ooo['Price']):
        xticks.append(counter)
        xlabels.append('€' + str(counter))
        counter += 500
    plt.rcParams['figure.figsize'] = (8, 15)
    ax = ooo.plot(kind='barh',x='Property Type', y='Price', color=ooo['Property Type'].map(cc), edgecolor=outline_colour,
                         linewidth=1, alpha=1, width=1)
    ax.set_title('Mean Price Per Property Type Categorized by Number of Beds',ww)
    ax.set_yticklabels(labels)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylabel('')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)
    ax.get_legend().remove()
plt.show()

# def RemoveOutliers(nums, outlierConstant):
#     ary = np.array(nums)
#     upper_quartile = np.percentile(ary, 75)
#     lower_quartile = np.percentile(ary, 25)
#     IQR = (upper_quartile - lower_quartile) * outlierConstant
#     quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
#     resultList = []
#     for y in ary.tolist():
#         if quartileSet[0] <= y <= quartileSet[1]:
#             resultList.append(y)
#         else:
#             pass
#     return resultList
#
# onebedn = RemoveOutliers(onebed,1.5)
# twobedn =  RemoveOutliers(twobed,1.5)
# threebedn = RemoveOutliers(threebed,1.5)
# fourbedsn = RemoveOutliers(fourbeds,1.5)
# fivebedsn = RemoveOutliers(fivebeds,1.5)
#
# bed = [onebed, twobed, threebed, fourbeds, fivebeds]
# beds = [onebedn, twobedn, threebedn, fourbedsn, fivebedsn]
#
# for i in range(5):
#     # Labeling X axis
#     xtick = []
#     xlabel = []
#     number = 0
#     print(max(beds[i]))
#     if max(beds[i]) >= 6000:
#         while number <= max(beds[i]):
#             print(number)
#             xtick.append(number)
#             xlabel.append('€' + str(number))
#             number += 1000
#
#         # labeling Y axis
#         ytick = []
#         ylabel = []
#         percent = 0
#         while percent <= 15:
#             ytick.append(percent)
#             ylabel.append(str(percent) + '%')
#             percent += 1
#         positions = [1,-2.2]
#
#     elif max(beds[i]) < 6000:
#         while number <= max(beds[i]):
#             xtick.append(number)
#             xlabel.append('€' + str(number))
#             number += 500
#
#         # labeling Y axis
#         ytick = []
#         ylabel = []
#         percent = 0
#         while percent <= 10:
#             ytick.append(percent)
#             ylabel.append(str(percent) + '%')
#             percent += 1
#         positions = [1,-1.5]
#
#     # Create and style plot
#     plt.rcParams['figure.figsize'] = (15, 9)
#     plt.rcParams.update({'text.color' : font_colour, 'font.weight':'bold'})
#     ww = {'fontweight':'bold'}
#     with plt.style.context('seaborn-v0_8-talk'):
#         plt.grid(visible=True, which='major', axis='both', linewidth=.5)
#         ax = sb.histplot(beds[i],
#                          bins=40,
#                          color=colours[counter],
#                          stat='percent',
#                          kde=True,
#                          edgecolor=outline_colour,
#                          linewidth=1, alpha=1 )
#         ax.set_axisbelow(True)
#         ax.lines[0].set_color(colours[4])
#         ax.lines[0].set_linestyle('dashdot')
#         ax.lines[0].set_label('Kernel Density Estimate')
#         ax.spines['top'].set_visible(False)
#         ax.spines['right'].set_visible(False)
#         plt.axvline(round(np.mean(beds[i])),
#                     label='Average rent across ROI = €' + str(round(np.mean(beds[i]))),
#                     c=colours[2],
#                     linestyle="--")
#         plt.title('Rent Prices For A '+str(i+1)+' Bed Across All Of The Republic of Ireland \n Total number of places = ' +
#                   str(len(beds[i])) + ' \n ' + str(date), ww)
#         plt.xticks(xtick, labels=xlabel)
#         plt.yticks(ytick, ylabel)
#         plt.xlabel('Price of Rent')
#         plt.ylabel('Places Available as a Percent %')
#         kwargs = {'fontstyle': 'italic', 'fontsize': 'x-small'}
#         plt.text(x=positions[0], y=positions[1],
#                  s='*Statistical outliers have been removed: ' + str(len(bed[i]) - len(beds[i])) + ''
#                   '. Prices presented as per month,where price was presented per week the '
#                   'formula (Price*52)/12 was used.',
#                  **kwargs)
#         plt.subplots_adjust(left=0.093, bottom=0.125, right=0.975, top=0.853, wspace=0.19, hspace=0.337)
#         plt.legend()
#         plt.savefig(fname=str(i+1) + ' bed rental property  '  + str(date)+'.png', format='png', dpi=300)
#         plt.cla()
#         counter += 1
#
# print('Process Complete :)')
#
#
# # Colours
# font_colour = '#000000'
# outline_colour = '#ffffff'
# colours = ['#00589C', '#016FC4', '#1891C3', "#3AC0DA", '#3DC6C3', '#50E3C2']
#
#
# # Create date
# date = datetime.datetime.now().strftime("%d-%m-%Y")
#
# # Read SCV
# df = pd.read_csv("Daft_rental_data_" + str(date) +".csv")
# properity_types = ['Apartment','Studio','House']
# ndf = pd.DataFrame()
#
# for i in properity_types:
#     ndf[i] = df.apply(lambda x:x.str.contains(str(i)).sum(), axis=1)
#
# ndf = ndf.drop([0, 2, 3])
#
# rental_numbers = ndf.values.tolist()
# rental_numbers = rental_numbers[0]
# percents = []
# for i in rental_numbers:
#     percents.append(round((i/sum(rental_numbers))*100))
#
# print(sum(percents))
#
#
# # Example data
# pdf = ndf.div(ndf.sum(axis=1),axis=0)*100
# plt.rcParams['figure.figsize'] = (18, 2)
# plt.rcParams.update({'text.color' : font_colour, 'font.weight':'bold'})
# plt.style.context('seaborn-v0_8-talk')
# fig, ax = plt.subplots()
# plt.title("Property Type as a Percent")
#
# z = pdf.plot(kind='barh', stacked=True, color=[colours[0], colours[2], colours[4]], edgecolor=outline_colour,
#          linewidth=1, width=1, ax=ax, label=percents)
#
# fig.patch.set_visible(False)
# plt.legend(bbox_to_anchor=(1.15, 0.5), loc='center right', borderaxespad=3)
#
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
#
# ax.set(xlim=(0, 100))
# ax.set_yticks([])
# for i in ax.containers:
#     print(i)
#     ax.bar_label(i, label_type='center', fmt='%.0f%%',color='#ffffff')
# plt.savefig(fname='Bar_Chart'  + str(date)+'.png', format='png', dpi=300)
# plt.cla()