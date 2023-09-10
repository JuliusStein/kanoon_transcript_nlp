import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from matplotlib.pyplot import figure

caseFrame = pd.read_json('../data_cleaning/formattedData_noText.json')

fig = plt.gcf()
fig.set_size_inches(24, 13.6)
frame1 = fig.gca()
frame1.axes.get_yaxis().set_visible(False)
frame1.set_facecolor((0, 0, 0))
fig.patch.set_facecolor('xkcd:black')
frame1.spines['bottom'].set_color('white')
frame1.xaxis.label.set_color('white')
frame1.tick_params(axis='x', colors='white')


for index, row in caseFrame.iterrows():
    date = row['date']
    year, month, day = map(int,date.split("-"))
    if(year>1970):
        if(row['resultCode'] != "U"):
            try:
                plt.axvline(dt.datetime(year, month, day), color="white",linewidth=0.5)
            except:
                print("Y:",year,"M:",month,"D:",day,"failed")

annot_x = (plt.xlim()[1] + plt.xlim()[0])/2
annot_y = (plt.ylim()[1] + plt.ylim()[0])/2


txt = frame1.text(annot_x, annot_y, "Chart Ready", 
              ha='center', fontsize=36, color='#DD4012')

def hover(event):
    txt.set_text("")

fig = plt.gcf()
fig.canvas.mpl_connect('motion_notify_event', hover)
plt.show()