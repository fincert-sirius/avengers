from app import app
import mainfunc
import requests, os

from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from src.models import User, Site
from app import login_manager, db, log
from src import forms
import sqlalchemy



@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    form_search = forms.AddSiteForm()
    form_file = forms.UploadFile()
    if form_search.validate_on_submit():
        if '.' in form_search.url.data:
            url = form_search.url.data
            site = Site(url=url)
            if Site.query.filter(Site.url == url).one_or_none() is None:
                requests.get('http://127.0.0.1:5001/add?domain={}'.format(url))
                db.session.add(site)
                db.session.commit()

            else:
                return render_template(
                    "index.html",
                    user=current_user,
                    sites=Site.query.all(),
                    form=form_search,
                    error='Данный URL уже есть в базе данных.'
                    )
        else:
            return render_template(
                "index.html",
                user=current_user,
                sites=Site.query.all(),
                form=form_search,
                error='Пожалуйста, введите корректный URL.'
            )
    elif form_file.validate_on_submit():
        if request.method == 'POST':
            file = request.files['file']
            if file and mainfunc.allowed_file(file.filename):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                return redirect(url_for('/',
                                        filename=file.filename))
            else:
                return render_template(
                    "index.html",
                    user=current_user,
                    sites=Site.query.all(),
                    form=form_search,
                    error="Ебаная залупа №1"
                )
        else:
            return render_template(
                "index.html",
                user=current_user,
                sites=Site.query.all(),
                form=form_search,
                error="Ебаная залупа №2"
            )




    #return redirect('/')

    return render_template(
        "index.html",
        user=current_user,
        sites=Site.query.all(),
        form=form_search,
        error=None
    )



@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = forms.LoginForm()

    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        user = User.query.filter(User.username == login).one_or_none()

        if user is None or user.password_hash != password:
            return render_template(
                "login.html",
                login=login,
                error="Wrong password or login",
                form=form
            )

        login_user(user)

        return redirect(url_for("index"))

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))


@app.route("/add", methods=["GET", "POST"])
def add_site():
    return redirect(url_for('index'))


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    form = forms.AddUserForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        user = User(username=login, password_hash=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_user.html",
                           form=form
                           )


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    form_file = forms.UploadFile()
    if form_file.validate_on_submit():
        f = form_file.file_field.data
        filename = f.filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    return render_template("upload_file.html", form=form_file, user=current_user)


@app.route("/site/<int:site_id>", methods=["GET", "POST"])
def site_info(site_id):
    form = forms.AddSiteForm()
    current_site = Site.query.filter(Site.id == site_id).first()
    return render_template('site.html',
                           site=current_site,
                           user=current_user,
                           webarchive=mainfunc.web_archive(current_site.url)[1:],
                           form=form
                           )

@app.route("/ban/site/<int:site_id>", methods=["GET", "POST"])
def ban_site(site_id):
    form = forms.AddComment()
    comment = form.comment.data
    current_site = Site.query.filter(Site.id == site_id).first()
    current_site.status = 'BLOCKED'
    current_site.comment = comment
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/clear/site/<int:site_id>", methods=["GET", "POST"])
def clear_site(site_id):
    current_site = Site.query.filter(Site.id == site_id).first()
    current_site.status = 'GOOD_SITE'
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/ban404")
def opa():
    return render_template("ban.html")
