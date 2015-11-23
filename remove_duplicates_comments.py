import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
from collections import OrderedDict
import itertools
from itertools import izip
import operator

# get the list of all the datetimes from the post.csv
colnames = ['postid' , 'commentid' ,'time', 'user','no1','no2','no3' ,'comment']

posts = pandas.read_csv('merged.csv' ,names=colnames)
post_id = posts.postid.tolist()
comment_id = posts.commentid.tolist()
time = posts.time.tolist()
user = posts.user.tolist()
no1 = posts.no1.tolist()
no2 = posts.no2.tolist()
no3 = posts.no3.tolist()
comment = posts.comment.tolist()


#intitalize lists for all unique posts
d ={}
new_post_id =[]
new_commentid=[]
new_time = []
new_user=[]
new_no1=[]
new_no2=[]
new_no3=[]
new_comment=[]
counter = 0
#populate the lists witl all the unique posts
for i in range(0,len(post_id)):
    if comment_id[i] in d.keys():
        counter+=1
        continue
    else:
        d[comment_id[i]] = i
        new_post_id.append(post_id[i])
        new_time.append(time[i])
        new_user.append(user[i])
        new_no1.append(no1[i])
        new_no2.append(no2[i])
        new_no3.append(no3[i])
        new_commentid.append(comment_id[i])
        new_comment.append(comment[i])

with open("combined_comments.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(izip(new_post_id,new_commentid,new_time,new_user, new_no1, new_no2, new_no3, new_comment))
