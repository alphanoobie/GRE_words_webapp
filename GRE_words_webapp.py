from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run()
