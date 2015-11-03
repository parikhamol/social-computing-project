import csv
import pandas
import matplotlib.pyplot as plt
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

#convert the string to get just the date
date =[]
for i in range(len(date_time)):
    date.append(datetime.datetime.strptime(date_time[i], "%m/%d/%Y %H:%M").date())

day =[]
for i in range(len(date)):
    day.append(date[i].weekday())


with open("combined_post_daywise.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(izip(day,post_body,num))
