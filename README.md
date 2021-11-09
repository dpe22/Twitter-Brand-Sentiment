# Twitter-Brand-Sentiment
## To Start: Run companySentiment.py, or run the query modules sequentially to generate results. 
These python programs utilize Twitter Search API and Google Cloud Natural Language API. Recent tweets about a company of your choice are aggregated into a text file and fed into Google's Natural Language AI for sentiment analysis, where they receive quantitative scores that are returned to the user. 

Originally conceptualized as a way for brands to track social media campaign performance, this project evolved due to Twitter Search API constraints: it's not possible to filter out paid content from the search without a higher tier plan. That makes a general search for a brand name mostly ineffective for sentiment analysis because it returns mostly paid product ads and content. So instead, the program was redirected using more specific search language "working for COMPANY" or "working at COMPANY". It's not a broad net, and could certainly be expanded, but it is sufficient to demonstrate proof of concept. 

# User Stories
  1. The Candidate: Seeking employment, the candidate turns to Twitter to see real-time sentiment of current employees, drawing inferences about working conditions and issues. 
  2. The Employee: Seeking validation, the employee uses this product as a means of justifying change to management using real-time data.
  3. The Employer: Seeking to create value for employees, customers, and stakeholders, while protecting and building brand equity, the employer uses this product to evaluate and improve company culture and reputation. 

# Possible Unit Tests
- What if the user tries to select a function outside the range {brand, employee}? 
- What if the user enters multiple company names? 
- What if the user doesn't use UTF-8 encoded characters to enter the company name? How does Twitter API endpoint respond? How does program respond? 
- What if the user enters a string longer than 280 character tweet limit?
- What if the user enters a gibberish string?

# Important Caveats
Brand results are less reliable than employee results because the employee query is more narrowly defined, e.g. For brand sentiment analysis, Apple tweet collection samples may include irrelevant tweets about fruit, or paid advertisements. Whereas for employee sentiment analysis, the tweet must include "working for" or "working at" and so produces slightly more relevant results. 
