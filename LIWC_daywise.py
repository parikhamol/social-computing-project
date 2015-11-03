import LIWCMeta
import sys
import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import datetime
from collections import OrderedDict
from itertools import izip
import itertools
import pylab as pl

# get all the posts number of words and time of all the posts
colnames = ['day' , 'post','num_words']

posts = pandas.read_csv('combined_post_daywise.csv' ,names=colnames)
post_body = posts.post.tolist()
num = posts.num_words.tolist()
day = posts.day.tolist()

#category is provided in the arguments. Get the normalized liwc values for this category
category1 =[]
index =0
liwc_lexicon = LIWCMeta.extract_liwc_features()
for item in post_body:
    if type(item) == float and np.isnan(item):
        item = ""
    outCountDict = LIWCMeta.getLex(item, liwc_lexicon)
    category1.append((outCountDict[sys.argv[1]])/float(num[index]))
    index = index + 1

#aggregate the liwc values based on the day of the week
mon = []
count_mon =0
tues =[]
count_tues =0
wed =[]
count_wed=0
thur =[]
count_thur =0
fri =[]
count_fri=0
sat =[]
count_sat=0
sun =[]
count_sun=0

for i in range(len(day)):
    if day[i] == 0:
        mon.append(category1[i])
        count_mon = count_mon+1
    elif day[i] == 1:
        tues.append(category1[i])
        count_tues = count_tues+1
    elif day[i] == 2:
        wed.append(category1[i])
        count_wed = count_wed+1
    elif day[i] == 3:
        thur.append(category1[i])
        count_thur = count_thur+1
    elif day[i] == 4:
        fri.append(category1[i])
        count_fri = count_fri+1
    elif day[i] == 5:
        sat.append(category1[i])
        count_sat = count_sat+1
    else:
        sun.append(category1[i])
        count_sun = count_sun+1

#take the day wise average of the LIWC values and plot a graph
days = 7
index = np.arange(days)
m = sum(mon)/count_mon
t = sum(tues)/count_tues
w = sum(wed)/count_wed
th = sum(thur)/count_thur
f = sum(fri)/count_fri
s = sum(sat)/count_sat
su = sum(sun)/count_sun
value = [m, t, w, th, f, s, su]

name = sys.argv[1] + "_daily.pdf"
pp = PdfPages(name)
fig, ax = plt.subplots()
rect = plt.bar(index, value, width = 0.35)
plt.xlabel('Days')
plt.ylabel('LIWC value')
pp.savefig(fig)
plt.show()
pp.close()

#write a csv with the LIWC values for each day
name = sys.argv[1] +"_LIWC_daywise.csv"
with open(name,"w") as f:
    writer = csv.writer(f)
    writer.writerows(itertools.izip_longest(mon,tues,wed, thur, fri, sat, sun, fillvalue=''))
