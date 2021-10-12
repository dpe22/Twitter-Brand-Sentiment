# Twitter-Brand-Sentiment
These python programs utilize Twitter Search API and Google Cloud Natural Language API. Recent tweets about a company of your choice are aggregated into a text file and fed into Google's Natural Language AI for sentiment analysis, where they receive quantitative scores that are returned to the user. 

Originally conceptualized as a way for brands to track social media campaign performance, this project evolved due to Twitter Search API constraints: it's not possible to filter out paid content from the search without a higher tier plan. That makes a general search for a brand name mostly ineffective for sentiment analysis because it returns mostly paid product ads and content. So instead, the program was redirected using more specific search language "working for COMPANY" or "working at COMPANY". It's not a broad net, and could certainly be expanded, but it is sufficient to demonstrate proof of concept. 

# User Stories
  1. The Candidate: Seeking employment, the candidate turns to Twitter to see real-time sentiment of current employees, drawing inferences about working conditions and issues. 
  2. The Employee: Seeking validation, the employee uses this product as a means of justifying change to management using real-time data.
  3. The Employer: Seeking to create value for employees, customers, and stakeholders, while protecting and building brand equity, the employer uses this product to evaluate and improve company culture and reputation. 

# Important Caveats
Brand Results are less reliable due to generic classification, e.g. Apple tweet collection samples may include irrelevant tweets about fruit, or paid advertisements.
