from flask import Flask, render_template
import requests
import datetime
datetime = datetime.datetime.now()
date = datetime.date()

posts = requests.get("https://api.npoint.io/69cedab579464ca0be52").json()

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", posts=posts, date=date)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template("post.html", posts=posts,id=post_id, date=date)



if __name__ == "__main__":
    app.run(debug=True)