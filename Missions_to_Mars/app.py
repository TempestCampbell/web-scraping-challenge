from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars1

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrapeIt")
def scrape():
    mars = mongo.db.mars
    mars_stuff= scrape_mars1.scrape()
    mars.update({}, mars_stuff, upsert=True)
    return "Scraping successful!"


if __name__ == "__main__":
    app.run()
