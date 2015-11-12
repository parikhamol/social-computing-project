import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import scipy.stats


colnames = ['postid' , 'positive', 'negative']
posts = pandas.read_csv("combined_emotions_posts.csv",names=colnames)
comments = pandas.read_csv("combined_emotions_comments_unique.csv", names = colnames)

p_postid  =list(posts.postid)
p_positive = list(posts.positive)
p_negative = list(posts.negative)
c_postid = list(comments.postid)
c_positive = list (comments.positive)
c_negative = list(comments.negative)
post_positive_value = []
post_negative_value = []
comments_positive_value =[]
comments_negative_value = []
count =0
for i in range(0,len(p_postid)):
    for j in range(0,len(c_postid)):
        if(p_postid[i] == c_postid[j]):
            count = count +1
            post_positive_value.append(p_positive[i])
            post_negative_value.append(p_negative[i])
            comments_positive_value.append(c_positive[j])
            comments_negative_value.append(c_negative[j])



print scipy.stats.pearsonr(post_positive_value, comments_positive_value)
print scipy.stats.pearsonr(post_negative_value, comments_negative_value)
