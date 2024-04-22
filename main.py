import tweepy   # "pip3 install tweepy" on terminal.
import time

#Twitter profile APIs' (developer.twitter.com).
api = tweepy.Client(
    consumer_key='',  #Information given on developer twitter website.
    consumer_secret='',
    access_token='',
    access_token_secret=''
)


print("\n\n Starting to prepare the tweets ...\n\n")

#To wait "10" seconds before going to the next line of the code
time.sleep(10)


#TWEETS
tweet1 = "Hey there"
tweet2 = "This is a twitter bot"


#"While" to keep posting
while True:
        try:
                tweet = api.create_tweet(text=tweet1)  #Will post the "tweet1"
                print("\n\nTweeted!!\n" + tweet1 + "\n")  #To see what's was done in terminal
        except Exception as error:   #Error handling
                print(error)

#Tweet can't be the same twice, add something on the end to be different
        tweet1 = tweet1 + "✌🏼"

        time.sleep(30)

#Tweet2
        try:
                tweet = api.create_tweet(text=tweet2)  
                print("\n\nTweeted!!\n" + tweet1 + "\n") 
        except Exception as error:   
                print(error)

        tweet2 = tweet2 + "🚀"

        time.sleep(30)


"""
On Twitter it will be:


Hey there
This is a twitter bot

Hey there✌🏼
This is a twitter bot🚀

Hey there✌🏼✌🏼
This is a twitter bot🚀🚀

Hey there✌🏼✌🏼✌🏼
This is a twitter bot🚀🚀🚀

......


"""