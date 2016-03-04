import pandas
import csv
from itertools import izip

colnames = ['postid' , 'datetime', 'userid', 'no1' , 'no2','no3','no4','title','content']

posts = pandas.read_csv ("../../CSVpost/combined_posts.csv", names=colnames)

post_id = posts.postid.tolist()
users =  posts.userid.tolist()

print len(users)


unique_users ={}

count =0

for i in range(len(users)):
    if users[i] in unique_users.values():
        continue
    else:
        unique_users[count] = users[i]
        count=count+1



with open("unique_user.csv" ,"w") as f:
    writer = csv.writer(f)
    for key in unique_users:
        print key, unique_users[key]
        writer.writerow([key, unique_users[key]])

execfile("ssh aparikh42@datavoyager.cc.gatech.edu nohup /usr/bin/python hello.py &")
