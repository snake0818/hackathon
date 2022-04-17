from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello!!"

@app.route("/API_Data",methods=['POST'])
def postInput():
    return "This is Test."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
