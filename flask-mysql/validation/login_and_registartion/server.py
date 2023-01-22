from app import app
from app.controllers import registrations, logins


if __name__ == "__main__":
    app.run(debug=True, port=5001)
