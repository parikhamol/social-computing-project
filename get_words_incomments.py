import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
from collections import OrderedDict
from itertools import izip

# get the list of all the datetimes from the post.csv
colnames = ['postid' , 'commentid','time', 'user','no1','no2','no3','comment']

posts = pandas.read_csv('combined_comments.csv' ,names=colnames)
post_id = posts.postid.tolist()
commentid = posts.commentid.tolist()
time = posts.time.tolist()
user = posts.user.tolist()
no1 = posts.no1.tolist()
no2 = posts.no2.tolist()
no3 = posts.no3.tolist()
comment = posts.comment.tolist()

number_words=[]

#calculate the number of words in the comments
for i in range(len(comment)):
    number_words.append(len(str(comment[i]).split()))

#create a new csv file with the number of words as a column
with open("combined_comments_with_counts.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(izip(post_id,commentid,time,user, no1, no2, no3,comment,number_words))