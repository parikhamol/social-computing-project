import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
from collections import OrderedDict


# get the list of all the datetimes from the post.csv
colnames = ['postid' , 'time', 'user','no1','no2','no3','n04' ,'title','post']

posts = pandas.read_csv('post.csv' ,names=colnames)
date_time = posts.time.tolist()

#convert the string to date format of python
time =[]
for i in range(len(date_time)):
    time.append(datetime.datetime.strptime(date_time[i], "%m/%d/%Y %H:%M").date())

#need to get the post1.csv
# get the list of all the datetimes from post1.csv
posts = pandas.read_csv('post1.csv' ,names=colnames)
date_time = posts.time.tolist()


#convert the string to date format of python
for i in range(len(date_time)):
    time.append(datetime.datetime.strptime(date_time[i], "%m/%d/%Y %H:%M").date())


#create a dictionary of unique dates
timeline = {}
for i in range(len(time)):
    if(time[i] in timeline):
        timeline[time[i]] +=1
    else:
        timeline[time[i]] = 1

timeline_sorted = OrderedDict(sorted(timeline.items()))

#write the data to a csv file
writer = csv.writer(open('timeline.csv', 'wb'))
for key, value in timeline_sorted.items():
    sum+=value
    writer.writerow([key, value])

plt.bar(range(len(timeline)), timeline_sorted.values(), align='center')
plt.xticks(range(len(timeline)), timeline_sorted.keys())

plt.show()
