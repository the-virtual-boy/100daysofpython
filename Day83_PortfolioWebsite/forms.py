from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, EqualTo, Email
from flask_ckeditor import CKEditorField

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit Post")