import csv
import pandas
from matplotlib.backends.backend_pdf import PdfPages
import datetime
from collections import OrderedDict
from itertools import izip

# get all the posts number of words and time of all the posts
colnames = ['postid' , 'time', 'user','no1','no2','no3','n04' ,'title','post','num_words']

posts = pandas.read_csv('combined_post_with_counts.csv' ,names=colnames)
post_body = posts.post.tolist()
num = posts.num_words.tolist()
date_time = posts.time.tolist()

a= datetime.datetime.strptime(date_time[1],"%m/%d/%Y %H:%M").time()

#convert the string to get just the date
time =[]
for i in range(len(date_time)):
    time.append(datetime.datetime.strptime(date_time[i], "%m/%d/%Y %H:%M").time())

hour =[]
for i in range(len(time)):
    hour.append(time[i].hour)


with open("combined_post_hourly.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(izip(hour,post_body,num))
