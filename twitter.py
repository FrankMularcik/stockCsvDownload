import tweepy
import youtube
import os

#authorize to the twitter API, you have to apply for a twitter developer account to get these keys that will work for your own twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

#This is an example of what the keys look like but you have to get your own from twitter in order to use this with your own twitter account
#auth = tweepy.OAuthHandler("bsU2LhDDQRRJono7CYZGHT5AY", "GOyefv0Ab5BrBhUGGbu2ku9dOW7CME5o3xR0qquxDw1DBFAuT8")
#auth.set_access_token("1304208352168177664-bIqUfGbgpEVsaV16h2pMNK6uKZqsPL", "t15WoeUTKOPdiE5dVmYw4kItfsiYKnSP4x75Y1PnG2oZB")

tweet = tweepy.API(auth)

#upload video, title, and thumbnail to twitter
tweet.update_with_media(youtube.thumbnail, "Check out my latest video:\n\n" + youtube.title + "\n\n" + youtube.vidurl)

#delete the thumbnail that was downloaded
os.remove(youtube.thumbnail)



