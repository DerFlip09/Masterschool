from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)


users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


@app.route('/')
def index():
    date_and_time = datetime.now()
    formatted_time = date_and_time.strftime("%d-%m-%Y %H:%M:%S")
    return render_template('index.html', title='Home', user=users, datetime=formatted_time)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/all-users')
def all_user():
    return render_template('all_users.html', users=users)


@app.route('/greet/<name>')
def greet(name):
    return render_template('index.html', title='Home', user=name)


@app.route('/update_country_form')
def update_form():
    return render_template('update_country_form.html')


@app.route('/update_country', methods=["POST"])
def update_country():
    user = request.form["user"]
    country = request.form["country"]
    users[user.capitalize()]["country"] = country
    return f"{user}'s country was updated to {country}!"


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5000)