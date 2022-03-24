import tweepy

# переменные ключей и токенов
consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_token_secret = 'token_secret'

# настройки OAuth API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# текст поста для учетной записи Twitter
tweet = 'Пробная запись!'
api.update_status(status=tweet)

print ('Запись добавлена успешно!')
