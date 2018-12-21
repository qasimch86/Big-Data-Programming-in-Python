#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#%logstart -o
#Variables that contains the user credentials to access Twitter API
access_token = "1336641781-Ciw8QEbir4JTAGDuVbyDrh94civrnq2EiQ0zZgs"
access_token_secret = "DzI8zEVXogTjbB4HOW77ye7exS2D51tuVDpqSVxXjAmo3"
consumer_key = "BqdjWfD5dbKhvCzUBY8r39LEp"
consumer_secret = "7pkbqt9Vg2OtUSBrErFd8mlfyQsvWyGyoNMGz4HKGD7rHlbUdC"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript'])
    #python twitter_streaming.py > twitter_data.txt