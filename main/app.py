from flask import Flask
app = Flask(__name__)

# routes in flask are created using @app.route
@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run