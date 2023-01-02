from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    # session['usercount'] = request.form['count'] -> not submittting user information so do not need request here
    else:
        session['count'] += 1 
    return render_template("index.html")

@app.route('/increment')
def increment():
    session['count'] += 2 
    return render_template("index.html")



@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/') 

if __name__=="__main__":
    app.run(debug=True, port=5001)