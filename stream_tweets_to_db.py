from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymysql
import time
import json

conn = pymysql.connect("lorenzoostano.mysql.pythonanywhere-services.com", "lorenzoostano", "lo301414",
                       "lorenzoostano$default")

c = conn.cursor()

# consumer key, consumer secret, access token, access secret.
ckey = "xG85OfFdDhnPS3CQ2dbDAUY0m"
csecret = "p56MqFNOE7fyH7TJxpc1cHRAgCfFB4fIQ6Qgm59Q2MoJG5jXAO"
atoken = "91334722-CqXu1Czm8kXlwhffar2oGkOUAC8YLo2urOquV39PV"
asecret = "u1FoOTBjq9htyBcNI8rtUdoX9ToVjZMsFzSzu3Q7h7bah"


class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]

            username = all_data["user"]["screen_name"]

            c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
                      (time.time(), username, tweet))

            conn.commit()

            print((username, tweet))

            return True
        except BaseException as e:
            print('failed ondata,', str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])