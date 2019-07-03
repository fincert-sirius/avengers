from app import app
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from src.models import User
from app import login_manager

@app.route("/")
@login_required
def index():
    return render_template("index.html", user=current_user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("login.html")

    user_id = request.form["login"]
    user = User.query.get(user_id)

    if user is None or user.password_hash != request.form["password"]:
        return render_template("login.html", login=user_id, error="Wrong password or login")

    login_user(user)

    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))

