from app import app
#from app.controllers import 

app.secret_key = "Secret..."


if __name__ == "__main__":
    app.run(debug=True, port=5001)
