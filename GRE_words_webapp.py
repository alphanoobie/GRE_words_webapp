from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from numpy import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
db = SQLAlchemy(app)

#word_db = db.Table('Words', db.metadata, autoload=True, autoload_with=db.engine)
Base = automap_base()
Base.prepare(db.engine, reflect = True)
Words = Base.classes.Words

@app.route("/")
def home():
    x = random.randint(1,333)
    random_row = db.session.query(Words).get(x)
    return render_template("index.html", random_row=random_row)
 
if __name__ == "__main__":
    app.run()
