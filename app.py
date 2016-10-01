from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from import simplejson as json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test@mysql:3306/test'
db = SQLAlchemy(app)
exp_id=1;
class EXP_SYS(db.Model):
    eid=db.Column(db.Integer,primary_key=true)
    name=db.Column(db.String(40),unique=true)
    email=db.Column(db.String(40),unique=true)
    category=db.Column(db.String(40),unique=false)
    description=db.Column(db.String(40),unique=true)
    link=db.Column(db.String(80),unique=false)
    estimated_costs=db.Column(db.Integer,unique=false)
    submit_date=db.Column(db.Date,unique=true)
    status=db.Column(db.String(40),unique=false)
    decision_date=db.Column(db.String(40),unique=true)

    def __init__(eid,name,email,category,description,link,estimated_costs,submit_date,status,decision_date):
        self.name=name
        self.eid=eid
        self.email=email
        self.category=category
        self.description=description
        self.link=linkp
        self.estimated_costs=estimated_costs
        self.submit_date=submit_date
        self.status=status
        self.decision_date=decision_date



@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/expenses")
def expenses():
    json_data=request.json;
    db.create_all();
    db.session.commit();
    e=EXP_SYS(exp_id,json_data['name'],json_data['email'],json_data['category'],json_data['description00'],json_data['link'],json_data['estimated_costs'],json_data['submit_date'])
    db.session.add(e);
    db.session.commit();

@app.route("/v1")
def v1():
    return "!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
