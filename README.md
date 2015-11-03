# social-computing-project
This is the code for the social computing project at Gatech

1.	Run sed 1p post*.csv > merged.csv 
    -   This combines all the posts file into a single csv merged.csv

2.  Run remove_duplicates_posts.csv
    -   This reads merge.csv and removes duplicates
    -   Generates combined_posts.csv
	
3.  Run sed1p comments*.csv >merged.csv
    - This combines all the comments into a single merged.csv

4. Run remove_duplicates_comments.csv
    - This reads merge.csv and removed duplicates
    - Generates combined_comment.csv

3.	Run get_words_inposts.py 
	-	use the combined_posts.csv file to get the number of words column.
	-	This generates a combined_post_with_counts.csv file with all the counts
	
4.	Run get_words_incomments.py
	-   use the combined_comments.csv file to get the number of words column.
	-	This generates a combined_comments_with_counts.csv with all the counts
	
5.	Run getLIWC.py combined_post_with_counts.csv
	-	this generates combined_emotions_post.csv
	-	This contains a list of 2 emotions from liwc for that post file
	-	emotions categories can be changed in the code
	
6.	Run getLIWC.py combined_comments_with_counts.csv
	-	This generates combined_emotions_comments_unique.csv
	-	This contains a list 2 same emotions as above for that comment file
	-	emotion categories can be changed as above
	
7.	Run plots.py 
    -   This reads the combined_emotions_post.csv and combined_emotions_comments_unique.csv
	-	This generates graphs and scatter plots for the emotions we choose above
	
8.	Run timeline_posts.py 
	-	This read combined_posts.csv.
	-	Generates a timeline of posts on a daily bases

9.	Run post_daywise.py 
	-	This reads combined_post_with_counts.csv
	-	creates combined_post_daywise.csv

10.	Run LIWC_daywise.py (LIWC category)
	-	This reads combined_post_daywise.csv and calculates the LIWC values on a day wise basis.
	-	Generates daywise bar graph for the LIWC category and creates (category)_daily.pdf
	-	Creates (category)_LIWC_daywise.csv file with the LIWC values for each day 

11. Run post_hour.py
 	-	This reads combined_post_with_counts.csv and (In future will use combined post file having number of words_
 	-	creates combined_post_hourly.csv

12. Run LIWC_hour.py (LIWC category)
	-	This read combined_post_hourly.csv and calculates the LIWC values on an hour wise basis
	-	Generates a hourwise bar graph for the LIWC category and creates (category)_hourly.pdf
	-	Creates (category)_LIWC.hourly.csv file with the LIWC values for each hour.
