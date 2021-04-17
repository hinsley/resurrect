from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

interviewees = {
    "albert einstein",
    "bernhard riemann",
    "isaac newton",
}

@app.route("/", methods=["GET"])
def index():
    if "interviewee" not in request.args or request.args["interviewee"] not in interviewees:
        print(url_for("select"))
        return redirect(url_for("select"))
    else:
        return render_template("index.html")

@app.route("/select")
def select():
    return render_template("select.html")
