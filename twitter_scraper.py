from ntscraper import Nitter
import schedule, time

twitter_accounts = [
    "Mr_Derivatives",
    "warrior_0719",
    "ChartingProdigy",
    "allstarcharts",
    "yuriymatso",
    "TriggerTrades",
    "AdamMancini4",
    "CordovaTrades",
    "Barchart",
    "RoyLMattox"
]

ticker_symbol = "$TSLA"

interval_minutes = 15

def scrape_account(account, ticker):
    response = Nitter().get_tweets(account, mode='user', number=150)
    
    count = 0
    for tweet in response.get('tweets'):
        tweet_text = tweet.get('text')
        if ticker in tweet_text:
            count += 1

    return count

def scrape_all_accounts():
    total_mentions = 0
    for account in twitter_accounts:
        count = scrape_account(account, ticker_symbol)
        total_mentions += count
    
    print(f"'{ticker_symbol}' was mentioned '{total_mentions}' times in the last '{interval_minutes}' minutes.")

scrape_all_accounts()

schedule.every(interval_minutes).minutes.do(scrape_all_accounts)

while True:
    schedule.run_pending()
    time.sleep(1)
