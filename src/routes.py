from app import app
import mainfunc

from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from src.models import User, Site
from app import login_manager, db, log
from src import forms
import sqlalchemy

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = forms.AddSiteForm()
    if form.validate_on_submit() and '.' in form.url.data:
        url = form.url.data
        site = Site(url=url)
        #existing_site =
        if Site.query.filter(Site.url == url).one_or_none() is None:
            db.session.add(site)
            db.session.commit()
        else:
            return render_template(
                "index.html",
                user=current_user,
                sites=Site.query.all(),
                form=form,
                error='Данный URL уже есть в базе данных.'
                )

        return redirect('/')

    return render_template(
        "index.html",
        user=current_user,
        sites=Site.query.all(),
        form=form,
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


@app.route("/upload_excel", methods=["GET", "POST"])
def upload_sites_excel():
    form = forms.UploadSitesExcel()
    if form.validate_on_submit():
        f = form.excel.data
        pass

    return render_template("upload_sites_excel.html",
                           form=form
                           )

# @app.route("/")

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
#@app.route("/upload_file")
#def upload(path)