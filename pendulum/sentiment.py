from textblob import TextBlob

def empathize(text):
    empathy = TextBlob(text)
    sentiment = empathy.sentiment
    print(sentiment)
    return sentiment
