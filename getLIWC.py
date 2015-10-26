import LIWCMeta
import sys
import matplotlib.pyplot as plt
import csv
import pandas
from itertools import izip
import math
import numpy as np


# Dictionary output of LIWC measures per post: ['present_tense', 'first_person_plural', 'family', 'feel', 'money', 'causation', 'insight', 'humans', 'relative', 'see', 'adverbs', 'anger', 'home', 'sexual', 'future_tense', 'death', 'third_person', 'negation', 'discrepancies', 'religion', 'percept', 'verbs', 'health', 'past_tense', 'body', 'bio', 'tentativeness', 'first_person_singular', 'inhibition', 'hear', 'cognitive_mech', 'second_person', 'friends', 'achievement', 'negative_affect', 'auxiliary_verbs', 'anxiety', 'certainty', 'work', 'sadness', 'swear', 'positive_affect', 'social']


def main(in_filename):
    doc = []
    str = "post";
    
    #this is done because of the different formats of the post and comment files
    if sys.argv[1].find(str) >=0:
        colnames = ['postid' , 'time', 'user','no1','no2','no3','no4' ,'title','post', 'now']
        posts = pandas.read_csv(sys.argv[1] ,names=colnames)
        num = posts.now.tolist()
        doc = posts.post.tolist()
    else:
        colnames = ['postid' , 'commentid','time', 'user','no1','no2','no3','comment','now']
        comments = pandas.read_csv(sys.argv[1],names=colnames)
        num = comments.now.tolist()
        doc = comments.comment.tolist()

    index =0
    all_postive_liwc_measures = []
    all_negative_liwc_measures = []
    print "Getting LIWC measures for " , sys.argv[1]
    liwc_lexicon = LIWCMeta.extract_liwc_features()
    for item in doc:
        if type(item) == float and np.isnan(item):
            item = ""
        outCountDict = LIWCMeta.getLex(item, liwc_lexicon)
        #creating an array of all positive category values for each post and adding them
        #creating an array of all negative category values for each post and adding them
        a=outCountDict['positive_affect']
        print item , a , "and ", num[index] ,"and " , a/float(num[index])
        all_postive_liwc_measures.append((outCountDict['positive_affect']  )/float(num[index]))
        all_negative_liwc_measures.append((outCountDict['negative_affect'])/float(num[index]))
        index = index + 1


    # This is for all the reddit posts to get postid , positive and negative comments for each post
    if in_filename.find(str) >=0:
        colnames = ['postid' , 'Time' , 'Author','Nocomments', 'upvotes' , 'downvotes' , 'updown' ,'title', 'commenttext']
        data = pandas.read_csv('post.csv' ,names=colnames)
        postid = list(data.postid)
        with open("emotions_posts.csv","w") as f:
            writer = csv.writer(f)
            writer.writerows(izip(postid,all_postive_liwc_measures,all_negative_liwc_measures))

    # This is for all the reddit comments to get postid for each comment, positive and negative score for each comment
    else:
        colnames = ['postid' , ' commentid' , 'Time' , 'Author', 'upvotes' , 'downvotes' , 'updown' , 'commenttext']
        data = pandas.read_csv('comments.csv' ,names=colnames)
        postid = list(data.postid)
        with open("emotions_comments.csv","w") as f:
            writer = csv.writer(f)
            writer.writerows(izip(postid,all_postive_liwc_measures,all_negative_liwc_measures))

        # Get the csv into lists get aggregate LIWC values for comments for each post
        colnames = ['postid' , 'positive' ,'negative']
        data = pandas.read_csv("emotions_comments.csv", names=colnames)
        postid= list(data.postid)
        positive = list(data.positive)
        negative = list(data.negative)
        unique_postid = []
        positive_unique_postid = []
        negative_unique_postid = []
        p1 =0
        sum_positive = 0
        sum_negative = 0
        while(p1<len(postid)):
            for p2 in range(p1,len(postid)):
                if postid[p1] == postid[p2]:
                    continue
                else:
                    unique_postid.append(postid[p1])
                    for i in range(p1,p2):
                        sum_positive += positive[i]
                        sum_negative += negative[i]
                    sum_positive = float(sum_positive) / (p2-p1+1)
                    sum_negative = float(sum_negative) / (p2-p1+1)
                    positive_unique_postid.append(sum_positive)
                    negative_unique_postid.append(sum_negative)
                    sum_positive = 0
                    sum_negative = 0
                    p1 = p2 -1 
                    break
            if p2 == len(postid) -1:
                for i in range(p1,p2+1):
                    sum_positive += positive[i]
                    sum_negative += negative[i]
                positive_unique_postid.append(sum_positive)
                negative_unique_postid.append(sum_negative)                
                unique_postid.append(postid[p1])
                break
            p1 = p1 + 1

        #write the average positive and negative LIWC values for all comments of a post into a CSV file
        with open("emotions_comments_unique.csv","w") as f:
            writer = csv.writer(f)
            writer.writerows(izip(unique_postid,positive_unique_postid,negative_unique_postid))

if __name__ == "__main__":
    main(sys.argv[1])
