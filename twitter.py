import tweepy

# переменные ключей и токенов
consumer_key = 'JsV6FCCUsCqkKsbc2LzsBLlh2'
consumer_secret = 'flC0NzGyKsrnb8vTLJvUtUoaDkw2UPuchPlgmk3VeFdKKsVkNo'
access_token = '2335158726-XBiP8R9HT7ijIyl0RvHx2UWtmH8gsZYYhXILCY9'
access_token_secret = 'hOwHDL2TlQvPS9N0tfNoWd6hV78J8O7xnrpaHGNTFQ45k'

# настройки OAuth API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# текст поста для учетной записи Twitter
tweet = 'Пробная запись!'
api.update_status(status=tweet)

print ('Запись добавлена успешно!')
