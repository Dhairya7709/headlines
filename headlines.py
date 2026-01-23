from flask import Flask,render_template,request
import feedparser
app = Flask(__name__)

NEWS_FEED = {"bbc": "http://feeds.bbci.co.uk/news/rss.xml",
             "fox": "https://moxie.foxnews.com/google-publisher/latest.xml",
             "cnn": "http://rss.cnn.com/rss/edition.rss%20"}

@app.route("/")
@app.route("/<publication>")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in NEWS_FEED:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(NEWS_FEED[publication])
    articles = feed['entries']
    return render_template("home.html",articles = articles)
if __name__ == '__main__':
    app.run(debug=True,port=5500)