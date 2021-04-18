from flask import Flask, make_response, redirect, render_template, request, url_for

import gpt3

app = Flask(__name__)

interviewees = {
    "Albert Einstein",
    "Bernhard Riemann",
    "Isaac Newton",
}

@app.route("/", methods=["POST"])
def index():
    if "interviewee" not in request.form or request.form["interviewee"] not in interviewees:
        # No interviewee was supplied. Who are we interviewing?
        # Warning: This logic is totally broken/untested. Don't rely on it.
        print(url_for("select"))
        return redirect(url_for("select"))
    else:
        response = make_response()

        if "content" not in request.cookies or "message" not in request.form:
            # We're just starting the interview. The check for "message" in POST data
            # is crucial in case the "content" cookie was present by accident.
            content = gpt3.new_transcript(request.form["interviewee"])
        else:
            content = request.cookies.get("content")
            # The interview has already begun.
            if "summarize" in request.form:
                # No message was sent -- this is just a request to summarize the existing transcript.
                pass
            else:
                # A new message was sent.
                content += request.form["message"]
                content = gpt3.query(content, request.form["interviewee"])
        
        print(content)
        response.set_cookie("content", content)

        response.set_data(render_template("index.html", content=content))

        return response

@app.route("/select")
def select():
    return render_template("select.html")
