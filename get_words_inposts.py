import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
from collections import OrderedDict
from itertools import izip

# get the list of all the datetimes from the post.csv
colnames = ['postid' , 'time', 'user','no1','no2','no3','no4' ,'title','post']

posts = pandas.read_csv('post.csv' ,names=colnames)
post_id = posts.postid.tolist()
time = posts.time.tolist()
user = posts.user.tolist()
no1 = posts.no1.tolist()
no2 = posts.no2.tolist()
no3 = posts.no4.tolist()
no4 = posts.no3.tolist()
title = posts.title.tolist()
post_body = posts.post.tolist()

number_words=[]

#calculate the number of words in the posts
for i in range(len(post_body)):
    number_words.append(len(str(post_body[i]).split()))


#create a new csv file with number of words as a column
with open("post_with_counts.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(izip(post_id,time,user, no1, no2, no3, no4,title, post_body,number_words))