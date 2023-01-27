from app import app
from app.controllers import users
app.secret_key = "secret..."

if __name__ == "__main__":
    app.run(debug=True, port=5001)
