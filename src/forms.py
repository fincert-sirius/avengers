from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.widgets import TextArea
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError


def URL_NEW(form, field):
    message = "Пожалуйста, введите корректный URL."
    d = field.data
    if ('.' not in d):
        raise ValidationError(message)
    return field.data


class LoginForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class AddSiteForm(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


class AddUserForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class UploadFile(FlaskForm):
    file_field = FileField('file', validators=[FileRequired(), FileAllowed(['txt', 'csv', 'json', 'xml'],
                                                                     'Некорректный формат(Допустимы только .csv, .json, .xml, .txt)')])


class AddComment(FlaskForm):
    comment = StringField(u'Comment', widget=TextArea())
