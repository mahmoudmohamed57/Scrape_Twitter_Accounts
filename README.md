# Scrape Twitter Accounts
### Description
This Python script scrapes tweets from a list of specified Twitter accounts every m minutes, looking for mentions of a particular ticker symbol. It uses the ntscraper package to fetch the latest t tweets from each account and counts how many times the ticker symbol appears. The results are printed out, showing the total number of mentions within the interval. The script runs continuously, checking and executing the scraping task at the scheduled intervals.
#