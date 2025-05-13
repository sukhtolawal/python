from flask import Flask,request

from flask_cors import CORS  

# Create Flask app and SocketIO instance
app = Flask(__name__)
CORS(app)





@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    # Run the Flask app
    app.run()