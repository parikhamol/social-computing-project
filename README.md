# social-computing-project
This is the code for the social computing project at Gatech
1.	Need to write a code that combines all the posts file in one file and remove duplicates
	⁃	this can be then used as the primary post.csv for all subsequent code
	-	also create a combined post file with the word counts for code that uses number of words
	
2.	Need to write a code that combines all the comments files in one file and remove duplicates
	⁃	this can be then used as the primary comments.csv for all subsequent code
	-	Also create a combined comment file with the word counts for code that uses number of words
	
3.	Right now the steps from 4 to 8 need to be run separately for each posts and comments file that we have

4.	Run get_words_inposts.py 
	⁃	change the posts.csv in the code to run on different posts (in future use the combined posts.csv file)
	⁃	This generates a post_with_count.csv file with all the counts
	
5.	Run get_words_incomments.py
	⁃	change the comments.csv in the code to run on different set of comments (in future will use the combined comments.csv file)
	⁃	This generates a comments_with_count.csv with all the counts
	
6.	Run getLIWC.py post_with_count.csv
	⁃	this generates emotions_post.csv
	⁃	This contains a list of 2 emotions from liwc for that post file
	⁃	emotions categories can be changed in the code
	
7.	Run getLIWC.py comments_with_count.csv
	⁃	This generates emotions_comments_unique.csv
	⁃	This contains a list 2 same emotions as above for that comment file
	⁃	emotion categories can be changed as above
	
8.	Run plots.py 
	⁃	This generates graphs and scatter plots for the emotions we choose above
	
9.	Run timeline_posts.py 
	⁃	This read post.csv and post1.csv (In the future will use the combined post.csv file)
	⁃	Generates a timeline of posts on a daily bases
10.	Run post_daywise.py 
	-	This reads post_with_count.csv and (In future will use combined post file having number of words)
	-	creates post_daywise.csv
11.	Run LIWC_daywise.py <LIWC category>
	-	This reads post_daywise.csv and calculates the LIWC values on a day wise basis.
	-	Generates daywise bar graph for the LIWC category in pdf
	-	Creates <cateogory>_LIWC_daywise.csv file with the LIWC values for each day 
