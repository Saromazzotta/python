from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/play')
def play_level_1():
    return render_template("play.html",num=3,color="blue")

@app.route('/play/<int:num>')
def play_level_2(num):
    return render_template("play.html", num=num, color="blue")
    # for i in range (0, num):
    #     return render_template('play.html', num=num) 


@app.route('/play/<int:num>/<string:color>')
def play_level_3(num, color):
    return render_template("play.html", num=num, color=color)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
