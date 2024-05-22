#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template


DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name": "PHS Green Energy",
    "description": "PHS Green Energy Page",
    "author": "Edwin and Jacob",
    "project_name": "PHS Green Energy",
    "keywords": "flask, webapp, tsa",
}


@app.route("/")
def index():
    return render_template("index.html", app_data=app_data, title="Pelham High Green Energy")


@app.route("/overview")
def overview():
    return render_template("overview.html", app_data=app_data, title="Overview")




@app.route("/about")
def about():
    return render_template("about.html", app_data=app_data, title="About")


@app.route("/works_cited")
def works_cited():
    return render_template(f"works_cited.html", app_data=app_data, title="Works Cited")

@app.route("/<subject>/<topic>")
def info(subject, topic):
    return render_template(f"{subject}/{topic}.html", app_data=app_data, title=f"{topic.capitalize()}")

if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)
