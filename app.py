from flask import Flask, render_template, request, redirect
import json
from datetime import datetime as dt

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def display_me():
    """Display information about the user on the 'Me' page."""
    return render_template("strona-wizytowka-me.html")


@app.route('/mypage/contact', methods=['GET'])
def display_contact():
    """Display the contact form on the 'Contact' page."""
    return render_template("strona-wizytowka-contact.html")


@app.route('/mypage/contact', methods=['POST'])
def user_comment():
    """Handle user comments from the contact form and save them to a JSON file."""
    user_name = request.form['usrname']
    user_text = request.form['comment']

    existing_data = []
    try:
        with open('user_comments.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        with open('user_comments.json', 'w') as json_file:
            json.dump(existing_data, json_file)

    date = dt.today()

    data = {
        "user_name": user_name,
        "user_text": user_text,
        "date": date.strftime('%Y-%m-%d %H:%M:%S')
    }

    existing_data.append(data)

    with open('user_comments.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    return redirect("/mypage/contact")


if __name__ == '__main__':
    app.run(debug=True)
