import LIWCMeta
import sys
import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import datetime
from collections import OrderedDict
from itertools import izip
import itertools
import pylab as pl

# get all the posts number of words and time of all the posts
colnames = ['hour' , 'post','num_words']

posts = pandas.read_csv('combined_post_hourly.csv' ,names=colnames)
post_body = posts.post.tolist()
num = posts.num_words.tolist()
hour = posts.hour.tolist()

#category is provided in the arguments. Get the normalized liwc values for this category
category1 =[]
index =0
liwc_lexicon = LIWCMeta.extract_liwc_features()
for item in post_body:
    if type(item) == float and np.isnan(item):
        item = ""
    outCountDict = LIWCMeta.getLex(item, liwc_lexicon)
    category1.append((outCountDict[sys.argv[1]])/float(num[index]))
    index = index + 1

#aggregate the liwc values based on the day of the week
one = []
count_one =0
two =[]
count_two =0
three =[]
count_three=0
four =[]
count_four =0
five =[]
count_five=0
six =[]
count_six=0
seven =[]
count_seven=0
eight =[]
count_eight=0
nine =[]
count_nine=0
ten =[]
count_ten=0
eleven =[]
count_eleven=0
twelve =[]
count_twelve=0
thirteen =[]
count_thirteen=0
fourt =[]
count_fourt=0
fift =[]
count_fift=0
sixt =[]
count_sixt=0
sevent =[]
count_sevent=0
eighteen =[]
count_eighteen=0
ninet =[]
count_ninet=0
twe =[]
count_twe=0
twe1 =[]
count_twe1=0
twe2 =[]
count_twe2=0
twe3 =[]
count_twe3=0
twe4 =[]
count_twe4=0

for i in range(len(hour)):
    if hour[i] == 1:
        one.append(category1[i])
        count_one = count_one+1
    elif hour[i] == 2:
        two.append(category1[i])
        count_two = count_two+1
    elif hour[i] == 3:
        three.append(category1[i])
        count_three = count_three+1
    elif hour[i] == 4:
        four.append(category1[i])
        count_four = count_four+1
    elif hour[i] == 5:
        five.append(category1[i])
        count_five = count_five+1
    elif hour[i] == 6:
        six.append(category1[i])
        count_six = count_six+1
    elif hour[i] == 7:
        seven.append(category1[i])
        count_seven= count_seven+1
    elif hour[i] == 8:
        eight.append(category1[i])
        count_eight = count_eight+1
    elif hour[i] == 9:
        nine.append(category1[i])
        count_nine = count_nine+1
    elif hour[i] == 10:
        ten.append(category1[i])
        count_ten = count_ten+1
    elif hour[i] == 11:
        eleven.append(category1[i])
        count_eleven = count_eleven+1
    elif hour[i] == 12:
        twelve.append(category1[i])
        count_twelve = count_twelve+1
    elif hour[i] == 13:
        thirteen.append(category1[i])
        count_thirteen = count_thirteen+1
    elif hour[i] == 14:
        fourt.append(category1[i])
        count_fourt = count_fourt+1
    elif hour[i] == 15:
        fift.append(category1[i])
        count_fift = count_fift+1
    elif hour[i] == 16:
        sixt.append(category1[i])
        count_sixt = count_sixt+1
    elif hour[i] == 17:
        sevent.append(category1[i])
        count_sevent = count_sevent+1
    elif hour[i] == 18:
        eighteen.append(category1[i])
        count_eighteen = count_eighteen+1
    elif hour[i] == 19:
        ninet.append(category1[i])
        count_ninet = count_ninet+1
    elif hour[i] == 20:
        twe.append(category1[i])
        count_twe = count_twe+1
    elif hour[i] == 21:
        twe1.append(category1[i])
        count_twe1 = count_twe1+1
    elif hour[i] == 22:
        twe2.append(category1[i])
        count_twe2 = count_twe2+1
    elif hour[i] == 23:
        twe3.append(category1[i])
        count_twe3 = count_twe3+1
    elif hour[i] == 0:
        twe4.append(category1[i])
        count_twe4 = count_twe4+1

#take the day wise average of the LIWC values and plot a graph
hours = 24
index = np.arange(hours)
if count_one > 0:
    one_avg = sum(one)/count_one
else:
    count_one = 0
if count_two > 0:
    two_avg = sum(two)/count_two
else:
    two_avg= 0
if count_three >0:
    three_avg = sum(three)/count_three
else:
    three_avg =0
if count_four > 0:
    four_avg = sum(four)/count_four
else:
    four_avg=0
if count_five >0:
    five_avg = sum(five)/count_five
else:
    five_avg =0;
if count_six > 0:
    six_avg = sum(six)/count_six
else:
    six_avg = 0
if count_seven > 0:
    seven_avg = sum(seven)/count_seven
else:
    print "7"
    seven_avg = 0
if count_eight > 0:
    eight_avg = sum(eight)/count_eight
else:
    print "8"
    eight_avg = 0
if count_nine > 0:
    nine_avg = sum(nine)/count_nine
else:
    print "9"
    nine_avg = 0
if count_ten > 0:
    ten_avg = sum(ten)/count_ten
else:
    print "10"
    ten_avg = 0
if count_eleven > 0:
    eleven_avg = sum(eleven)/count_eleven
else:
    print "11"
    eleven_avg = 0
if count_twelve > 0:
    twelve_avg = sum(twelve)/count_twelve
else:
    print "12"
    twelve_avg = 0
if count_thirteen > 0:
    thirteen_avg = sum(thirteen)/count_thirteen
else:
    print "13"
    thirteen_avg = 0
if count_fourt > 0:
    fourt_avg = sum(fourt)/count_fourt
else:
    print "14"
    fourt_avg = 0
if count_fift > 0:
    fift_avg = sum(fift)/count_fift
else:
    print "15"
    fift_avg = 0
if count_sixt > 0:
    sixt_avg = sum(sixt)/count_sixt
else:
    print "16"
    sixt_avg = 0
if count_sevent > 0:
    sevent_avg = sum(sevent)/count_sevent
else:
    print "17"
    sevent_avg = 0
if count_eighteen > 0:
    eighteen_avg = sum(eighteen)/count_eighteen
else:
    print "18"
    eighteen_avg = 0
if count_ninet > 0:
    ninet_avg = sum(ninet)/count_ninet
else:
    print "19"
    ninet_avg = 0
if count_twe > 0:
    twe_avg = sum(twe)/count_twe
else:
    print "20"
    twe_avg = 0
if count_twe1 > 0:
    twe1_avg = sum(twe1)/count_twe1
else:
    print "21"
    twe1_avg = 0
if count_twe2 > 0:
    twe2_avg = sum(twe2)/count_twe2
else:
    print "22"
    twe2_avg = 0
if count_twe3 > 0:
    twe3_avg = sum(twe3)/count_twe3
else:
    print "23"
    twe3_avg = 0
if count_twe4 > 0:
    twe4_avg = sum(twe4)/count_twe4
else:
    print "24"
    twe4_avg = 0

value = [twe4_avg,one_avg,two_avg, three_avg, four_avg, five_avg, six_avg, seven_avg, eight_avg, nine_avg, ten_avg, eleven_avg, twelve_avg, thirteen_avg, fourt_avg, fift_avg, sixt_avg, sevent_avg, eighteen_avg, ninet_avg, twe_avg, twe1_avg, twe2_avg, twe3_avg]

name = sys.argv[1] + "_hourly.pdf"
pp = PdfPages(name)
fig, ax = plt.subplots()
rect = plt.bar(index, value, width = 0.35)
plt.xlabel('Hour')
plt.ylabel('LIWC value')
pp.savefig(fig)
plt.show()
pp.close()

#write a csv with the LIWC values for each day
name = sys.argv[1] +"LIWC_hourly.csv"
with open(name,"w") as f:
    writer = csv.writer(f)
    writer.writerows(itertools.izip_longest(twe4,one,two, three, four, five, six, seven, eight, nine, ten, eleven , twelve, thirteen, fourt, fift, sixt, sevent,eighteen, ninet, twe, twe1, twe2, twe3, fillvalue=''))
