import imagegen
import twitter

[quote,author]=imagegen.generate_image()
text = "\"" + quote + "\"" + " " + author + "  #CCDZNMotivation #Motivation #MotivationalQuotes"
twitter.tweet_img(texts=text)
