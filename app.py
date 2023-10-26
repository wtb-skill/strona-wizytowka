from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def visit_me():
    return render_template("strona-wizytowka-me.html")


@app.route('/mypage/contact', methods=['GET'])
def visit_contact():
    return render_template("strona-wizytowka-contact.html")


# @app.route('/hello')
# def hello():
#     my_name = "John"
#     return f'Hello, {my_name}!'
#
#
# @app.route('/blog', methods=['GET'])
# def blog_main():
#     return f"This is a main blog page"
#
#
# @app.route('/blog/<_id>')
# def blog(_id):
#     return f"This is blog entry #{_id}"
#
#
# @app.route('/message', methods=['GET', 'POST'])
# def message():
#     if request.method == 'GET':
#         print("We received GET")
#         return render_template("form.html")
#     elif request.method == 'POST':
#         print("We received POST")
#         print(request.form)
#         return redirect("/")
#
#
# @app.route("/warehouse")
# def warehouse():
#     items = ["screwdriver", "hammer", "saw"]
#     text = "Przykładowy tekst"
#     errors = ["hammer is broken!"]
#     return render_template("warehouse.html", items=items, text=text, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)
