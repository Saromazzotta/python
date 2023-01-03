from flask import Flask, render_template, redirect, request, session

app = Flask (__name__)
app.secret_key = "Secret..."

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/process', methods=['POST'])
def process():
    print("Got Form Info")
    print(request.form)
    session['username'] = request.form['name']
    session['userlocation'] = request.form['locations']
    session['userlanguage'] = request.form['languages']
    session['userhours'] = request.form['hours'] #only showing whether radio button is true or false
    session['usercheck'] = request.form['choice'] #only showing whether checkbox is true or false
    session['usercomment'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)