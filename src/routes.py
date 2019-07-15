# -*- coding: utf8 -*-

from app import app
from src import mainfunc
import requests, os, json

from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from src.models import User, Site
from app import login_manager, db, log
from src import forms
import sqlalchemy


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    form_file = forms.UploadFile()
    form_search = forms.AddSiteForm()
    if form_search.validate_on_submit():
        if '.' in form_search.url.data:
            url = form_search.url.data
            site = Site(url=url)
            if Site.query.filter(Site.url == url).one_or_none() is None:
                try:
                    requests.get('http://127.0.0.1:5001/add?domain={}'.format(url))
                    db.session.add(site)
                    db.session.commit()
                    return render_template(
                        "index.html",
                        user=current_user,
                        sites=Site.query.all(),
                        form_search=form_search,
                        form_file=form_file
                    )
                except:
                    return render_template(
                        "index.html",
                        user=current_user,
                        sites=Site.query.all(),
                        form_search=form_search,
                        form_file=form_file,
                        error='Не удается подключиться к серверу-обработчику.\nПроверьте подключение.'
                    )


            else:
                return render_template(
                    "index.html",
                    user=current_user,
                    sites=Site.query.all(),
                    form_search=form_search,
                    form_file=form_file,
                    error='Данный URL уже есть в базе данных.'
                )
        else:
            return render_template(
                "index.html",
                user=current_user,
                sites=Site.query.all(),
                form_search=form_search,
                form_file=form_file,
                error="Введите корректное доменное имя."
            )

        return redirect('/')

    if form_file.validate_on_submit():
        f = form_file.file_field.data
        filename = f.filename
        f.save(os.path.join(app.instance_path, filename))
        return redirect(url_for('index'))

    return render_template(
        "index.html",
        user=current_user,
        sites=Site.query.all(),
        form_search=form_search,
        form_file=form_file,
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
    form2 = forms.UploadFile()
    site_type = request.form.get('site_type')
    current_site = Site.query.filter(Site.id == site_id).first()
    return render_template('site.html',
                           site=current_site,
                           user=current_user,
                           webarchive=mainfunc.web_archive(current_site.url)[1:],
                           form_search=form,
                           form_file=form2,
                           criterions=json.loads(current_site.criterions)
                           )


@app.route("/ban/site/<int:site_id>", methods=["GET", "POST"])
def ban_site(site_id):
    form = forms.AddComment()
    comment = form.comment.data
    site_type = request.form.get('site_type')
    current_site = Site.query.filter(Site.id == site_id).first()
    mainfunc.send_to_registrator(current_site.url, site_type, current_site.reg_mail)
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


# @app.route("/upload_file")
# def upload(path)

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/update_db', methods=['GET', 'POST'])
def add_test():
    current_site = Site.query.filter(Site.id == 7).first()
    dict = {'5': 'опа', '10': 'а что это', '14': 'такое у нас'}
    current_site.criterions = json.dumps(dict, ensure_ascii=False, separators=(',', ': '))
    current_site.screen = 'https://www.music-bazaar.com/album-images/vol1001/580/580642/2419480-big/-Ban-[EP]-cover.jpg'
    db.session.commit()
    return redirect(url_for('index'))