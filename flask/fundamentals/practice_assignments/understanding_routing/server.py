from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    # if == None:
    #     return render_template('error.html')

    # else:
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return "Hello, " + name + "!" 

@app.route('/repeat/<int:num>/<string:thing>')
def repeat(num, thing):
    return f"{thing * num}"



if __name__=="__main__":
    app.run(debug=True, port=5001)