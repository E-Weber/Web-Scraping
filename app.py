from flask import Flask, render_template, redirect
from flask_PyMongo import PyMongo
import scrape_mars.py

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsDB")


# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    mars = mongo.db.Mars.find()
    print(mars)
    return render_template("index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars = mongo.db.Mars()
    marsData = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars.update({}, marsData, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
