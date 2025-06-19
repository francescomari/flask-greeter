# How to Greet in Flask

This repository is a simple web application built with [Flask][1] that asks
users for their name, remembers them using sessions, and greets users by name.
This application also shows how to publish flash messages for one-time
notifications and explores some more advanced templating techniques.

## Prerequisites

This repository builds upon the concepts explored in [Introduction to Flask][2]
and [To-Do List in Flask][3], which will not be repeated here. The application
can be set up and executed as described in [Introduction to Flask][2].

## Explore the code

The [web server](app.py) defines the routes to serve the two pages of this
application, to handle form submissions, and to manage the session.

The [base template](templates/base.html) defines the layout for all the pages in
this application, and the [index page template](templates/index.html) and the
[greeting page template](templates/greet.html) both extend from the base
template to avoid repetition.

[1]: https://flask.palletsprojects.com/en/stable/
[2]: https://github.com/francescomari/flask-introduction
[3]: https://github.com/francescomari/flask-todo
