from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.widgets import TextArea
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Length
from string import ascii_letters


def URL_NEW(form, field):
    message = "Пожалуйста, введите корректный URL."
    d = field.data
    if ('.' not in d):
        raise ValidationError(message)
    return field.data

def validate_rus(form, field):
    if not any(i in field.data for i in ascii_letters):
        raise ValidationError('Нельзя кириллицей')

# class UrlForm(Form):
#     url = StringField('Name', [DataRequired(), Length(min=3, max=100)])

#     def validate_url(form, field):
#         if '.' not in field.data:
#             raise ValidationError('Некорректный URL')





class LoginForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class AddSiteForm(FlaskForm):
    url = StringField('url', validators=[DataRequired(), Length(min=3, max=100), validate_rus])


class AddUserForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class UploadFile(FlaskForm):
    file_field = FileField('file', validators=[FileRequired(), FileAllowed(['txt', 'csv', 'json', 'xml'],
                                                                     'Некорректный формат(Допустимы только .csv, .json, .xml, .txt)')])


class AddComment(FlaskForm):
    comment = StringField(u'Comment', widget=TextArea())
