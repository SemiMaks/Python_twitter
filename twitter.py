import tweepy

# переменные ключей и токенов
consumer_key = 'JsV6FCCUsCqkKsbc2LzsBLlh2'
consumer_secret = 'flC0NzGyKsrnb8vTLJvUtUoaDkw2UPuchPlgmk3VeFdKKsVkNo'
access_token = '2335158726-XBiP8R9HT7ijIyl0RvHx2UWtmH8gsZYYhXILCY9'
access_token secret = 'hOwHDL2TlQvPS9N0tfNoWd6hV78J8O7xnrpaHGNTFQ45k'

# настройки OAuth API
auth = tweepy.OAuthHandler(JsV6FCCUsCqkKsbc2LzsBLlh2, flC0NzGyKsrnb8vTLJvUtUoaDkw2UPuchPlgmk3VeFdKKsVkNo)
auth.set_access_token(2335158726-XBiP8R9HT7ijIyl0RvHx2UWtmH8gsZYYhXILCY9, hOwHDL2TlQvPS9N0tfNoWd6hV78J8O7xnrpaHGNTFQ45k)
api = tweepy.API(auth)

# текст поста для учетной записи Twitter
