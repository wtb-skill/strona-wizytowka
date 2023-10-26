from flask import Flask, render_template, request, redirect
import json
from datetime import datetime as dt

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def visit_me():
    return render_template("strona-wizytowka-me.html")


@app.route('/mypage/contact', methods=['GET'])
def visit_contact():
    return render_template("strona-wizytowka-contact.html")


@app.route('/mypage/contact', methods=['POST'])
def user_comment():
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
