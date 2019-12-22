from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_function, mars_scraping

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_database = mongo.db.mars_db.find_one()
    return render_template("index.html", mars_database=mars_database)



@app.route("/scrape")
def scraper():
    mars = mongo.db.mars_database
    mars_data = scrape_function.scrape_everything()
    mars_database.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

