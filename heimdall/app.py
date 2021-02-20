from flask import Flask, render_template, url_for, request

app = Flask(__name__)

svcs = [
    {"id": 1, "name": "service1", "owner": "me", "description": "This is a sample service" },
    {"id": 2, "name": "service2", "owner": "me", "description": "This is a sample service" },
    {"id": 3, "name": "service3", "owner": "me", "description": "This is a sample service" },
    {"id": 4, "name": "service4", "owner": "me", "description": "This is a sample service" },
    {"id": 5, "name": "service5", "owner": "me", "description": "This is a sample service" },
    {"id": 6, "name": "service6", "owner": "me", "description": "This is a sample service" },
    {"id": 7, "name": "service7", "owner": "me", "description": "This is a sample service" }
]

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html", svcs=svcs)

@app.route("/reporting")
def reporting():
    return render_template("reporting.html")

@app.route("/oncall")
def oncall():
    return render_template("oncall.html")