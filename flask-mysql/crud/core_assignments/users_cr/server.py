from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/read')
def read_all():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)


@app.route('/user/new')
def form():
    return render_template("create.html")


@app.route('/user/new/process', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect('/read')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
