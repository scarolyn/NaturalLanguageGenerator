# NaturalLanguageGenerator
Code Suisse Challenge

NLG.py - code for natural language generator
This code contains all the functions for how to create sentences. All of the functions were then combined into
a paragraph in the paragraph() function. We debugged by running this program using mock variables.

Ticker.py - code for our Ticker object
Tickers are the headers in csv file that we care about analyzing. We created an object to have a more object oriented
design. It contains fields concerning each type of individual ticker.

FrameFunctions.py - code for manipulating dataframes
We used the pandas library in python to interpret the csv files and turn the data into time series. These are the
functions to get the information we need from the frames and csv.

Tests.py - code for unit tests
In the preliminary stages of testing our functions, we wrote black box unit tests to make sure that the output matched
the expectation. As we added more language, the original tests may have been less relevant in the end when we wanted to
change phrasing.

page.py - flask code to get a webpage
Integrated flask to host the UI

/templates/Page.html - code for html webpage

To get webpage:
-run flask on page.py using an IDE (pycharm)
-click on the localhost link that it outputs
-type in the two dates. date 1 must be before date 2
-receive the paragraph page with the natural language generator analysis


