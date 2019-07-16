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

        return redirect(url_for('index'))

    if request.method == ["POST"]:
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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


@app.route("/upload", methods=["POST"])
def upload():
    form_file = forms.UploadFile()
    form_search = forms.AddSiteForm()

    target = os.path.join(app.config['UPLOAD_FOLDER'])
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)
    urls = mainfunc.upload_file(destination)
    for url in urls:
        site = Site(url=url)
        if Site.query.filter(Site.url == url).one_or_none() is None:
            try:
                requests.get('http://127.0.0.1:5001/add?domain={}'.format(url))
                db.session.add(site)
                db.session.commit()
            except:
                return render_template(
                    "index.html",
                    user=current_user,
                    sites=Site.query.all(),
                    form_search=form_search,
                    form_file=form_file,
                    error='Не удается подключиться к серверу-обработчику.\nПроверьте подключение.'
                )


    return redirect(url_for('index'))

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
                           criterions=json.loads(current_site.criterions),
                           whois_data=json.loads(current_site.whois_data)
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


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/update_db', methods=['GET', 'POST'])
def add_test():
    current_site = Site.query.filter(Site.id == 7).first()
    dict = {'5': 'опа', '10': 'а что это', '14': 'такое у нас'}
    whoisraw = '''Domain Name: acegw.com
Registry Domain ID: 2251995052_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.maff.com
Registrar URL: http://www.maff.com
Updated Date: 2019-03-13T13:17:32Z
Creation Date: 2018-04-14T02:50:37Z
Registrar Registration Expiration Date: 2020-04-14T02:50:37Z
Registrar: MAFF Inc.
Registrar IANA ID: 817
Registrar Abuse Contact Email: email@maff.com
Registrar Abuse Contact Phone: +86.5925990220
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited 
Registry Registrant ID: 
Registrant Name: hui tian
Registrant Organization: tianhui
Registrant Street: pulandianshi,lianshanzhen,shuimenzicun,chengzigout
Registrant City: dalianshi
Registrant State/Province: liaoning
Registrant Postal Code: 116200
Registrant Country: China
Registrant Phone: +86.15998101049
Registrant Phone Ext: 
Registrant Fax: +86.15998101049
Registrant Fax Ext: 
Registrant Email: email@qq.com
Registry Admin ID: 
Admin Name: hui tian
Admin Organization: tianhui
Admin Street: pulandianshi,lianshanzhen,shuimenzicun,chengzigout
Admin City: dalianshi
Admin State/Province: liaoning
Admin Postal Code: 116200
Admin Country: China
Admin Phone: +86.15998101049
Admin Phone Ext: 
Admin Fax: +86.15998101049
Admin Fax Ext: 
Admin Email: email@qq.com
Registry Tech ID: 
Tech Name: hui tian
Tech Organization: tianhui
Tech Street: pulandianshi,lianshanzhen,shuimenzicun,chengzigout
Tech City: dalianshi
Tech State/Province: liaoning
Tech Postal Code: 116200
Tech Country: China
Tech Phone: +86.15998101049
Tech Phone Ext: 
Tech Fax: +86.15998101049
Tech Fax Ext: 
Tech Email: email@qq.com
Name Server: V1.DNSDUN.COM
Name Server: V1.DNSDUN.NET
DNSSEC: Unsigned'''
    dict_whois = {}
    for i in whoisraw.split('\n'):
        i = i.split(':')
        dict_whois[i[0]] = ':'.join(i[1:])
    #dict2 = {(i[0], i[1]) for i in whoisraw.split('\n')}
    current_site.whois_data = json.dumps(dict_whois, ensure_ascii=False, separators=(',', ':'))
    current_site.criterions = json.dumps(dict, ensure_ascii=False, separators=(',', ': '))
    current_site.screen = 'https://www.music-bazaar.com/album-images/vol1001/580/580642/2419480-big/-Ban-[EP]-cover.jpg'
    db.session.commit()
    return redirect(url_for('index'))