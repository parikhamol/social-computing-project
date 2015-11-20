import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
from collections import OrderedDict
from itertools import izip
import gensim
from gensim import corpora, models, similarities
import codecs
# get the list of all the datetimes from the post.csv
colnames = ['postid' , 'time', 'user','no1','no2','no3','no4' ,'title','post']

posts = pandas.read_csv('combined_posts.csv' ,names=colnames)
post_id = posts.postid.tolist()
time = posts.time.tolist()
user = posts.user.tolist()
no1 = posts.no1.tolist()
no2 = posts.no2.tolist()
no3 = posts.no4.tolist()
no4 = posts.no3.tolist()
title = posts.title.tolist()
post_body = posts.post.tolist()


documents=[]
texts=[]
for i in range(len(post_body)):
    documents.append(post_body[i])

stoplist = set('for a of the and to in'.split())
for document in documents:
    if type(document)!=str:
        continue
    else:
        texts.append([word for word in document.lower().split() if word not in stoplist])


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100, update_every=1, passes=5)
print "THE POST TOPICS ARE"
print lda.print_topics(20)

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

documents=[]
texts=[]
for i in range(len(comment)):
    if type(comment[i])!=str:
        continue
    else:
        try:
            comment[i].decode('utf-8')
            documents.append(comment[i])
        except UnicodeError:
            continue


stoplist = set('for a of the and to in'.split())
for document in documents:
    if type(document)!=str:
        continue
    else:
        texts.append([word for word in document.lower().split() if word not in stoplist])

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100, update_every=1, passes=5)
print "THE COMMENT TOPICS ARE"
print lda.print_topics(20)

