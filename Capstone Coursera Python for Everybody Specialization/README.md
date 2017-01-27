For my "Python for Everybody" Capstone project, I chose to produce a word cloud
by analyzing the text transcripts of more than 400 speeches by Barack Obama.

The texts were scraped from "http://www.americanrhetoric.com/barackobamaspeeches.htm" using urllib and parsed using Beautiful Soup.

The scraping and cleanup/analysis is a two-step Python program.

Step 1. Run [bs_speeches.py](bs_speeches.py) in the terminal to extract data and dump it to a txt file (bs_write.txt).

Step 2. Run [gword.py](gword.py) to clean data, create a word-count dictionary and dump it to a
JavaScript file (the html, js and d3 files are templates provided by Coursera).

Open gword.htm to view the word cloud.

A [screenshot](cloud_screenshot.png) of the final output is included. 
