from flask import Flask, request, render_template, redirect, session, flash, url_for

app = Flask(__name__)

# This application needs to use sessions, and sessions can only be enabled if
# Flask is configured with a secret key. The secret key can be any string, but
# in a production-ready application it should be a cryptographically random
# string. The secret key is used to sign cookies, which allows Flask to verify
# that the cookies received from the client have been generated from this
# server. For more information about sessions, see:
#
# https://flask.palletsprojects.com/en/stable/quickstart/#sessions
#
# For the purpose of a small demo application like this one, the value we give
# below is enough – and it is a good reminder to replace it with something
# better if this application becomes popular and we publish it on the Internet.

app.secret_key = "<replace>"


@app.get("/")
def index():
    return render_template("index.html")


# The "set_name" route processes the form that the user submits to give the
# application their name. If the name is empty, the route flashes an error
# message and redirects the user to the index page. Otherwise, the route saves
# the name in the session and redirects the user to the greeting page. For more
# information about flash messages, see:
#
# https://flask.palletsprojects.com/en/stable/patterns/flashing/
#
# Note how this route uses the post-redirect-get pattern to prevent the user
# from accidentally resubmitting this form by hitting the refresh button.


@app.post("/")
def set_name():
    name = request.form["name"]
    if not name:
        flash("Please enter a valid name!")
        return redirect(url_for("index"))
    session["name"] = name.title()
    return redirect(url_for("greet"))


# The "greet" route is responsible for showing a greeting message to the current
# user. The name of the current user must have been saved in the session. If the
# name of the user is not in the session, the user didn't give their name to the
# application. Therefore, we flash an error message and redirect the user to the
# index page. Otherwise, the route sets the user's name in the template
# variables and renders the greeting page.
#
# Note that, if the user's name is not found in the session, we redirect the
# user to the index page. This forces the browser to perform a new request to
# the index page, which will consume the flash message and display it. Redirects
# are not limited to the post-redirect-get pattern!


@app.get("/greet")
def greet():
    name = session.get("name")
    if not name:
        flash("I can't greet you if you don't tell me your name first!")
        return redirect(url_for("index"))
    return render_template("greet.html", name=name)


# The "forget" route is similar to a "logout" functionality. The user asks to be
# forgotten, which results from the application to remove the user's name from
# the session. Because this link can be clicked by a user that didn't disclose
# his name, this route flashes different messages depending on whether the name
# of the user was known or not. Either way, we redirect the user's browser to
# the index page.


@app.get("/forget")
def forget():
    name = session.pop("name", None)
    if not name:
        flash("I don't even know you!")
    else:
        flash("I forgot you...")
    return redirect(url_for("index"))
