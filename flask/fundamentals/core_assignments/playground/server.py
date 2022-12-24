from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:num>')
def play_num(num):
    
    for i in range (0, num):
        return render_template('play.html') 

if __name__ == "__main__":
    app.run(debug=True, port=5001)
