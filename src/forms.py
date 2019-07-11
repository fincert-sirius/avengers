from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.widgets import TextArea
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, URL

class LoginForm(FlaskForm):
	login = StringField('login', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

class AddSiteForm(FlaskForm):
	url = StringField('url', validators=[DataRequired(), URL() ])

class AddUserForm(FlaskForm):
	login = StringField('login', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])

class UploadSitesExcel(FlaskForm):
	excel = FileField('excel', validators=[FileRequired()])

class AddComment(FlaskForm):
	comment = StringField(u'Comment',widget=TextArea())