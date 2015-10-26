import csv
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



colnames = ['postid' , 'positive', 'negative']
posts = pandas.read_csv("emotions_posts.csv",names=colnames)
comments = pandas.read_csv("emotions_comments_unique.csv", names = colnames)

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
for i in range(len(p_postid)):
    for j in range(len(c_postid)):
        if(p_postid[i] == c_postid[j]):
            post_positive_value.append(p_positive[i])
            post_negative_value.append(p_negative[i])
            comments_positive_value.append(c_positive[j])
            comments_negative_value.append(c_negative[j])
            break

#creating a bar graph to compare the positive for each comment
y = range(len(c_postid))
fig, axes = plt.subplots(ncols=2, sharey=True)
axes[0].barh(y, post_positive_value, align='center', color='b',edgecolor='none')
axes[0].set_xlabel('POSTS')
axes[1].barh(y, comments_positive_value, align='center', color='r',edgecolor='none')
axes[1].set_xlabel('COMMENTS')
axes[0].invert_xaxis()
plt.suptitle('Positive Affect', fontsize=15)
plt.show()
pp = PdfPages('Postive and Negative Affect.pdf')
pp.savefig(fig)


#creating a bar graph to compare the negative for each comment
y = range(len(c_postid))
fig, axes = plt.subplots(ncols=2, sharey=True)
axes[0].barh(y, post_negative_value, align='center', color='b',edgecolor='none')
axes[0].set_xlabel('POSTS')
axes[1].barh(y, comments_negative_value, align='center', color='r',edgecolor='none')
axes[1].set_xlabel('COMMENTS')
axes[0].invert_xaxis()
plt.suptitle('Negative Affect', fontsize=15)
plt.show()
pp.savefig(fig)

fig = plt.figure()
ax = fig.add_subplot(1,1,1) 
ax.scatter(post_positive_value,comments_positive_value)
ax.set_title("Positive LIWC values")
plt.show()
pp.savefig(fig)

fig = plt.figure()
ax = fig.add_subplot(1,1,1) 
ax.scatter(post_negative_value,comments_negative_value)
ax.set_title("Negative LIWC values")
plt.show()
pp.savefig(fig)
pp.close()


